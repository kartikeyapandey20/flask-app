import mysql.connector
import json
from flask import make_response ,request
import jwt
import re
from functools import wraps
from config.config import dbconfig
class TokenModel:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host=dbconfig["hostname"],user=dbconfig["username"],password=dbconfig["password"],database=dbconfig["flask_tutorial"])
            self.con.autocommit=True
            self.cur = self.con.cursor(dictionary=True)
            print("connection successful")
        except:
            print("failed")
    def token_auth(self,endpoint=""):
        def inner1(func):
            @wraps(func)
            def inner2(*args):
                endpoint = request.url_rule
                authorization = request.headers.get("authorization")
                if re.match("^Bearer *([^ ]+) *$",authorization , flags=0):
                    token = authorization.split(" ")[1]
                    try:
                        jwt_decoded = jwt.decode(token,"kartikeya",algorithms="HS256")
                    except jwt.ExpiredSignatureError:
                        return make_response({"ERROR" : "TOKEN EXPRIED"},401)
                    role_id = jwt_decoded["playload"]["roles_id"]
                    self.cur.execute(f"SELECT roles FROM access_view WHERE endpoints = '{endpoint}'")
                    result = self.cur.fetchall()
                    if len(result)>0:
                        allowed_roles = json.loads(result[0]["roles"])
                        if(role_id is allowed_roles):
                            return func(*args)
                        else:
                            return make_response({"ERROR" : "INVALID USER"},404)
                    else:
                        return make_response({"ERROR" : "UNKNOWN ENDPOINT"},404)
                else:
                    return make_response({"ERROR" : "INVALID AUTHORIZATION"}, 401)
            return inner2
        return inner1