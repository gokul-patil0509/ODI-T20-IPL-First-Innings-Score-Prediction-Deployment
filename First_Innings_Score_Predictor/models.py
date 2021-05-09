from django.db import models
import pandas as pd
import pickle


# !!!----- Train Model For ODI -----!!!

### Loading the dataset for ODI
df = pd.read_csv('odi.csv')

# --- Data Cleaning ---
# Removing unwanted columns
columns_to_remove = ['mid','batsman', 'bowler', 'striker', 'non-striker']
df.drop(labels=columns_to_remove, axis=1, inplace=True)

# Keeping only consistent teams
consistent_teams = ['India', 'England', 'Pakistan', 'Sri Lanka', 'Australia', 'South Africa',
                     'New Zealand', 'Bangladesh', 'West Indies', 'Zimbabwe',]

df = df[(df['bat_team'].isin(consistent_teams)) & (df['bowl_team'].isin(consistent_teams))]

# Removing the first 10 overs data in every match
df = df[df['overs']>=10.0]

# Converting the column 'date' from string into datetime object
from datetime import datetime
df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))

# --- Data Preprocessing ---
# Converting categorical features using OneHotEncoding method
encoded_df = pd.get_dummies(data=df, columns=['bat_team', 'bowl_team', 'venue'])

# Rearranging the columns
encoded_df = encoded_df[['date', 'bat_team_Australia', 'bat_team_Bangladesh',  'bat_team_England', 'bat_team_India', 'bat_team_New Zealand',
                         'bat_team_Pakistan', 'bat_team_South Africa', 'bat_team_Sri Lanka',  'bat_team_West Indies', 'bat_team_Zimbabwe', 
                         'bowl_team_Australia','bowl_team_Bangladesh', 'bowl_team_England', 'bowl_team_India', 'bowl_team_New Zealand',
                         'bowl_team_Pakistan', 'bowl_team_South Africa', 'bowl_team_Sri Lanka', 'bowl_team_West Indies', 'bowl_team_Zimbabwe',
                         'venue_M Chinnaswamy Stadium, Bangalore',  'venue_Punjab Cricket Association Stadium, Mohali',  'venue_Feroz Shah Kotla Stadium, Delhi',
                         'venue_Wankhede Stadium, Mumbai', 'venue_Eden Gardens Stadium, Kolkata', 'venue_Sawai Mansingh Stadium, Rajasthan',
                         'venue_Rajiv Gandhi International Stadium, Hyderabad',  'venue_M.A. Chidambaram Stadium, Chennai',  'venue_H. P. C. A. Stadium, Dharamshala',
                         'venue_Maharashtra Cricket Association Stadium, Pune', 'venue_Vidarbha Cricket Association Stadium, Nagpur',  'venue_Sardar Patel Stadium, Ahmedabad',         
                         'overs', 'runs', 'wickets', 'runs_last_10', 'wickets_last_10', 'total']]


# Splitting the data into train and test set
X_train = encoded_df.drop(labels='total', axis=1)[encoded_df['date'].dt.year <= 2006]
X_test = encoded_df.drop(labels='total', axis=1)[encoded_df['date'].dt.year >= 2007]

y_train = encoded_df[encoded_df['date'].dt.year <= 2006]['total'].values
y_test = encoded_df[encoded_df['date'].dt.year >= 2007]['total'].values

# Removing the 'date' column
X_train.drop(labels='date', axis=True, inplace=True)
X_test.drop(labels='date', axis=True, inplace=True)

# --- Model Building ---
# Linear Regression Model
from sklearn.linear_model import LinearRegression
odi_regressor = LinearRegression()
odi_regressor.fit(X_train,y_train)

# Creating a pickle file for the classifier
filename = 'first-odi-innings-score-lr-model.pkl'
pickle.dump(odi_regressor, open(filename, 'wb'))



# !!!----- Train Model For T20 -----!!!

### Loading the dataset
df = pd.read_csv('T20.csv')

# --- Data Cleaning ---
# Removing unwanted columns
columns_to_remove = ['mid','batsman', 'bowler', 'striker', 'non-striker']
df.drop(labels=columns_to_remove, axis=1, inplace=True)

# Keeping only consistent teams
consistent_teams = ['England', 'Australia', 'South Africa', 'Sri Lanka', 'West Indies',
                    'Kenya', 'Pakistan', 'India', 'New Zealand', 'Bangladesh', 'Zimbabwe', 'Ireland']

df = df[(df['bat_team'].isin(consistent_teams)) & (df['bowl_team'].isin(consistent_teams))]

# Removing the first 5 overs data in every match
df = df[df['overs']>=5.0]

# Converting the column 'date' from string into datetime object
from datetime import datetime
df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))

# --- Data Preprocessing ---
# Converting categorical features using OneHotEncoding method
encoded_df = pd.get_dummies(data=df, columns=['bat_team', 'bowl_team', 'venue'])

