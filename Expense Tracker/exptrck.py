import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import csv

# Function to write data to CSV file
def write_to_csv(data, filename):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Function to read data from CSV file
def read_from_csv(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return pd.DataFrame(data, columns=["Date", "Category", "Amount"])
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Category", "Amount"])

# Main title
st.title("Expense Tracking System")

# Sidebar for adding expenses
with st.sidebar:
    st.header("Add Expense")
    expense_date = st.date_input("Date of Expense")
    expense_category = st.selectbox("Expense Category", ["Choose Category", "Groceries", "Utilities", "Entertainment", "Other"], index=0)
    expense_amount = st.number_input("Expense Amount")

    if st.button("Add Expense") and expense_category != "Choose Category":
        expense_data = [expense_date, expense_category, expense_amount]
        write_to_csv(expense_data, "expenses.csv")


# Reading from the CSV
expenses_df = read_from_csv("expenses.csv")
expenses_df["Amount"] = pd.to_numeric(expenses_df["Amount"])
expenses_df["Date"] = pd.to_datetime(expenses_df["Date"])
expenses_df["Month"] = expenses_df["Date"].dt.month
expenses_df["Year"] = expenses_df["Date"].dt.year

# Button to show data in tabular format
if st.button("Show Overall Data"):
    st.subheader("Stored Data")
    data = expenses_df 
    if not data.empty:
        st.write(data)
    else:
        st.write("No data available.")


# Choose the Options
analysis_type = st.selectbox("Select Analysis Type", ["None", "Daily", "Monthly", "Yearly"], index=0)
if analysis_type != "None":
    selected_category = st.selectbox("Select Category", ["None", "Groceries", "Utilities", "Entertainment", "Other"], index=0)



# Button to display the total expenditure for each day, month, and year
if st.button("Show Expenditure"):
    st.subheader("Expenditure Analysis")

    if analysis_type != "None":

        if analysis_type == "Daily":

            # Filter by category
            if selected_category != "None":
                category_data = expenses_df[expenses_df["Category"] == selected_category]
                st.write(category_data)
            else:
                daily_expenditure = expenses_df.groupby("Date")["Amount"].sum().reset_index()
                st.write(daily_expenditure)

        elif analysis_type == "Monthly":

            # Filter by category
            if selected_category != "None":
                category_data = expenses_df[expenses_df["Category"] == selected_category]
                monthly_expenditure = category_data.groupby(["Year", "Month"])["Amount"].sum().reset_index()
                st.write(monthly_expenditure)
            else:
                monthly_expenditure= expenses_df.groupby(["Year", "Month"])["Amount"].sum().reset_index()
                st.write(monthly_expenditure)

        else:  # Yearly

            # Filter by category
            if selected_category != "None":
                category_data = expenses_df[expenses_df["Category"] == selected_category]
                yearly_expenditure = category_data.groupby("Year")["Amount"].sum().reset_index()
                st.write(yearly_expenditure)
            else:
                yearly_expenditure = expenses_df.groupby("Year")["Amount"].sum().reset_index()
                st.write(yearly_expenditure)



# Button to display the graph
if st.button("Show Expenses Over Time"):
    # Read data from CSV file into a DataFrame
    expenses_df = read_from_csv("expenses.csv")

    # Convert date column to datetime type
    expenses_df["Date"] = pd.to_datetime(expenses_df["Date"])

    # Group expenses by category and date
    grouped_expenses = expenses_df.groupby(["Category", pd.Grouper(key="Date", freq="D")]).sum().reset_index()

    # Create a bar chart for each category
    fig = go.Figure()
    for category in grouped_expenses["Category"].unique():
        category_data = grouped_expenses[grouped_expenses["Category"] == category]
        fig.add_trace(go.Bar(x=category_data["Date"], y=category_data["Amount"], name=category))

    # Update layout
    fig.update_layout(barmode='stack', title='Expenses Over Time by Category', xaxis_title='Date', yaxis_title='Total Amount')

    # Display the chart
    st.plotly_chart(fig)
