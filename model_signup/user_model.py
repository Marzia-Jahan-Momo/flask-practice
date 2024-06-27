import mysql.connector
import json
from flask import make_response
class user_model():
    # connection esttablishment code in the __init__ or constructor because when object is called __init__ is automatically established, we need to connect with database through model then we must specify the user, host, password, database etc
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="momo",
                database="pythondb",
                port=3308)
            self.conn.autocommit=True
            self.myc = self.conn.cursor(dictionary=True)
            print("Connection successful")
        except:
            print("Some error has occur")
    def user_getall_model(self):
        try:
            ## This is business logic
            self.myc.execute("SELECT * FROM user")
            fetching = self.myc.fetchall()
            # print(fetching) ->>> if you write print than it will show into terminal but if you write return then it will be shown into browser
            #return fetching
            
            if len(fetching) > 0:
                # return json.dumps(fetching)  ## This will be string or text/html format
                return make_response({"Payload": fetching}, 200)    # This will be dictionary or json format
                # return fetching
            else:
                return make_response({"message":"No result found"}, 204)     ## generated JSON reply quickly      
        except mysql.connector.Error as e:
            print(f"Error fetching data from MySQL: {e}")
            return {"Error":" There has an error"}
        return "This is a user signup model"
            
        
    
    def user_addone_model(self, data):
        self.myc.execute(f"INSERT INTO user(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')") ## after establishment of connection from client to controller, then controller to model, now we can create our sql query
        #print(data)
        print(data["email"]) ## to specific see any data
        return make_response({"Message":"This is user_addone_model & successfully inserted data from client to db"}, 201) ## generated JSON reply quickly      
    
    def user_update_model(self, data):
        self.myc.execute(f"UPDATE user SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' WHERE id={data['id']} ")
        if self.myc.rowcount > 0:            
            return make_response({"Message":"This is update statements done by PUT method"}, 201)
        else:
            return make_response({"Message":"Nothing to update"}, 202)
    
    def user_delete_model(self, id):
        self.myc.execute(f"DELETE FROM user WHERE id={id}")
        if self.myc.rowcount >= 0:
            return make_response({"Message":"This is delete operation"}, 200)
        else:
            return make_response({"Message":"Nothing to delete"}, 202)
        