encoded_df = encoded_df[['date', 'bat_team_Australia', 'bat_team_Bangladesh', 'bat_team_England', 'bat_team_India', 'bat_team_Ireland',  'bat_team_Kenya',
                         'bat_team_New Zealand', 'bat_team_Pakistan', 'bat_team_South Africa', 'bat_team_Sri Lanka', 'bat_team_West Indies', 'bat_team_Zimbabwe', 
                         'bowl_team_Australia', 'bowl_team_Bangladesh', 'bowl_team_England', 'bowl_team_India', 'bowl_team_Ireland', 'bowl_team_Kenya',
                         'bowl_team_New Zealand', 'bowl_team_Pakistan',  'bowl_team_South Africa', 'bowl_team_Sri Lanka',  'bowl_team_West Indies', 'bowl_team_Zimbabwe',
                         'venue_Eden Gardens Stadium, Kolkata', 'venue_Feroz Shah Kotla Stadium, Delhi', 'venue_Himachal Pradesh Cricket Association Stadium, Dharamshala',
                         'venue_M Chinnaswamy Stadium, Bangalore', 'venue_M.A. Chidambaram Stadium, Chennai', 'venue_Maharashtra Cricket Association Stadium, Pune',
                         'venue_Punjab Cricket Association Stadium, Mohali',  'venue_Rajiv Gandhi International Stadium, Hyderabad',  'venue_Sardar Patel Stadium, Ahmedabad', 
                         'venue_Sawai Mansingh Stadium, Rajasthan', 'venue_Vidarbha Cricket Association Stadium, Nagpur', 'venue_Wankhede Stadium, Mumbai',
                         'venue_Melbourne Cricket Ground, Melbourne',  'venue_Shere Bangla National Stadium, Dhaka',  'venue_R. Premadasa Stadium, Colombo',
                         'overs', 'runs', 'wickets', 'runs_last_5', 'wickets_last_5', 'total']]

# Splitting the data into train and test set
X_train = encoded_df.drop(labels='total', axis=1)[encoded_df['date'].dt.year <= 2008]
X_test = encoded_df.drop(labels='total', axis=1)[encoded_df['date'].dt.year >= 2009]

y_train = encoded_df[encoded_df['date'].dt.year <= 2008]['total'].values
y_test = encoded_df[encoded_df['date'].dt.year >= 2009]['total'].values

# Removing the 'date' column
X_train.drop(labels='date', axis=True, inplace=True)
X_test.drop(labels='date', axis=True, inplace=True)

# --- Model Building ---
# Linear Regression Model
from sklearn.linear_model import LinearRegression
t20_regressor = LinearRegression()
t20_regressor.fit(X_train,y_train)

# Creating a pickle file for the classifier
filename = 'first-t20-innings-score-lr-model.pkl'
pickle.dump(t20_regressor, open(filename, 'wb'))





# !!!----- Train Model For IPL -----!!!

# Loading the dataset for IPL
df = pd.read_csv('ipl.csv')

# --- Data Cleaning ---
# Removing unwanted columns
columns_to_remove = ['mid','batsman', 'bowler', 'striker', 'non-striker']
df.drop(labels=columns_to_remove, axis=1, inplace=True)

# Keeping only consistent teams
consistent_teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
                    'Mumbai Indians', 'Kings XI Punjab', 'Royal Challengers Bangalore',
                    'Delhi Daredevils', 'Sunrisers Hyderabad']
df = df[(df['bat_team'].isin(consistent_teams)) & (df['bowl_team'].isin(consistent_teams))]

# Removing the first 5 overs data in every match
df = df[df['overs']>=5.0]

# Converting the column 'date' from string into datetime object
from datetime import datetime
df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))

# --- Data Preprocessing ---
# Converting categorical features using OneHotEncoding method
encoded_df = pd.get_dummies(data=df, columns=['bat_team', 'bowl_team', 'venue'])

# Rearranging the columns
encoded_df = encoded_df[['date', 'bat_team_Chennai Super Kings', 'bat_team_Delhi Daredevils', 'bat_team_Kings XI Punjab',
                         'bat_team_Kolkata Knight Riders', 'bat_team_Mumbai Indians', 'bat_team_Rajasthan Royals',
                         'bat_team_Royal Challengers Bangalore', 'bat_team_Sunrisers Hyderabad',
                         'bowl_team_Chennai Super Kings', 'bowl_team_Delhi Daredevils', 'bowl_team_Kings XI Punjab',
                         'bowl_team_Kolkata Knight Riders', 'bowl_team_Mumbai Indians', 'bowl_team_Rajasthan Royals',
                         'bowl_team_Royal Challengers Bangalore', 'bowl_team_Sunrisers Hyderabad',
                         'venue_M Chinnaswamy Stadium, Bangalore', 'venue_Punjab Cricket Association Stadium, Mohali', 'venue_Feroz Shah Kotla Stadium, Delhi', 
                         'venue_Wankhede Stadium, Mumbai', 'venue_Eden Gardens Stadium, Kolkata', 'venue_Sawai Mansingh Stadium, Rajasthan', 'venue_Rajiv Gandhi International Stadium, Hyderabad',
                         'venue_M.A. Chidambaram Stadium, Chennai', 'venue_Himachal Pradesh Cricket Association Stadium, Dharamshala', 'venue_Maharashtra Cricket Association Stadium, Pune',
                         'venue_Sardar Patel Stadium, Motera', 'venue_Dubai International Cricket Stadium', 'venue_Sharjah Cricket Stadium',          
                         'overs', 'runs', 'wickets', 'runs_last_5', 'wickets_last_5', 'total']]

# Splitting the data into train and test set
X_train = encoded_df.drop(labels='total', axis=1)[encoded_df['date'].dt.year <= 2016]
X_test = encoded_df.drop(labels='total', axis=1)[encoded_df['date'].dt.year >= 2017]

y_train = encoded_df[encoded_df['date'].dt.year <= 2016]['total'].values
y_test = encoded_df[encoded_df['date'].dt.year >= 2017]['total'].values

# Removing the 'date' column
X_train.drop(labels='date', axis=True, inplace=True)
X_test.drop(labels='date', axis=True, inplace=True)

# --- Model Building ---
# Linear Regression Model
from sklearn.linear_model import LinearRegression
ipl_regressor = LinearRegression()
ipl_regressor.fit(X_train,y_train)

# Creating a pickle file for the classifier
filename = 'first-ipl-innings-score-lr-model.pkl'
pickle.dump(ipl_regressor, open(filename, 'wb'))
