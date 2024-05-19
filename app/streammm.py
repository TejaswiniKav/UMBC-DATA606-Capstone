import streamlit as st
import pandas as pd
import requests
import io
import pickle
url = 'https://raw.githubusercontent.com/TejaswiniKav/UMBC-DATA606-Capstone/main/data/telecom_customer_churn.csv'

# Fetch the CSV file
response = requests.get(url)

# Conditional logic using list comprehension
data = pd.DataFrame(
    [line.split(',') for line in response.text.split('\n')] if response.status_code == 200 else []
)

# Display an error message if the CSV fetch failed
if response.status_code != 200:
    st.error(f"Error fetching CSV file: {response.status_code} - {response.reason}")

# Display the first few rows of the data
st.write(data.head() if not data.empty else "No data to display")

import builtins

# Lambda function that returns None for functions and raises an exception for other types
my_hash_func = lambda obj: None if isinstance(obj, builtins.function) else (_ for _ in ()).throw(ValueError("This should not be called!"))

# Example usage
try:
    print(my_hash_func(lambda x: x))  # This should print None because the input is a function
    print(my_hash_func(42))           # This should raise a ValueError
except ValueError as e:
    print(e)

@st.cache(allow_output_mutation=True)
def cached_load_model():
    return load_model()

model = cached_load_model()

filename = 'Bestmodel.pkl'
pickle.dump(load_model, open(filename, 'wb'))

load_model = pickle.load(open(filename, 'rb'))

tenure = st.number_input('Tenure (months)', min_value=0, value=30)
monthly_charges = st.number_input('Monthly Charges', min_value=0.0, value=70.0)
total_charges = st.number_input('Total Charges', min_value=0.0, value=200.0)
contract = st.selectbox('Contract Type', ['Month-to-month', 'One year', 'Two year'])

if st.button('Predict'):
    input_data = pd.DataFrame([[tenure, monthly_charges, total_charges, contract]], columns=['tenure', 'MonthlyCharges', 'TotalCharges', 'Contract'])
    prediction = load_model.predict(input_data)
    result = ['No Churn', 'Churn'][prediction[0]]
    st.success(f'The prediction result is: {result}')

import subprocess

command = ['streamlit', 'run', 'stream_py.py', '--server.port', '8501']

try:
    completed_process = subprocess.run(command, timeout=300)
    
    if completed_process.returncode == 0:
        print("Streamlit app ran successfully.")
    else:
        print("Streamlit app exited with an error.")
except subprocess.TimeoutExpired:
    print("Streamlit app timed out and was forcefully terminated.")
except Exception as e:
    print(f"Error running Streamlit app: {e}")
