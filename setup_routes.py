from flask import Flask 

app = Flask(__name__)

def setup_routes():
    import root
    import about
    import contact
    
    root.resgister_routes(app)
    about.register_routes(app)
    contact.register_routes(app)