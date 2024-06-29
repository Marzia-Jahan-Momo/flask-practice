import mysql.connector
import json
from flask import make_response, request
import jwt
import re 
from functools import wraps


class auth_model():
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
    
    def token_auth(self, endpoint):
        def inner1(func):
            @wraps(func) 
            def inner2(*args):
                authorization = request.headers.get("Authorization")
                if re.match("^Bearer *([^ ]+) *$", authorization, flags=0):
                    token_with_split_auth = authorization.split(" ")[1]
                    try:
                        jwt_decoded = jwt.decode(token_with_split_auth, "JahanMomo", algorithms="HS256")
                    except:
                        return make_response({"ERROR": "TOKEN_EXPIRED"}, 401)
                    jwt_role_id = jwt_decoded['payload']['role_id']
                    self.myc.execute(f"SELECT roles from accessibility_view WHERE endpoint='{endpoint}'")
                    result = self.myc.fetchall()
                    if len(result) > 0:
                        allowed_role = json.loads(result[0]['roles'])
                        if isinstance(allowed_role, list) and jwt_role_id in allowed_role:
                            return func(*args)
                        else:
                            return make_response({"ERROR": "INVALID_ROLE"}, 404)
                    else:
                        return make_response({"ERROR": "UNKNOWN_ENDPOINT"}, 404)
                else:
                    return make_response({"ERROR":"INVALID_TOKEN"}, 401)
                 
            return inner2
        return inner1