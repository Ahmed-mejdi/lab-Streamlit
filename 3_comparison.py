import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Loan Comparison Tool")

st.write("""
### Compare Different Loan Options
Use this tool to compare how different interest rates, loan terms, or down payments affect your mortgage.
""")

# Create columns for side-by-side comparison
col1, col2 = st.columns(2)

with col1:
    st.write("### Option 1")
    home_value1 = st.number_input("Home Value ($)", min_value=0, value=500000, key="hv1")
    deposit1 = st.number_input("Deposit ($)", min_value=0, value=100000, key="dp1")
    interest_rate1 = st.number_input("Interest Rate (%)", min_value=0.0, value=5.5, key="ir1")
    loan_term1 = st.number_input("Loan Term (years)", min_value=1, value=30, key="lt1")

with col2:
    st.write("### Option 2")
    home_value2 = st.number_input("Home Value ($)", min_value=0, value=500000, key="hv2")
    deposit2 = st.number_input("Deposit ($)", min_value=0, value=100000, key="dp2")
    interest_rate2 = st.number_input("Interest Rate (%)", min_value=0.0, value=4.5, key="ir2")
    loan_term2 = st.number_input("Loan Term (years)", min_value=1, value=25, key="lt2")

# Calculate for Option 1
loan_amount1 = home_value1 - deposit1
monthly_interest_rate1 = (interest_rate1 / 100) / 12
number_of_payments1 = loan_term1 * 12
monthly_payment1 = (
    loan_amount1
    * (monthly_interest_rate1 * (1 + monthly_interest_rate1) ** number_of_payments1)
    / ((1 + monthly_interest_rate1) ** number_of_payments1 - 1)
)
total_payments1 = monthly_payment1 * number_of_payments1
total_interest1 = total_payments1 - loan_amount1

# Calculate for Option 2
loan_amount2 = home_value2 - deposit2
monthly_interest_rate2 = (interest_rate2 / 100) / 12
number_of_payments2 = loan_term2 * 12
monthly_payment2 = (
    loan_amount2
    * (monthly_interest_rate2 * (1 + monthly_interest_rate2) ** number_of_payments2)
    / ((1 + monthly_interest_rate2) ** number_of_payments2 - 1)
)
total_payments2 = monthly_payment2 * number_of_payments2
total_interest2 = total_payments2 - loan_amount2

# Show comparison results
st.write("## Comparison Results")

comparison_data = {
    "Metric": ["Loan Amount", "Monthly Payment", "Total Payments", "Total Interest", "Loan Term"],
    "Option 1": [f"${loan_amount1:,.0f}", f"${monthly_payment1:,.2f}", 
                f"${total_payments1:,.0f}", f"${total_interest1:,.0f}", f"{loan_term1} years"],
    "Option 2": [f"${loan_amount2:,.0f}", f"${monthly_payment2:,.2f}", 
                f"${total_payments2:,.0f}", f"${total_interest2:,.0f}", f"{loan_term2} years"],
    "Difference": [f"${loan_amount2-loan_amount1:,.0f}", f"${monthly_payment2-monthly_payment1:,.2f}", 
                  f"${total_payments2-total_payments1:,.0f}", f"${total_interest2-total_interest1:,.0f}", 
                  f"{loan_term2-loan_term1} years"]
}

comparison_df = pd.DataFrame(comparison_data)
st.table(comparison_df)

# Create visual comparison
st.write("### Visual Comparison")

# Create bar chart for monthly payments
chart_data = pd.DataFrame({
    'Option': ['Option 1', 'Option 2'],
    'Monthly Payment': [monthly_payment1, monthly_payment2],
    'Total Interest': [total_interest1, total_interest2]
})

# Monthly payment comparison
st.write("#### Monthly Payment Comparison")
st.bar_chart(chart_data.set_index('Option')['Monthly Payment'])

# Total interest comparison
st.write("#### Total Interest Comparison")
st.bar_chart(chart_data.set_index('Option')['Total Interest'])

st.write("""
### Which Option is Better?
Consider your financial situation:
- Lower monthly payments make the budget more manageable
- Shorter loan terms mean less total interest paid
- Lower interest rates save money over the life of the loan
""")