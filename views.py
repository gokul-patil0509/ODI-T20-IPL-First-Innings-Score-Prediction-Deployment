from django.shortcuts import render
from django.http import HttpResponse
import pickle
import numpy as np


# !!!----- Home Page -----!!!

def home(request):
        return render(request,'cricket_home.html')


# !!!----- ODI APPLICATION -----!!!

# Load the Random Forest CLassifier model
filename = 'first-odi-innings-score-lr-model.pkl'
odi_regressor = pickle.load(open(filename, 'rb'))

# ODI First-Innings-Score-Prediction-Model
def odi_home(request):
        return render(request,'odi_index.html')


def odi_predict(request):   
    temp_array = list()

    if request.method == 'POST':
            
        
        batting_team = request.POST.get('batting-team')
        if batting_team == 'India':
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0]
        elif batting_team == 'England':
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0]
        elif batting_team == 'Pakistan':
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0]
        elif batting_team == 'Sri Lanka':
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0]
        elif batting_team == 'Australia':
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0]
        elif batting_team == 'South Africa':
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0]
        elif batting_team == 'New Zealand':
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0]
        elif batting_team == 'Bangladesh':
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0]
        elif batting_team == 'West Indies':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0]
        elif batting_team == 'Zimbabwe':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1]    
            
            
        bowling_team = request.POST.get('bowling-team')
        if bowling_team == 'India':
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0]
        elif bowling_team == 'England':
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0]
        elif bowling_team == 'Pakistan':
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0]
        elif bowling_team == 'Sri Lanka':
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0]
        elif bowling_team == 'Australia':
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0]
        elif bowling_team == 'South Africa':
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0]
        elif bowling_team == 'New Zealand':
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0]
        elif bowling_team == 'Bangladesh':
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0]
        elif bowling_team == 'West Indies':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0]
        elif bowling_team == 'Zimbabwe':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1]    


        Venue = request.POST.get('Venue')
        if Venue == 'M Chinnaswamy Stadium, Bangalore':
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0,0]
        elif Venue == 'Punjab Cricket Association Stadium, Mohali':
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0,0]
        elif Venue == 'Feroz Shah Kotla Stadium, Delhi':
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0,0]
        elif Venue == 'Wankhede Stadium, Mumbai':
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0,0]
        elif Venue == 'Eden Gardens Stadium, Kolkata':
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0,0]
        elif Venue == 'Maharashtra Cricket Association Stadium, Pune':
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0,0]
        elif Venue == 'Vidarbha Cricket Association Stadium, Nagpur':
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0,0]
        elif Venue == 'Sawai Mansingh Stadium, Rajasthan':
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0,0]
        elif Venue == 'Rajiv Gandhi International Stadium, Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0,0]
        elif Venue == 'M.A. Chidambaram Stadium, Chennai':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1,0,0]
        elif Venue == 'H. P. C. A. Stadium, Dharamshala':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,1,0]
        elif Venue == 'Sardar Patel Stadium, Ahmedabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,1]    
            
            
        overs = float(request.POST.get('overs'))
        runs = int(request.POST.get('runs'))
        wickets = int(request.POST.get('wickets'))
        runs_in_prev_10 = int(request.POST.get('runs_in_prev_10'))
        wickets_in_prev_10 = int(request.POST.get('wickets_in_prev_10'))
        
        temp_array = temp_array +[overs, runs, wickets, runs_in_prev_10, wickets_in_prev_10]
        
        data = np.array([temp_array])
        my_prediction = int(odi_regressor.predict(data)[0])
        context={'lower_limit' : my_prediction-10, 'upper_limit' :  my_prediction+5}      
        return render(request, 'odi_result.html',context )


# !!!----- T20 APPLICATION -----!!!

# Load the Random Forest CLassifier model
filename = 'first-t20-innings-score-lr-model.pkl'
t20_regressor = pickle.load(open(filename, 'rb'))

def t20_home(request):
        return render(request,'t20_index.html')


