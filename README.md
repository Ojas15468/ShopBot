# ShopBot — AI Customer Support Agent

An agentic AI that answers customer questions for an online store using **Groq API** with tool calling.

## 🔴 Live Demo
👉 **[Try it here!](https://ojas15468-shopbot-app-dlc9q0.streamlit.app/)**
---

## Demo

```
Q: Where is my order ORD-1002?
A: Your order ORD-1002 is currently out for delivery and is expected to arrive today by 8 PM at Mumbai, Maharashtra.

Q: Is there a cheaper alternative to the shoes in ORD-1001?
A: The Puma Softride Enzo (P-401) is a cheaper alternative to Nike Air Max 270, priced at ₹3,499 vs ₹8,999.

Q: What is the status of order ORD-9999?
A: I'm sorry, order ORD-9999 was not found in our system. Please check your order ID and try again.
```

---

## Project Structure

```
shopbot/
├── Database.py      # Mock database — users, orders, products
├── tools.py         # 3 tool functions — get_order, search_products, get_product
├── agent.py         # AI agent — run_agent() function
├── app.py           # Streamlit web interface with login
├── test_agent.py    # 37 unit tests
├── requirements.txt # Dependencies
├── .env             # API keys (not uploaded to GitHub)
├── .gitignore       # Ignores .env file
└── README.md
```

---

## Quick Start

**1. Clone the repository**
```bash
git clone https://github.com/Ojas15468/ShopBot
cd ShopBot
```

**2. Install dependencies**
```bash
pip install groq streamlit python-dotenv
```

**3. Set up API key**

Create a `.env` file:
```
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxx
```

Get your free API key at: https://console.groq.com

**4. Run the app**
```bash
python -m streamlit run app.py
```

**5. Run tests**
```bash
python test_agent.py
```

---

## Demo Accounts

| Phone | Name | Orders |
|-------|------|--------|
| 9876543210 | Rahul Sharma | ORD-1001, ORD-1003 |
| 9123456789 | Priya Singh | ORD-1002 |
| 9999900000 | Amit Kumar | ORD-1004, ORD-1005 |

---

## Available Tools

| Tool | Description |
|------|-------------|
| `get_order(order_id)` | Fetch order status, address, ETA |
| `search_products(query, max_price)` | Search catalog by keyword, optional price filter |
| `get_product(product_id)` | Get full product details — price, features, reviews, warranty |

---

## How the Agent Works

```
Customer Question
      ↓
Agent analyzes question
      ↓
Decides which tool(s) to call     ← Tool Selection
      ↓
Executes tool(s) in order         ← Tool Chaining
      ↓
Gets results
      ↓
Generates friendly response       ← Customer-friendly output
```

### Tool Chaining Example

For *"Is there a cheaper alternative to the shoes in ORD-1001?"*:

```
Step 1: get_order("ORD-1001")       → product_id: P-101
Step 2: get_product("P-101")        → Nike Air Max 270, ₹8,999, category: shoes
Step 3: search_products("shoes",    → Puma Softride Enzo ₹3,499 ✅
         max_price=8999)
```

---

## Features

- **Agentic Loop** — Agent keeps calling tools until it has enough data to answer
- **Tool Chaining** — Multiple tools called in sequence automatically
- **Conversation Memory** — Remembers context from previous messages
- **Error Handling** — Gracefully handles invalid orders and empty searches
- **Login System** — Demo user accounts with order history
- **Agent Reasoning Sidebar** — See every tool call the agent made
- **Price Filter** — Finds cheaper alternatives automatically

---

## Test Results

```
37 tests — 0 failed

✅ get_order tests       (10/10)
✅ search_products tests (10/10)
✅ get_product tests     (12/12)
✅ Edge case tests        (5/5)
```

---

## Tech Stack

- **LLM** — Groq API (meta-llama/llama-4-scout-17b-16e-instruct)
- **UI** — Streamlit
- **Language** — Python 3.10+
