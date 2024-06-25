from flask import Flask 
import root
from controller_signup import about, contact, signup, dashboard

app = Flask(__name__)

def setup_routes():

    
    root.resgister_routes(app)
    about.register_routes(app)
    contact.register_routes(app)
    signup.register_route(app)
    dashboard.register_route(app)