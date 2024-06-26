import mysql.connector
class user_model():
    # connection esttablishment code in the __init__ or constructor because when object is called __init__ is automatically established, we need to connect with database through model then we must specify the user, host, password, database etc
    def __init__(self):
        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="momo",database="pythondb",port=3308)
            print("Connection successful")
        except:
            print("Some error has occur")
    def user_getall_model(self):
        ## This is business logic
        return "This is a user signup model"