from flask import Flask,render_template,request
import joblib
import numpy as np
app = Flask(__name__)
model = joblib.load('IPL_Score_Predictor.pkl')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    temp_array = list()

    if request.method == 'POST':

        #Venue
        venue = request.form['venue']
        if venue == 'Barabati Stadium':
            temp_array = temp_array + [1]*1 + [0]*30
        elif venue == 'Brabourne Stadium':
            temp_array = temp_array + [0]*1 + [1]*1 +[0]*29
        elif venue == 'Buffalo Park':
            temp_array = temp_array + [0]*2 + [1]*1 +[0]*28
        elif venue == 'De Beers Diamond Oval':
            temp_array = temp_array + [0]*3 + [1]*1 +[0]*27
        elif venue == 'Dr DY Patil Sports Academy':
            temp_array = temp_array + [0]*4 + [1]*1 +[0]*26
        elif venue == 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium':
            temp_array = temp_array + [0]*5 + [1]*1 +[0]*25
        elif venue == 'Dubai International Cricket Stadium':
            temp_array = temp_array + [0]*6 + [1]*1 +[0]*24
        elif venue == 'Eden Gardens':
            temp_array = temp_array + [0]*7 + [1]*1 +[0]*23
        elif venue == 'Feroz Shah Kotla':
            temp_array = temp_array + [0]*8 + [1]*1 +[0]*22
        elif venue == 'Himachal Pradesh Cricket Association Stadium':
            temp_array = temp_array + [0]*9 + [1]*1 +[0]*21
        elif venue == 'Holkar Cricket Stadium':
            temp_array = temp_array + [0]*10 + [1]*1 +[0]*20
        elif venue == 'JSCA International Stadium Complex':
            temp_array = temp_array + [0]*11 + [1]*1 +[0]*19
        elif venue == 'Kingsmead':
            temp_array = temp_array + [0]*12 + [1]*1 +[0]*18
        elif venue == 'M Chinnaswamy Stadium':
            temp_array = temp_array + [0]*13 + [1]*1 +[0]*17
        elif venue == 'MA Chidambaram Stadium, Chepauk':
            temp_array = temp_array + [0]*14 + [1]*1 +[0]*16
        elif venue == 'Maharashtra Cricket Association Stadium':
            temp_array = temp_array + [0]*15 + [1]*1 +[0]*15
        elif venue == 'New Wanderers Stadium':
            temp_array = temp_array + [0]*16 + [1]*1 +[0]*14
        elif venue == 'Newlands':
            temp_array = temp_array + [0]*17 + [1]*1 +[0]*13
        elif venue == 'OUTsurance Oval':
            temp_array = temp_array + [0]*18 + [1]*1 +[0]*12
        elif venue == 'Punjab Cricket Association IS Bindra Stadium, Mohali':
            temp_array = temp_array + [0]*19 + [1]*1 +[0]*11
        elif venue == 'Punjab Cricket Association Stadium, Mohali':
            temp_array = temp_array + [0]*20 + [1]*1 +[0]*10
        elif venue == 'Rajiv Gandhi International Stadium, Uppal':
            temp_array = temp_array + [0]*21 + [1]*1 +[0]*9
        elif venue == 'Sardar Patel Stadium, Motera':
            temp_array = temp_array + [0]*22 + [1]*1 +[0]*8
        elif venue == 'Sawai Mansingh Stadium':
            temp_array = temp_array + [0]*23 + [1]*1 +[0]*7
        elif venue == 'Shaheed Veer Narayan Singh International Stadium':
            temp_array = temp_array + [0]*24 + [1]*1 +[0]*6
        elif venue == 'Sharjah Cricket Stadium':
            temp_array = temp_array + [0]*25 + [1]*1 +[0]*5
        elif venue == 'Sheikh Zayed Stadium':
            temp_array = temp_array + [0]*26 + [1]*1 +[0]*4
        elif venue == 'St George\'s Park':
            temp_array = temp_array + [0]*27 + [1]*1 +[0]*3
        elif venue == 'Subrata Roy Sahara Stadium':
            temp_array = temp_array + [0]*28 + [1]*1 +[0]*2
        elif venue == 'SuperSport Park':
            temp_array = temp_array + [0]*29 + [1]*1 +[0]*1
        elif venue == 'Wankhede Stadium':
            temp_array = temp_array + [0]*30 + [1]*1

        #Batting team
        batting_team = request.form['batting_team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1]*1 + [0]*7
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array + [0]*1 + [1]*1 +[0]*6
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0]*2 + [1]*1 +[0]*5
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0]*3 + [1]*1 +[0]*4
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0]*4 + [1]*1 +[0]*3
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0]*5 + [1]*1 +[0]*2
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0]*6 + [1]*1 +[0]*1
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0]*7 + [1]*1

        bowling_team = request.form['bowling_team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1]*1 + [0]*7
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [0]*1 + [1]*1 + [0]*6
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0]*2 + [1]*1 + [0]*5
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0]*3 + [1]*1 + [0]*4
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0]*4 + [1]*1 + [0]*3
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0]*5 + [1]*1 + [0]*2
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0]*6 + [1]*1 + [0]*1
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0]*7 + [1]*1

        #Current over
        c_overs = float(request.form['c_over'])

        #Current run
        c_runs = int(request.form['c_run'])

        #Current wicket
        c_wickets = int(request.form['c_wicket'])

        #Last 5 over runs
        l_runs = int(request.form['l_run'])

        #Last 5 over wickets
        l_wickets = int(request.form['l_wicket'])

        temp_array = temp_array + [c_runs,c_wickets,c_overs,l_runs,l_wickets]
        pred_array = np.array([temp_array])
        prediction = int(model.predict(pred_array)[0])

        lower = prediction - 10
        uper = prediction + 10

    return render_template('result.html',lower_limit=lower,upper_limit=uper,batting_team=batting_team,bowling_team=bowling_team)



if __name__ == '__main__':
    app.run(debug=True)