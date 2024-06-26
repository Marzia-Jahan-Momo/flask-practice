import mysql.connector
import json
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
            self.myc = self.conn.cursor(dictionary=True)
            print("Connection successful")
        except:
            print("Some error has occur")
    def user_getall_model(self):
        try:
            
            self.myc.execute("SELECT * FROM user")
            fetching = self.myc.fetchall()
            # print(fetching) ->>> if you write print than it will show into terminal but if you write return then it will be shown into browser
            #return fetching
            # but we need to specify into string format with:
            if len(fetching) > 0:
                return json.dumps(fetching)
            else:
                return "No result found" 
        ## This is business logic
        except mysql.connector.Error as e:
            print(f"Error fetching data from MySQL: {e}")
            return []
        return "This is a user signup model"