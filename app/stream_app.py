import streamlit as st #importing the necessary modules
import pandas as pd
import pickle
import requests
import builtins

#URL of the dataset
dataset_url = 'https://github.com/TejaswiniKav/UMBC-DATA606-Capstone/blob/main/data/telecom_customer_churn.csv'
response = requests.get(dataset_url)
if response.status_code == 200:
    lines = response.text.split('\n')
    data_frame = pd.DataFrame([line.split(',') for line in lines], columns=None)
else:
    print(f"Error fetching CSV file: {response.status_code} - {response.reason}")

print(data_frame.head()) #printing the dataframe head

def my_hash_function(obj):    #defining the hash function
    if isinstance(obj, builtins.function):
        return None 
    else:
        raise ValueError("This shouldn't be called!")

@st.cache(allow_output_mutation=True)
def load_model():    #loading the model using pickle
    with open('C:/Users/tejas/Downloads/Bestmmodel.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

st.title('Telecom Customer Churn Prediction') #title of the project

project_model = load_model() #loading the model

file_name = 'Bestmmodel.pkl'
pickle.dump(load_model, open(file_name, 'wb'))  #saving the model

load_model = pickle.load(open(file_name, 'rb')) #loading the model

tenure = st.number_input('Tenure (months)', min_value=0, value=25)
monthly_charges = st.number_input('Monthly Charges', min_value=0.0, value=70.0)
total_charges = st.number_input('Total Charges', min_value=0.0, value=300.0)
contract = st.selectbox('Contract Type', ['Month-to-month', 'One year', 'Two year'])

if st.button('Predict'):
    data_input = pd.DataFrame([[tenure, monthly_charges, total_charges, contract]], columns=['tenure', 'MonthlyCharges', 'TotalCharges', 'Contract'])
    model_prediction = load_model.predict(data_input)
    final_result = 'Churned' if model_prediction[0] == 1 else 'Not Churned'
    st.success(f'The final_prediction result of the model is: {final_result}') #result


