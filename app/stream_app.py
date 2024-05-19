import streamlit as st
import pandas as pd
import pickle
import requests


url = 'https://github.com/TejaswiniKav/UMBC-DATA606-Capstone/blob/main/data/telecom_customer_churn.csv'


response = requests.get(url)
if response.status_code == 200:
    
    lines = response.text.split('\n')
   
    data = pd.DataFrame([line.split(',') for line in lines], columns=None)
else:
    print(f"Error fetching CSV file: {response.status_code} - {response.reason}")


print(data.head())

import builtins

def my_hash_func(obj):
    if isinstance(obj, builtins.function):
        return None 
    else:
        return obj

def my_hash_func(obj):
    raise ValueError("This should not be called!")


@st.cache(allow_output_mutation=True)
def load_model():
    with open('Bestmmodel.pkl', 'rb') as file:
        model = pickle.load(file)
    return model


st.title('Telecom Customer Churn Prediction')

# Load model
model = load_model()

filename = 'Bestmmodel.pkl'
pickle.dump(load_model, open(filename, 'wb'))

load_model = pickle.load(open(filename, 'rb'))

tenure = st.number_input('Tenure (months)', min_value=0, value=30)
monthly_charges = st.number_input('Monthly Charges', min_value=0.0, value=70.0)
total_charges = st.number_input('Total Charges', min_value=0.0, value=200.0)
contract = st.selectbox('Contract Type', ['Month-to-month', 'One year', 'Two year'])

if st.button('Predict'):
    input_data = pd.DataFrame([[tenure, monthly_charges, total_charges, contract]], columns=['tenure', 'MonthlyCharges', 'TotalCharges', 'Contract'])
    prediction = load_model.predict(input_data)
    result = 'Churn' if prediction[0] == 1 else 'No Churn'
    st.success(f'The prediction result is: {result}')




import subprocess

command = ['streamlit', 'run', 'stream_py.py', '--server.port', '8501']
subprocess.run(command)
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