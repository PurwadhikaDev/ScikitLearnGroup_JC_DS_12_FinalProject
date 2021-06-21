import joblib
from flask import Flask, render_template, request
from sqlalchemy import create_engine
import pandas as pd

'''
https://getbootstrap.com
'''

# Opsi 1 - Klasik - Statis
'''
- Dataset 
df.to_html('dataset.html')

- Visualizasi
plt.savefig

- Prediction
Model Import
'''

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/dataset')
# def df():
#     return render_template('dataset.html')

@app.route('/visualize')
def vis():
    return render_template('viz.html')

@app.route('/prediction')
def pred():
    sqlengine = create_engine('mysql+pymysql://root:!bun36Prakoso@127.0.0.1/flaskapp', pool_recycle=3605)
    engine = sqlengine.raw_connection()
    cursor = engine.cursor()
    cursor.execute("SELECT * FROM jam_new")
    data = cursor.fetchall()
    return render_template('pred.html',data=data)

@app.route('/hasil', methods=['POST'])
def result():
    if request.method == 'POST':
    ## Untuk Predict
        input = request.form
        
        season = ''
        if input['season'] == 'Spring':
            season = 2
        elif input['season'] == 'Summer':
            season = 3
        elif input['season'] == 'Fall':
            season = 4
        else:
            season = 1
        
        year = int(input['yr'])

        month = ''
        if input['mnth'] == 'January':
            month = 1
        elif input['mnth'] == 'February':
            month = 2
        elif input['mnth'] == 'March':
            month = 3
        elif input['mnth'] == 'April':
            month = 4
        elif input['mnth'] == 'May':
            month = 5
        elif input['mnth'] == 'June':
            month = 6
        elif input['mnth'] == 'July':
            month = 7
        elif input['mnth'] == 'August':
            month = 8
        elif input['mnth'] == 'September':
            month = 9
        elif input['mnth'] == 'October':
            month = 10
        elif input['mnth'] == 'November':
            month = 11
        else:
            month = 12

        hour = int(input['hr'])

        holiday = ''
        if input['holiday'] == 'Holiday':
            holiday = 1
        else:
            holiday = 0
        
        day = ''
        if input['weekday'] == 'Monday':
            day = 1
        elif input['weekday'] == 'Tuesday':
            day = 2
        elif input['weekday'] == 'Wednesday':
            day = 3
        elif input['weekday'] == 'Thursday':
            day = 4
        elif input['weekday'] == 'Friday':
            day = 5
        elif input['weekday'] == 'Saturday':
            day = 6
        else:
            day = 0

        work = ''
        if input['workingday'] == 'Work':
            work = 1
        else:
            work = 0
        
        weather = ''
        if input['weathersit'] == 'Clear':
            weather = 1
        elif input['weathersit'] == 'Cloudy':
            weather = 2
        elif input['weathersit'] == 'Light':
            weather = 3
        else:
            weather = 4

        atemp=float(input['atemp'])
        hum=float(input['hum'])
        wind=float(input['windspeed'])

        event = ''
        if input['event'] == 'Yes':
            event = 1
        else:
            event = 0

        data_df={
            'season': season,
            'yr' : year,
            'mnth' : month,
            'hr' : hour,
            'holiday' : holiday, 
            'weekday' : day,
            'workingday' : work,
            'weathersit' : weather,
            'atemp' : atemp,
            'hum' : hum,
            'windspeed' : wind,
            'event' : event
        }

        df = pd.DataFrame(data_df, index=[1])


        # pred = Model.predict([[season, year, month, hour, holiday, day, work, weather, temp,atemp, hum, wind, event]])[0].round(0) #=> tanpa pipeline
        pred = Model.predict(df)[0].round(0) #=> make pipeline

        ## Untuk Isi Data
        season_dt = ''
        if input['season'] == 'Spring':
            season_dt = 'Spring'
        elif input['season'] == 'Summer':
            season_dt = 'Summer'
        elif input['season'] == 'Fall':
            season_dt = 'Fall'
        else:
            season_dt = 'Winter'

        month_dt = ''
        if input['mnth'] == 'January':
            month_dt = 'January'
        elif input['mnth'] == 'February':
            month_dt = 'February'
        elif input['mnth'] == 'March':
            month_dt = 'March'
        elif input['mnth'] == 'April':
            month_dt = 'April'
        elif input['mnth'] == 'May':
            month_dt = 'May'
        elif input['mnth'] == 'June':
            month_dt = 'June'
        elif input['mnth'] == 'July':
            month_dt = 'July'
        elif input['mnth'] == 'August':
            month_dt = 'August'
        elif input['mnth'] == 'September':
            month_dt = 'September'
        elif input['mnth'] == 'October':
            month_dt = 'October'
        elif input['mnth'] == 'November':
            month_dt = 'November'
        else:
            month_dt = 'December'

        holiday_dt = ''
        if input['holiday'] == 'Holiday':
            holiday_dt = 'Holiday'
        else:
            holiday_dt = 'Non-Holiday'
        
        day_dt = ''
        if input['weekday'] == 'Monday':
            day_dt = 'Monday'
        elif input['weekday'] == 'Tuesday':
            day_dt = 'Tuesday'
        elif input['weekday'] == 'Wednesday':
            day_dt = 'Wednesday'
        elif input['weekday'] == 'Thursday':
            day_dt = 'Thursday'
        elif input['weekday'] == 'Friday':
            day_dt = 'Friday'
        elif input['weekday'] == 'Saturday':
            day_dt = 'Saturday'
        else:
            day_dt = 'Sunday'

        work_dt = ''
        if input['workingday'] == 'Work':
            work_dt = 'Work'
        else:
            work_dt = 'Non-Work'
        
        weather_dt = ''
        if input['weathersit'] == 'Clear':
            weather_dt = 'Clear'
        elif input['weathersit'] == 'Cloudy':
            weather_dt = 'Cloudy'
        elif input['weathersit'] == 'Light Rain/Snow':
            weather_dt = 'Light Rain/Snow'
        else:
            weather_dt = 'Heavy Rain/Snow'

        event_dt = ''
        if input['event'] == 'Yes':
            event_dt = 'Yes'
        else:
            event_dt = 'No'

        return render_template('result.html',
            season=season_dt,
            year = int(input['yr']),
            month=month_dt,
            hour = int(input['hr']),
            holiday=holiday_dt,
            day=day_dt,
            work=work_dt,
            weather=weather_dt,
            atemp=float(input['atemp']),
            hum=float(input['hum']),
            wind=float(input['windspeed']),
            event=event_dt,
            bike_pred = pred
            )




if __name__ == '__main__':
    Model = joblib.load('Model_RF_RS')
    app.run(debug=True)



