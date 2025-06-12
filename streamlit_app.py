import os
import streamlit as st
import requests
import pandas as pd
from datetime import datetime

API_BASE = "http://localhost:8000"

st.set_page_config(
    page_title="Invoice Reimbursement System",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    .header {
        background-color: #1f2937;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    .header h1 {
        color: white;
        margin: 0;
    }
    .header p {
        color: #d1d5db;
        margin: 0;
    }
    .main-content {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    .stButton > button {
        background-color: #69B716;
        color: white;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
    }
    .stButton > button:hover {
        background-color: #45a049;
        transform: translateY(-2px);
    }
    .tips-section {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #4CAF50;
        margin-bottom: 2rem;
    }
    .footer {
        background-color: #1f2937;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-top: 2rem;
    }
    h2, h3, p {
        color: #1f2937 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="header">
        <h1>💰 Invoice Reimbursement System</h1>
        <p>Automated analysis and intelligent querying of expense invoices</p>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## ⚙️ Navigation")
    page = st.radio("", ["1) Invoice Analysis", "2) Chat Assistant", "3) System Health"])
    st.markdown("---")
    st.markdown("#### 🔧 Settings")
    # Add any sidebar settings here if needed

if page.startswith("1"):
    st.markdown("## I) Invoice Analysis")
    st.markdown("<div class='main-content'>", unsafe_allow_html=True)

    policy = st.file_uploader("📄 Upload Policy PDF", type=['pdf'])
    invoices = st.file_uploader("📦 Upload Invoices ZIP", type=['zip'])
    name = st.text_input("👤 Employee Name")

    if st.button("🔍 Analyze"):
        if not (policy and invoices and name):
            st.warning("Please provide policy, invoices, and employee name.")
        else:
            with st.spinner("Analyzing invoices..."):
                files = {"policy_file": policy, "invoices_zip": invoices}
                data = {"employee_name": name}
                r = requests.post(f"{API_BASE}/analyze-invoices", files=files, data=data)
                if r.status_code == 200:
                    res = r.json()
                    st.success(res["message"])
                    for a in res["results"]:
                        with st.expander(f"📋 {a['invoice_filename']}"):
                            col1, col2, col3 = st.columns(3)
                            col1.metric("Status", a["reimbursement_status"])
                            col2.metric("Total Amount", f"₹{a['total_amount']}")
                            col3.metric("Reimbursable", f"₹{a['reimbursable_amount']}")
                            st.markdown("**Reason:**")
                            st.write(a["reason"])
                            if a["detailed_breakdown"]:
                                st.markdown("**Detailed Breakdown:**")
                                st.json(a["detailed_breakdown"])
                else:
                    st.error(r.text)

    st.markdown("</div>", unsafe_allow_html=True)

elif page.startswith("2"):
    st.markdown("## II) Chat Assistant")
    st.markdown("<div class='main-content'>", unsafe_allow_html=True)

    if "history" not in st.session_state:
        st.session_state.history = []

    # display chat history
    for msg in st.session_state.history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask about invoices, employees, or policies..."):
        st.session_state.history.append({"role": "user", "content": prompt})
        r = requests.post(
            f"{API_BASE}/chat",
            json={
                "query": prompt,
                "chat_history": [{"role": m["role"], "content": m["content"]} for m in st.session_state.history[:-1]]
            }
        )
        if r.status_code == 200:
            ans = r.json()["response"]
            st.session_state.history.append({"role": "assistant", "content": ans})
            with st.chat_message("assistant"):
                st.markdown(ans)
        else:
            st.error(r.text)

    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.markdown("## III) System Health")
    st.markdown("<div class='main-content'>", unsafe_allow_html=True)

    if st.button("🔌 Check API Health"):
        r = requests.get(f"{API_BASE}/health")
        if r.status_code == 200:
            st.success("✅ API is healthy")
            st.json(r.json())
        else:
            st.error("❌ API error")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
    <div class="footer">
        Developed by Saurabh Kumar
    </div>
""", unsafe_allow_html=True)
