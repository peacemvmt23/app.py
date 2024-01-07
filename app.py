import streamlit as st
import pandas as pd

# Create an empty DataFrame to store customer data
customer_data = pd.DataFrame(columns=['Name', 'Email', 'Phone', 'Company'])

# Sidebar with options
st.sidebar.title("CRM App")
option = st.sidebar.selectbox("Select an option", ["View Customers", "Add Customer"])

if option == "Add Customer":
    st.header("Add Customer")
    # Get customer information
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    company = st.text_input("Company")

    # Add customer to DataFrame
    if st.button("Add"):
        customer_data = customer_data.append({'Name': name, 'Email': email, 'Phone': phone, 'Company': company},
                                             ignore_index=True)
        st.success("Customer added successfully!")

elif option == "View Customers":
    st.header("View Customers")
    st.table(customer_data)

# Save the DataFrame to a CSV file
customer_data.to_csv("customer_data.csv", index=False)
