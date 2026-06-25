from groq import Groq
from dotenv import load_dotenv
import json
import os
from tools import get_order, search_products, get_product
 
load_dotenv()
 
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
 
TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "get_order",
            "description": "Fetch order details like status, address, and ETA using an order ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "Order ID e.g. ORD-1001"
                    }
                },
                "required": ["order_id"]
            }
        }
    },
    {
    "type": "function",
    "function": {
        "name": "search_products",
        "description": "Search products in the catalog. Optionally filter by max price to find cheaper alternatives.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search keyword e.g. shoes or Nike or puma"
                },
                "max_price": {
                    "type": "integer",
                    "description": "Maximum price filter in rupees. Use this when looking for cheaper alternatives."
                }
            },
            "required": ["query"]
        }
    }
},
    {
        "type": "function",
        "function": {
            "name": "get_product",
            "description": "Fetch full details of a product using its product ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {
                        "type": "string",
                        "description": "Product ID e.g. P-101"
                    }
                },
                "required": ["product_id"]
            }
        }
    }
]
 
def call_tool(tool_name, tool_input):
    if tool_name == "get_order":
        return get_order(tool_input["order_id"])
    elif tool_name == "search_products":
        max_price = tool_input.get("max_price", None)
        return search_products(tool_input["query"], max_price)
    elif tool_name == "get_product":
        return get_product(tool_input["product_id"])
    else:
        return {"error": f"Unknown tool: {tool_name}"}
 
def run_agent(question: str, chat_history: list = []) -> dict:
    print(f"\nQuestion: {question}")
    print("-" * 40)
 
    # Only keep last 6 messages to avoid context issues
    recent_history = chat_history[-6:] if len(chat_history) > 6 else chat_history
 
    messages = recent_history + [{"role": "user", "content": question}]
    tool_log = []
 
    system = """You are ShopBot, a helpful and smart customer support agent for an online store.
 
You have access to tools to fetch order and product information from the database.
 
HOW TO ANSWER:
1. If the question is about a specific order (e.g. ORD-1001) → use get_order tool
2. If the question is about a specific product ID (e.g. P-101) → use get_product tool
3. If the question is about searching products by name/brand/category → use search_products tool
4. If the question is general or a follow-up → answer directly from your knowledge and chat history, do NOT use tools
5. If a tool returns an error → stop immediately and inform the customer politely
 
STRICT RULES:
- Never fabricate order or product data
- For general or follow-up questions, use your knowledge and chat history freely
- Always reply in a warm, friendly tone
- Keep answers concise and helpful"""
 
    max_iterations = 5
    iteration = 0
 
    while iteration < max_iterations:
        iteration += 1
 
        try:
            response = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                max_tokens=1024,
                messages=[{"role": "system", "content": system}] + messages,
                tools=TOOL_SCHEMAS,
                tool_choice="auto"
            )
        except Exception as e:
            print(f"API Error: {e}")
            # Retry without tools on error
            response = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                max_tokens=1024,
                messages=[{"role": "system", "content": system}] + messages,
            )
            return {
                "answer": response.choices[0].message.content,
                "tool_log": tool_log
            }
 
        message = response.choices[0].message
        finish_reason = response.choices[0].finish_reason
        print(f"finish_reason: {finish_reason}")
 
        if finish_reason == "stop":
            return {
                "answer": message.content,
                "tool_log": tool_log
            }
 
        if finish_reason == "tool_calls":
            messages.append({
                "role": "assistant",
                "content": message.content,
                "tool_calls": message.tool_calls
            })
 
            for tool_call in message.tool_calls:
                tool_name  = tool_call.function.name
                tool_input = json.loads(tool_call.function.arguments)
 
                print(f"  Tool call: {tool_name}({tool_input})")
                result = call_tool(tool_name, tool_input)
                print(f"  Result: {result}")
 
                tool_log.append({
                    "tool": tool_name,
                    "input": tool_input,
                    "result": result,
                    "success": "error" not in result
                })
 
                if "error" in result:
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": json.dumps(result)
                    })
                    messages.append({
                        "role": "user",
                        "content": "The tool returned an error. Do not call any more tools. Inform the customer politely."
                    })
                    break
 
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                })
 
    return {
        "answer": "I'm sorry, I was unable to process your request. Please contact our support team.",
        "tool_log": tool_log
    }
 

 