from flask import Flask, render_template
app = Flask(__name__)

# each app.route is an endpoint

@app.route('/helloo')
def hello_world():
    return 'Hello, World!!!!'

@app.route('/Simon')
def hello_s():
    return 'Hello, Simon'

@app.route('/appname')
def report_appname():
    appname = __name__      
    return f"First Flask App, {appname}!!"

# this one passes the last part of the URL as an srgument in the variable var_name
@app.route('/<string:var_name>')
def hello(var_name):
    return f"Hello, {var_name}!!"

# these execute templates stored in the directory templates (in project folder)
# this passes a veariable headline into the index.html template
# it replace {{ headline }} in the template
@app.route('/')
def index():
    headline_py = "FAT Turkey"
    return render_template("index.html", headline=headline_py)


@app.route('/recipe')
def recipe():
    headline = "LOW FAT Crab & Prawn Lunch"
    return render_template("recipe_template.html", recipe_name=headline, recipe_2='Gimme beef')

# this one passes the last part of the URL as an srgument in the variable var_name
@app.route('/<path:var_name_path>')
def get_path(var_name_path):
    return f"Path was: {var_name_path} <"



# for images :
# http://127.0.0.1:5000/20190128_140750_lemon_grass_chicken_lo_cal.jpg
# http://127.0.0.1:5000/images/images/20190128_140750_lemon_grass_chicken_lo_cal.jpg
# http://127.0.0.1:5000/images/20190101_171835_venison_wellington_turkey_croquette.jpg
# http://127.0.0.1:5000/templates/css_breakout.css

