import streamlit as st
import pandas as pd
import math
import matplotlib.pyplot as plt

st.title("Detailed Payment Schedule")

# Sidebar for inputs
st.sidebar.header("Loan Parameters")
home_value = st.sidebar.number_input("Home Value", min_value=0, value=500000)
deposit = st.sidebar.number_input("Deposit", min_value=0, value=100000)
interest_rate = st.sidebar.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
loan_term = st.sidebar.number_input("Loan Term (in years)", min_value=1, value=30)

# Calculate loan details
loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12

monthly_payment = (
    loan_amount
    * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
    / ((1 + monthly_interest_rate) ** number_of_payments - 1)
)

# Create payment schedule
schedule = []
remaining_balance = loan_amount

for i in range(1, number_of_payments + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12)
    month_name = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                 "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][(i-1) % 12]
    
    schedule.append(
        [
            i,
            f"Year {year}, {month_name}",
            monthly_payment,
            principal_payment,
            interest_payment,
            remaining_balance,
            year,
        ]
    )

df = pd.DataFrame(
    schedule,
    columns=["Payment #", "Period", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
)

# Format monetary columns
for col in ["Payment", "Principal", "Interest", "Remaining Balance"]:
    df[col] = df[col].map("${:,.2f}".format)

# Display filters
st.write("### Filter the Schedule")
year_filter = st.selectbox("Select Year", options=[0] + sorted(df["Year"].unique().tolist()), 
                          format_func=lambda x: "All Years" if x == 0 else f"Year {x}")

if year_filter == 0:
    filtered_df = df
else:
    filtered_df = df[df["Year"] == year_filter]

# Display data
st.write(f"### Payment Schedule {'' if year_filter == 0 else f'- Year {year_filter}'}")
st.dataframe(filtered_df)

# Add download button
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv().encode('utf-8')

csv = convert_df_to_csv(filtered_df)
st.download_button(
    "Download Payment Schedule",
    csv,
    "payment_schedule.csv",
    "text/csv",
    key='download-csv'
)