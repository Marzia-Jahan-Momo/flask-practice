from model_signup.user_model import user_model 
obj = user_model()
 
def register_route(app):
    @app.route("/user/getall") ## first read operation
    def signup():
        return obj.user_getall_model()