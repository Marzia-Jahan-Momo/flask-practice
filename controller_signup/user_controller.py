from model_signup.user_model import user_model 
from flask import request
obj = user_model()
 
def register_route(app):
    @app.route("/user/getall") ## first read operation
    def user_getall_controller():
        return obj.user_getall_model()

    @app.route("/user/addone", methods=["POST"]) ## from here recieved a form from client to controller
    def user_addone_controller():
        #print(request.form)  ## after checked its recived the values, now need to send this data form to mdoel
        return obj.user_addone_model(request.form)