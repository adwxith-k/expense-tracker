import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

# --- Custom Styling ---
st.markdown(
    """
    <style>
        body, .stApp {
            background-color: #254B99;
            color: white;
        }

        h1, h2, h3, h4, h5, h6, p, div, span, label {
            color: white !important;
        }

        .logo-container {
            text-align: center;
            margin-bottom: 20px;
            background-color: transparent;
        }

        button[kind="secondary"] {
            color: white !important;
            background-color: #0d6efd !important;
            border: none;
            border-radius: 6px;
            padding: 8px 16px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Logo ---
try:
    logo = Image.open("logo1.png")
    col1, col2, col3 = st.columns([2, 5, 1])  # You can tweak the ratio for spacing
    with col1:
        st.image(logo, width=150)
except Exception:
    st.warning("⚠️ Logo image not found or failed to load.")


# --- Title ---
st.title("Business Expense & Profit Tracker")

# --- Input Handler ---
def get_input(label):
    value = st.text_input(label)
    try:
        return int(value) if value.strip() != "" else 0
    except ValueError:
        st.warning(f"Please enter a valid number for: {label}")
        return 0

# --- Expense Input Section ---
st.header("Expense Inputs:")
marketing_exp = get_input("1. What is your monthly spending on marketing and advertising?")
salary_exp = get_input("2. What is your monthly expense on staff salaries?")
admin_exp = get_input("3. What are your monthly administrative or office-related expenses (e.g., rent, internet, insurance, supplies)?")
logistic_exp = get_input("4. Do you have any monthly logistics, delivery, or distribution expenses?")
legal_exp = get_input("5. What is your monthly spending on legal, licensing, or compliance-related fees?")
other_exp = get_input("6. Do you have any other monthly business expenses not listed above?")

# --- Income Input Section ---
st.header("Income Inputs:")
main_income = get_input("1. What is your monthly income from core business activities (e.g., product sales, services, subscriptions)?")
other_income = get_input("2. Do you have any monthly income from additional sources (e.g., commissions, rent, investments, etc.)?")

# --- Annual Calculations ---
annual_expenses = {
    "Marketing": marketing_exp * 12,
    "Staff Salaries": salary_exp * 12,
    "Administrative": admin_exp * 12,
    "Logistics": logistic_exp * 12,
    "Legal & Compliance": legal_exp * 12,
    "Other": other_exp * 12
}

total_expenses = sum(annual_expenses.values())
annual_main_income = main_income * 12
annual_other_income = other_income * 12
total_income = annual_main_income + annual_other_income
profit = total_income - total_expenses
profit_margin = (profit / total_income * 100) if total_income > 0 else 0

# --- Output ---
if st.button("🔍 Calculate"):
    st.subheader("Yearly Summary (Based on Monthly Inputs):")
    st.write(f"**Total Annual Expenses:** ₹{total_expenses:,.0f}")
    st.write(f"**Total Annual Income:** ₹{total_income:,.0f}")
    st.write(f"**Annual Profit:** ₹{profit:,.0f}")
    st.write(f"**Profit Margin:** {profit_margin:.2f}%")

    highest_expense = max(annual_expenses, key=annual_expenses.get)
    st.write(f"**Highest Expense Area:** {highest_expense} (₹{annual_expenses[highest_expense]:,.0f})")

    # --- Pie Chart ---
    fig, ax = plt.subplots()
    ax.pie(annual_expenses.values(), labels=annual_expenses.keys(), autopct='%1.1f%%', startangle=140)
    ax.set_title("Annual Expense Breakdown")
    st.pyplot(fig)



    # --- Suggestions ---
    st.subheader("💡 Suggestions")
    if profit < 0:
        st.error("🔴 You're operating at a loss.")
        st.markdown("""
        - Review pricing and cost structures.
        - Cut unnecessary expenses in highest spend areas.
        - Explore new revenue streams.
        """)
    elif profit_margin < 30:
        st.warning("🟠 Low to Moderate Profit Margin (0–29%)")
        st.markdown("""
        - Slightly increase prices if possible.
        - Focus on operational efficiency.
        - Upsell or bundle high-margin services.
        """)
    elif 30 <= profit_margin < 50:
        st.info("🟡 Healthy Profit Margin (30–49%)")
        st.markdown("""
        - You're doing well! Optimize for growth.
        - Explore automation and marketing.
        - Strengthen your value proposition.
        """)
    elif 50 <= profit_margin < 60:
        st.success("🟢 Very Good Profit Margin (50–59%)")
        st.markdown("""
        - Consider scaling sustainably.
        - Invest in quality and customer service.
        """)
    elif 60 <= profit_margin < 80:
        st.success("🟢 Strong Profit Margin (60–79%)")
        st.markdown("""
        - Expand into new markets.
        - Reinvest in your brand and team.
        """)
    elif 80 <= profit_margin <= 100:
        st.success("🟢 Excellent Profit Margin (80–100%)")
        st.markdown("""
        - Consider franchising or partnerships.
        - Build thought leadership.
        - Invest in innovation.
        """)
    else:
        st.warning("⚠️ Profit margin seems outside the normal range. Please verify your inputs.")

