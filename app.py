import streamlit as st
from agent import run_agent
from Database import USERS, ORDERS, PRODUCTS
 
st.set_page_config(
    page_title="ShopBot",
    page_icon="🛍️",
    layout="wide"
)
 
# ── Session state initialize ──────────────────────
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "all_tool_logs" not in st.session_state:
    st.session_state.all_tool_logs = []
 
# ════════════════════════════════════════════════
# LOGIN SCREEN
# ════════════════════════════════════════════════
if not st.session_state.logged_in:
 
    # Center the login form
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.title("🛍️ ShopBot")
        st.caption("AI-powered Customer Support")
        st.markdown("---")
 
        st.subheader("Login to your account")
 
        phone = st.text_input(
            "📱 Phone Number",
            placeholder="Enter your phone number"
        )
 
        if st.button("Login →", use_container_width=True):
            if phone in USERS:
                user = USERS[phone]
                st.session_state.logged_in = True
                st.session_state.user = user
                st.session_state.messages = [
                    {
                        "role": "assistant",
                        "content": f"Hi {user['name']}! 👋 Welcome back to ShopBot. You have {len(user['orders'])} order(s). How can I help you today?"
                    }
                ]
                st.rerun()
            else:
                st.error("Phone number not found. Please try a demo account below.")
 
        # Demo accounts
        st.markdown("---")
        st.caption("🧪 Demo Accounts — click to fill:")
 
        demo_users = [
            {"phone": "9876543210", "name": "Rahul Sharma"},
            {"phone": "9123456789", "name": "Priya Singh"},
            {"phone": "9999900000", "name": "Amit Kumar"},
        ]

        for demo in demo_users:
            if st.button(
                f"📱 {demo['phone']} — {demo['name']}",  # ← orders hata diye
                use_container_width=True
            ):
                user = USERS[demo["phone"]]
                st.session_state.logged_in = True
                st.session_state.user = user
                st.session_state.messages = [
                    {
                        "role": "assistant",
                        "content": f"Hi {user['name']}! 👋 Welcome back to ShopBot. You have {len(user['orders'])} order(s). How can I help you today?"
                    }
                ]
                st.rerun()
 
# ════════════════════════════════════════════════
# MAIN CHAT SCREEN
# ════════════════════════════════════════════════
else:
    user = st.session_state.user
 
    # ── Sidebar ───────────────────────────────────
    with st.sidebar:
 
        # User info
        st.markdown(f"### 👤 {user['name']}")
        st.caption(f"📱 {user['phone']}")
        st.caption(f"📧 {user['email']}")
        st.markdown("---")
 
        # User's orders
        st.markdown("### 📦 Your Orders")
        for order_id in user["orders"]:
            order = ORDERS.get(order_id)
            if order:
                product = PRODUCTS.get(order["product_id"], {})
                status_emoji = {
                    "Delivered": "✅",
                    "Out for Delivery": "🚚",
                    "Shipped": "📦",
                    "Processing": "⏳"
                }.get(order["status"], "📋")
 
                with st.expander(f"{status_emoji} {order_id}"):
                    st.write(f"**Product:** {product.get('name', 'N/A')}")
                    st.write(f"**Status:** {order['status']}")
                    st.write(f"**Date:** {order['date']}")
                    if "eta" in order:
                        st.write(f"**ETA:** {order['eta']}")
 
        st.markdown("---")
 
        # Agent reasoning
        st.markdown("### 🔧 Agent Reasoning")
        tool_display = st.empty()
 
        st.markdown("---")
 
        # Logout button
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.session_state.messages = []
            st.session_state.all_tool_logs = []
            st.rerun()
 
    # ── Main chat ─────────────────────────────────
    st.title("🛍️ ShopBot — Customer Support")
    st.caption(f"Logged in as {user['name']}")
 
    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
 
    # User input
    user_input = st.chat_input("Ask about your order, a product, or anything...")
 
    if user_input:
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })
        with st.chat_message("user"):
            st.write(user_input)
 
        # Build history
        history = [
            {"role": msg["role"], "content": msg["content"]}
            for msg in st.session_state.messages[:-1]
            if msg["role"] in ["user", "assistant"] and msg["content"]
        ]
 
        # Add user context to question
        order_ids = ", ".join(user["orders"])
        question_with_context = f"[Customer: {user['name']}, Orders: {order_ids}]\n{user_input}"
 
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = run_agent(question_with_context, history)
 
            answer   = response["answer"]
            tool_log = response["tool_log"]
 
            st.write(answer)
 
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })
 
        if tool_log:
            st.session_state.all_tool_logs.extend(tool_log)
        else:
            st.session_state.all_tool_logs.append({
                "tool": "none",
                "input": {"question": user_input},
                "result": {"source": "General knowledge"},
                "success": True
            })
 
    # Tool logs in sidebar
    with tool_display.container():
        if st.session_state.all_tool_logs:
            for i, log in enumerate(st.session_state.all_tool_logs):
                status = "✅" if log["success"] else "❌"
                if log["tool"] == "none":
                    st.info(f"💬 Step {i+1}: General knowledge")
                else:
                    with st.expander(f"{status} Step {i+1}: {log['tool']}"):
                        st.write("**Input:**")
                        st.json(log["input"])
                        st.write("**Result:**")
                        st.json(log["result"])
        else:
            st.info("Ask a question to see agent reasoning.")
 
