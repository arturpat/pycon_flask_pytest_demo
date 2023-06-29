# HTML templates source: https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application
from flask import Flask, render_template, request, url_for, flash, redirect

from solution_accuweather_proxy import AccuweatherProxy

app = Flask(__name__)
app.secret_key = 'super secret key'  # without this flask will refuse to 'flash'
messages = []

weather_proxy = AccuweatherProxy(apikey="ADuP1UGtZCSRyLyM2lRcSTalxzBxbaqD")  # Artur's demo temporary key

# Flask "debug mode" is something else, see: https://flask.palletsprojects.com/en/2.2.x/quickstart/#debug-mode


@app.route('/')
def index():
    return render_template('index.html', messages=messages)


@app.route('/weather/', methods=('GET', 'POST'))
def weather():
    weather_forcast = ""
    if request.method == 'POST':
        city_key = weather_proxy.find_city_key(request.form['city'])
        weather_forcast = weather_proxy.get_forecast_for_city_by_key(city_key)
        messages.append({'title': request.form['city'],
                         'content': weather_forcast})

    return render_template('weather.html', weather_data=weather_forcast)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        # example: understand handling two methods in one function
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')
