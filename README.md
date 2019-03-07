# 00_flask
Flask tutorial - newbie level


Setting up and running Flask - Hello world
$ cd /Users/simon/a_syllabus/lang/python/00_flask 	# create project directory
$ python3 -m venv venv								# create virtual envirmonment - assuming like rvm
$ ls
venv
$ . venv/bin/activate								# activate environment
(venv) $ pip install Flask
Successfully installed Flask-1.0.2 Jinja2-2.10 MarkupSafe-1.1.1 Werkzeug-0.14.1 click-7.0 itsdangerous-1.1.0
(venv) $ ls
hello.py	venv

$ export FLASK_APP=hello.py							# ADDED to ~/.bash_profile
$ flask run
(venv) $ flask run
 * Serving Flask app "hello.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

										# ADDED to ~/.bash_profile
$ export FLASK_ENV=development							# TURN ON DEBUG MODE - Auto reload on code changes	
$ flask run
 * Serving Flask app "hello.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 102-487-015

Trying to serve image from directory
<!-- one image served localy using Node.js server WORK —>
<img src="http://192.168.0.8:8000/images/20190217_162807_mon_prawn_n_crabcake_mango_salsa.jpg" width="430" height="286">

<!-- one image pulled from Gtihub repo - link from DLOAD button WORKS —>
<img src="https://github.com/UnacceptableBehaviour/html_label/raw/recipe_page/images/20190217_144626_sun_steak_aub_tartar.jpg" width="430" height="286">

<!-- project folder image directory FAILS —>
<img src="20190128_140750_lemon_grass_chicken_lo_cal.jpg" width="430" height="286">

<!-- project folder image directory FAILS -->
<img src="20190101_171835_venison_wellington_turkey_croquette.jpg" width="430" height="286">

The empty place holder has the follow link:
http://127.0.0.1:5000/20190101_171835_venison_wellington_turkey_croquette.jpg

Need to create a folder static which is where it finds these files, and the .css file
