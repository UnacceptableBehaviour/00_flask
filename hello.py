# to run this.
# cd into repo
# .pe   (activate venv)
# flask run

from flask import Flask, render_template
app = Flask(__name__)


def get_nutridata():
             #  0          1              2             3             4    5    6    7    8    9
    header = 'rcp_id,image_filename,recipe_title,txt_ingredient_file,n_En,n_Fa,n_Fs,n_Fm,n_Fp,n_Fo3,n_Ca,n_Su,n_Fb,n_St,n_Pr,n_Sa,n_Al,serving_size'
    text = '1,20190306_145901_seabass kale and potato dinner.jpg,seabass kale and potato dinner,20190306_145901_seabass kale and potato dinner.txt,55,1.6,0.44,0.5,0.43,0.4,2.74,0.32,0.47,0.0,7.28,0.45,0.0,450.0'
    
    header_list = header.split(',') 
    rcp_list = text.split(',')

    info = {}
    
    for i in range( len(header_list) ):        
        info[ header_list[i] ] = rcp_list[i]
        #print(f"{ header_list[i] } = { info[ header_list[i] ] }")
        
    info['n_EnkJ'] = str( round( float( info['n_En'] ) * 4.184 ) )
    info['serving_size'] = str( round( float( info['serving_size'] ) ) )
    
    return info


def get_nutrients_per_serving():
    info = get_nutridata()
    
    nutrient_keys = 'n_En,n_Fa,n_Fs,n_Fm,n_Fp,n_Fo3,n_Ca,n_Su,n_Fb,n_St,n_Pr,n_Sa,n_Al'.split(',')
    
    multiplier = float( info['serving_size'] ) / 100.0
    
    b4 = 0
    
    for key in nutrient_keys:
        b4 = info[key]
        info[key] = str( round( ( float( info[key] ) * multiplier ), 1 ) )
        print(f"key:{key} - b4:{b4} - x:{multiplier} - conv:{info[key]}- conv:{info[key].__class__.__name__}")

    return info


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

@app.route('/js')
def java_script():
    headline = 'Java buttons init!!?'
    
    image_list = ["/static/images/20190128_140750_lemon_grass_chicken_lo_cal.jpg",
                "/static/images/20190101_171835_venison_wellington_turkey_croquette.jpg"]
    
    return render_template("java_buttons.html", headline=headline, image_list=image_list)

@app.route('/recipe')
def recipe():
    headline = "LOW FAT Crab & Prawn Lunch"    
    return render_template("recipe_template.html", recipe_name=headline, recipe_2='Gimme beef')


@app.route('/nutri_lights')
def nutri_lights():
    #info = get_nutridata()
    info = get_nutrients_per_serving()
    
    return render_template("nutrients_traffic_lights.html", info=info )
    
    # was - scruffy and long winded!    
    # return render_template("nutrients_traffic_lights.html",
    #                         n_EnkJ=str( float( info['n_En'] ) * 4.184 ),
    #                         n_Encal=info['n_En'],
    #                         n_Fa=info['n_Fa'],
    #                         n_Fs=info['n_Fs'],
    #                         n_Su=info['n_Su'],
    #                         n_Sa=info['n_Sa'],
    #                         recipe_name=info['recipe_title'],
    #                         serving_size=f"{info['serving_size']}g",
    #                         recipe_2='Gimme beef')


# this one passes the last part of the URL as an srgument in the variable var_name
# EG http://127.0.0.1:5000/bloaty/bloaty
# Screen: Path was: bloaty/bloaty <
@app.route('/<path:var_name_path>')
def get_path(var_name_path):
    return f"Path was: {var_name_path} <"



# for images :
# http://127.0.0.1:5000/20190128_140750_lemon_grass_chicken_lo_cal.jpg
# http://127.0.0.1:5000/images/images/20190128_140750_lemon_grass_chicken_lo_cal.jpg
# http://127.0.0.1:5000/images/20190101_171835_venison_wellington_turkey_croquette.jpg
# http://127.0.0.1:5000/templates/css_breakout.css

