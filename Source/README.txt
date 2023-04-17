File Explanation
manage.py -- our launcher for every django related command... do not bother
db.sqlite3 -- our prebuilt database


messesnger/ -- our website folder
messesnger/__pycache__ -- do not bother
messesnger/__init__.py -- identifier that this folder is python package... do not bother
messesnger/settings.py -- contains all our settings for our project and installed apps declarations
messesnger/urls.py -- is where our app will look to find urls and paths in which we can include urls from other apps
messesnger/views.py -- our starting page view
messesnger/wsgi.py -- our web server getaway interface... do not bother



static/ --our css and js files if we have any


templates/ --our html code
templates/base.html --one of our base html code
templates/home.html --the second base html code
templates/accounts -- rest of html code


accounts/ -- our app folder
accounts/__pycache__ -- do not bother
accounts/migrations -- the connections built between models and database made by migrate and makemigrations commands... do not bother
accounts/__init__.py -- identifier that this folder is python package... do not bother
accounts/apps.py -- setting about our app
accounts/admin.py -- settings considering the administrator
accounts/tests.py -- how to deploy tests
accounts/urls.py -- urls to start views functions
accounts/views.py -- our python functions that will call the html pages and the forms to create the front end
accounts/models.py -- our data sets that will represent a real life model
accounts/forms.py -- changes to models.py in order to achieve the front end and sometimes back end functionality we want

