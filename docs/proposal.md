## Telecom Customer Churn Prediction
 
## 1. Title and Author

#DATA 606 Capstone in Data Science


#Professor: Dr. Chaojie (Jay) Wang


#Title of the project: Telecom Customer Churn Prediction


#Author: Tejaswini Kavuri(CM12215)


#Github profile link: https://github.com/TejaswiniKav/UMBC-DATA606-Capstone


#PowerPoint presentation file:


#YouTube video:

## 2. Background 
 
## Topic Overview:
The project I have chosen is the Telecom Customer Churn Prediction. In the telecom companies, reliability of the customers plays a vital role in-order to maintain revenue to the companies which is the ultimate benefit for every organization. The interest and main goal of the project is to predict the churn rate of the customer for the telecom company. The Churn rate is that the rate at which the customers discontinue the telecom service. By developing a ML predictive model, it will identify the customer's churn rate based on the previous historial data and so that the company will implement the strategies in-order to minimize the churn.

## Importance in choosing the topic:
The Churn issue is very important for any company especially for telecom companies mainly in-terms of the business perspective. Few of the reasons that will impact the organization during Churn are:
The reduction in the revenue costs, it will become expensive for the companies to invest in acquiring the new customers and to maintain stability in the no. of customers using the telecom service.
Ensuring trust is the most crucial aspect and the trust-worthy business will stay consistent in the long-run with profits. 
In a broader aspect, ultimately the Churn effects the job stability within the organization and could minimize the profits of the organization.
By considering all these factors, I believe it is very important and it matters to minimize the Churn rate in the Telecom companies.

## Research questions:
1. Can we identify these Churn early using by any measures ?
2. How accurate we can predict the churn rate using the machine learning prediction models ?
3. After all the measures, how much percentage we can constantly maintain the revenue of the telecom companies ?

## 3. Data 
## Data sources:
The specific telecom customer churn dataset:
https://www.mavenanalytics.io/blog/maven-churn-challenge
## Kaggle Link:
https://www.kaggle.com/datasets/shilongzhuang/telecom-customer-churn-by-maven-analytics?select=telecom_customer_churn.csv
- Size of the dataset is - 1.40 MB
- Our dataset has 38 columns and 7,043 customer data in total. 
- Each row represent the customer data according to the specific column.
- Attaching the image of the columns that are present in the dataset.
- Link:https://github.com/TejaswiniKav/UMBC-DATA606-Capstone/blob/main/docs/Dataset%20columns.jpg

| Column                             | Dtype   | Definition                                                                                                           |
| ---------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------- |
| Customer ID                        | object  | Represents the unique identifier of each customer                                                                   |
| Gender                             | object  | Indicates customer gender (Male or Female)                                                                          |
| Age                                | int64   | Represents the customer age (in years)                                                                              |
| Married                            | object  | Indicates whether the customer is married or not (Yes or No)                                                        |
| Number of Dependents               | int64   | Represents the number of dependents in the family associated with the customer                                      |
| City                               | object  | Represents the customer city where they are located                                                                 |
| Zip Code                           | int64   | Represents the customer zipcode                                                                                     |
| Latitude                           | float64 | Represents the customer's latitude geographical location                                                            |
| Longitude                          | float64 | Represents the customer's longitude geographical location                                                           |
| Number of Referrals                | int64   | Indicates the number of referrals of the customer                                                                   |
| Tenure in Months                   | int64   | Represents the service duration of the customer associated with the service in months                              |
| Offer                              | object  | Represents the offer type that the customer is subscribed to                                                        |
| Phone Service                      | object  | Indicates whether the customer has the phone service or not (Yes or No)                                              |
| Avg Monthly Long Distance Charges  | float64 | Represents the average monthly long-distance service charges                                                         |
| Multiple Lines                     | object  | Indicates whether the customer is in multiple phone lines (Yes or No)                                                 |
| Internet Service                   | object  | Represents the internet service that the customer is subscribed to                                                    |
| Internet Type                      | object  | Represents the type of the internet service that the customer is subscribed to                                        |
| Avg Monthly GB Download            | float64 | Represents the average monthly usage of the data in Gigabytes                                                         |
| Online Security                    | object  | Indicates whether or not a customer has online security services                                                     |
| Online Backup                      | object  | Indicates whether the customer has online backup services                                                            |
| Device Protection Plan             | object  | Indicates whether the customer has a Device Protection Plan                                                          |
| Premium Tech Support               | object  | Indicates whether the customer has Premium Tech Support                                                              |
| Streaming TV                       | object  | Indicates whether the customer has Streaming TV service                                                              |
| Streaming Movies                   | object  | Indicates whether the customer has Streaming Movies service                                                          |
| Streaming Music                    | object  | Indicates whether the customer has Streaming Music services                                                          |
| Unlimited Data                     | object  | Indicates whether the customer has Unlimited Data services                                                           |
| Contract                           | object  | Represents the type of contract that the customer has (One, two years, month-to-month)                               |
| Paperless Billing                  | object  | Indicates whether a customer has opted for paperless billing                                                         |
| Payment Method                     | object  | Represents the customer's preferred payment method                                                                   |
| Monthly Charge                     | float64 | Represents the monthly charges for the customer according to the subscription                                        |
| Total Charges                      | float64 | Represents the total charges of the customer                                                                         |
| Total Refunds                      | float64 | Represents the total refunds for the customer                                                                        |
| Total Extra Data Charges           | int64   | Represents the total extra data charges for the customer                                                             |
| Total Long Distance Charges        | float64 | Represents the total long-distance charges for the customer                                                          |
| Total Revenue                      | float64 | Represents the total revenue generated from the customer                                                             |
| Customer Status                    | object  | Represents the status of the customer (active or inactive for the service)                                           |
| Churn Category                     | object  | Indicates whether a customer is churned (Yes or No)                                                                  |
| Churn Reason                       | object  | Reason provided for the customer Churn if possible                                                                   |

## Which variable/column will be your target/label in your ML model?
The model that will be targeted in the model is the 'Customer Status' column
## Which variables/columns may be selected as features/predictors for your ML models?
All the columns excluding the 'Customer Status' column can be selected for the features/predictors.


## 4. References 
The specific telecom customer churn dataset:
https://www.mavenanalytics.io/blog/maven-churn-challenge


