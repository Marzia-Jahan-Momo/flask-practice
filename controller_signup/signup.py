from model_signup.user_model_signup import user_model 
obj = user_model()
 
def register_route(app):
    @app.route("/user/signup")
    def signup():
        return obj.user_signup_model()