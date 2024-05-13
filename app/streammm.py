import streamlit as st
import pandas as pd
import pickle
import requests

# URL of the CSV file
url = 'https://github.com/TejaswiniKav/UMBC-DATA606-Capstone/blob/main/data/telecom_customer_churn.csv'

# Fetch the raw CSV content
response = requests.get(url)
if response.status_code == 200:
    # Read the content as text and split it into lines
    lines = response.text.split('\n')
    # Process the lines to create a DataFrame
    data = pd.DataFrame([line.split(',') for line in lines], columns=None)
else:
    print(f"Error fetching CSV file: {response.status_code} - {response.reason}")

# Display the first few rows of the DataFrame
print(data.head())

import builtins

def my_hash_func(obj):
    if isinstance(obj, builtins.function):
        return None  # Return None to indicate that the object should not be hashed
    else:
        return obj

def my_hash_func(obj):
    raise ValueError("This should not be called!")

# Load the trained model from a local pickle file
@st.cache(allow_output_mutation=True)
def load_model():
    with open('ML.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# App title
st.title('Telecom Customer Churn Prediction')

# # Load model
# model = load_model()

# Save the model
filename = 'ML.pkl'
pickle.dump(load_model, open(filename, 'wb'))

# Load the model
load_model = pickle.load(open(filename, 'rb'))

# User Inputs
tenure = st.number_input('Tenure (months)', min_value=0, value=30)
monthly_charges = st.number_input('Monthly Charges', min_value=0.0, value=70.0)
total_charges = st.number_input('Total Charges', min_value=0.0, value=200.0)
contract = st.selectbox('Contract Type', ['Month-to-month', 'One year', 'Two year'])

# Prediction
if st.button('Predict'):
    input_data = pd.DataFrame([[tenure, monthly_charges, total_charges, contract]], columns=['tenure', 'MonthlyCharges', 'TotalCharges', 'Contract'])
    prediction = load_model.predict(input_data)
    result = 'Churn' if prediction[0] == 1 else 'No Churn'
    st.success(f'The prediction result is: {result}')

# # streamlit run stream_py.py
# import subprocess

# subprocess.run(["streamlit", "run", "stream_py.py"])

import subprocess

command = ['streamlit', 'run', 'stream_py.py', '--server.port', '8501']
subprocess.run(command)
try:
    
    completed_process = subprocess.run(command, timeout=300)
    # Check if the subprocess completed successfully
    if completed_process.returncode == 0:
        print("Streamlit app ran successfully.")
    else:
        print("Streamlit app exited with an error.")
except subprocess.TimeoutExpired:
    print("Streamlit app timed out and was forcefully terminated.")
except Exception as e:
    print(f"Error running Streamlit app: {e}")


