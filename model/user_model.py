import mysql.connector
import json
from flask import make_response
from datetime import datetime , timedelta
import jwt
from config.config import dbconfig
class UserModel:
    def __init__(self):
        try:
            print(dbconfig)
            self.con = mysql.connector.connect(host=dbconfig["hostname"],user=dbconfig["username"],password=dbconfig["password"],database=dbconfig["database"])
            # self.con = mysql.connector.connect(host="localhost",user="root",password="#VIP2888",database="flask_tutorial")
            self.con.autocommit=True
            self.cur = self.con.cursor(dictionary=True)
            print("connection successful")
        except:
            print("failed")
    def  userGetModel(self):
        # connections establisment
        # query establisment
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        print(result)
        if len(result) >0:
            # return json.dumps(result)
            res = make_response({"payload" : result},200)
            res.headers["Access-Control-Allow-Origin"] = "*"
            return res
        else:
            return make_response({"message" :"No data found"},204)


    def userAddModel(self,data):
        # connections establisment
        # query establisment
        self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        print(data)
        return make_response({"message" :"User Created Successfully"},201)
    
    def userAddMultipleModel(self,data):
        # connections establisment
        # query establisment
        # self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        print(data)
        qry = "INSERT INTO users(name,email,phone,role,password) VALUES"
        for userdata in data:
            qry += f"('{userdata['name']}','{userdata['email']}','{userdata['phone']}','{userdata['role']}','{userdata['password']}'),"
        finalQuery = qry.strip(",")
        self.cur.execute(finalQuery)    
        return make_response({"message" :"Multiple User Created Successfully"},201)

    def userUpdateModel(self,data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({"message" :"User Updated Successfully"},201)
        else:
            return make_response({"message" :"No data found"},202)
    def userDeleteModel(self,id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message" :"User deleted successfully"},200)
        else:
    
            return make_response({"message" :"No data found"},204)
    def userPatchModel(self,data,id):
        qry = "UPDATE users SET "
        for key in data:
            qry += f"{key}='{data[key]}',"
        qry = qry[:-1] + f"WHERE id={id}"
        self.cur.execute(qry)
        print(qry)
        if self.cur.rowcount>0:
            return make_response({"message" :"User Updated Successfully"},201)
        else:
            return make_response({"message" :"No data found"},202)
        
    def userPagination(self,limit, page):
        limit = int(limit)
        page = int(page)
        start = (page*limit) - limit    
        qry = f"SELECT * FROM users LIMIT {start} , {limit}"
        self.cur.execute(qry)
        result = self.cur.fetchall()
        print(result)
        if len(result) >0:
            # return json.dumps(result)
            res = make_response({"payload" : result , 
            "page_no" : page ,
            "limit" : limit},200)
            return res
        else:
            return make_response({"message" :"No data found"},204)
    def user_upload_avatar_model(self,uid,filepath):
        self.cur.execute(f"UPDATE users set avatar = '{filepath}' WHERE id = {uid}")
        if self.cur.rowcount>0:
            return make_response({"message" :"FILE_UPLOADED_SUCCESSFULLY", "filePath" : filepath},201)
        else:
            return make_response({"message" :"No data found"},202)
    def user_login_model(self, data):
        self.cur.execute(f"SELECT id , name , email , phone ,avatar , roles_id  FROM users Where email ='{data['email']}' AND password ='{data['password']}'")
        
        result = self.cur.fetchall()
        userdata = result[0]
        exp_time = datetime.now() + timedelta(minutes=15)
        exp_epoch_time = int(exp_time.timestamp())
        payload= {
            "playload" : userdata,
            "exp" : exp_epoch_time
        }
        token = jwt.encode(payload, "kartikeya", algorithm="HS256")
        return make_response({"token" : token}, 200)