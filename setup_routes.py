from flask import Flask 

app = Flask(__name__)

def setup_routes():
    import root
    import controller_signup.about as about
    import controller_signup.contact as contact
    import controller_signup.signup as signup
    
    root.resgister_routes(app)
    about.register_routes(app)
    contact.register_routes(app)
    signup.register_route(app)