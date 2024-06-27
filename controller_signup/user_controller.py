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
    
    @app.route("/user/update", methods=["PUT"])
    def user_update_controller():
        return obj.user_update_model(request.form)
    
    @app.route("/user/delete/<id>", methods=["DELETE"])
    def user_delete_controller(id):
        return obj.user_delete_model(id)
    
    @app.route("/user/patch/<id>", methods=["PATCH"])
    def user_patch_controller(id):
        return obj.user_patch_model(request.form, id)
    
    @app.route("/user/getall/limit/<limit>/page/<page>", methods=["GET"])
    def user_pagination_controller(limit, page):
        return obj.user_pagination_model(limit, page) 
        