def t20_predict(request):   
    temp_array = list()

    if request.method == 'POST':
            
        batting_team = request.POST.get('batting-team')
        if batting_team == 'India':
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0,0]
        elif batting_team == 'England':
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0,0]
        elif batting_team == 'Pakistan':
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0,0]
        elif batting_team == 'Sri Lanka':
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0,0]
        elif batting_team == 'Australia':
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0,0]
        elif batting_team == 'South Africa':
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0,0]
        elif batting_team == 'New Zealand':
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0,0]
        elif batting_team == 'Bangladesh':
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0,0]
        elif batting_team == 'West Indies':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0,0]
        elif batting_team == 'Zimbabwe':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1,0,0]
        elif batting_team == 'Kenya':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,1,0]    
        elif batting_team == 'Ireland':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,1]    
                    
            
            
        bowling_team = request.POST.get('bowling-team')
        if bowling_team == 'India':
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0,0]
        elif bowling_team == 'England':
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0,0]
        elif bowling_team == 'Pakistan':
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0,0]
        elif bowling_team == 'Sri Lanka':
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0,0]
        elif bowling_team == 'Australia':
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0,0]
        elif bowling_team == 'South Africa':
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0,0]
        elif bowling_team == 'New Zealand':
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0,0]
        elif bowling_team == 'Bangladesh':
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0,0]
        elif bowling_team == 'West Indies':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0,0]
        elif bowling_team == 'Zimbabwe':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1,0,0]
        elif bowling_team == 'Kenya':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,1,0]
        elif bowling_team == 'Ireland':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,1]     


        Venue = request.POST.get('Venue')
        if Venue == 'M Chinnaswamy Stadium, Bangalore':
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venue == 'Punjab Cricket Association Stadium, Mohali':
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venue == 'Feroz Shah Kotla Stadium, Delhi':
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venue == 'Wankhede Stadium, Mumbai':
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
        elif Venue == 'Eden Gardens Stadium, Kolkata':
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
        elif Venue == 'Maharashtra Cricket Association Stadium, Pune':
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
        elif Venue == 'Vidarbha Cricket Association Stadium, Nagpur':
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
        elif Venue == 'Sawai Mansingh Stadium, Rajasthan':
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
        elif Venue == 'Rajiv Gandhi International Stadium, Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
        elif Venue == 'M.A. Chidambaram Stadium, Chennai':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
        elif Venue == 'Himachal Pradesh Cricket Association Stadium, Dharamshala':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
        elif Venue == 'Sardar Patel Stadium, Ahmedabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
        elif Venue == 'Melbourne Cricket Ground, Melbourne':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
        elif Venue == 'Shere Bangla National Stadium, Dhaka':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
        elif Venue == 'R. Premadasa Stadium, Colombo':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]    
            
            
        overs = float(request.POST.get('overs'))
        runs = int(request.POST.get('runs'))
        wickets = int(request.POST.get('wickets'))
        runs_in_prev_5 = int(request.POST.get('runs_in_prev_5'))
        wickets_in_prev_5 = int(request.POST.get('wickets_in_prev_5'))
        
        temp_array = temp_array +[overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        
        data = np.array([temp_array])
        my_prediction = int(t20_regressor.predict(data)[0])
        context={'lower_limit' : my_prediction-10, 'upper_limit' :  my_prediction+5}      
        return render(request, 't20_result.html',context )


# !!!----- IPL APPLICATION -----!!!

# Load the Random Forest CLassifier model
filename = 'first-ipl-innings-score-lr-model.pkl'
ipl_regressor = pickle.load(open(filename, 'rb'))

# IPL First-Innings-Score-Prediction-Model
def ipl_home(request):
        return render(request,'ipl_index.html')


def ipl_predict(request):   
    temp_array = list()

    if request.method == 'POST':
            
        
        batting_team = request.POST.get('batting-team')
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
            
        bowling_team = request.POST.get('bowling-team')
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]


        Venue = request.POST.get('Venue')
        if Venue == 'M Chinnaswamy Stadium, Bangalore':
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venue == 'Punjab Cricket Association Stadium, Mohali':
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0,0,0]
        elif Venue == 'Feroz Shah Kotla Stadium, Delhi':
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0,0,0]
        elif Venue == 'Wankhede Stadium, Mumbai':
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0,0,0]
        elif Venue == 'Eden Gardens Stadium, Kolkata':
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0,0,0]
        elif Venue == 'Sawai Mansingh Stadium, Rajasthan':
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0,0,0]
        elif Venue == 'Rajiv Gandhi International Stadium, Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0,0,0]
        elif Venue == 'M.A. Chidambaram Stadium, Chennai':
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0,0,0]
        elif Venue == 'Himachal Pradesh Cricket Association Stadium, Dharamshala':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0,0,0]
        elif Venue == 'Maharashtra Cricket Association Stadium, Pune':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1,0,0,0]
        elif Venue == 'Sardar Patel Stadium, Motera':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,1,0,0]
        elif Venue == 'Dubai International Cricket Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,1,0]
        elif Venue == 'Sharjah Cricket Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,1]    
            
            
        overs = float(request.POST.get('overs'))
        runs = int(request.POST.get('runs'))
        wickets = int(request.POST.get('wickets'))
        runs_in_prev_5 = int(request.POST.get('runs_in_prev_5'))
        wickets_in_prev_5 = int(request.POST.get('wickets_in_prev_5'))
        
        temp_array = temp_array +[overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        
        data = np.array([temp_array])
        my_prediction = int(ipl_regressor.predict(data)[0])
        context={'lower_limit' : my_prediction-10, 'upper_limit' :  my_prediction+5}      
        return render(request, 'ipl_result.html',context )

