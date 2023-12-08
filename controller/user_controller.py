from app import app
from model.user_model import UserModel
from model.token_model import TokenModel
from flask import request ,send_file
from datetime import datetime
obj = UserModel()
auth = TokenModel()
@app.route("/user/getall")
@auth.token_auth()
def user_get_controller():
    return obj.userGetModel()

@app.route("/user/addone",methods=["POST"])
@auth.token_auth()
def user_addone_controller():
    return obj.userAddModel(request.form)


@app.route("/user/addmultiple",methods=["POST"])
def user_addmultiple_controller():
    return obj.userAddMultipleModel(request.json)

@app.route("/user/updateone",methods=["PUT"])
def user_update_controller():
    return obj.userUpdateModel(request.form)

@app.route("/user/delete/<id>",methods=["DELETE"])
def user_delete_controller(id):
    return obj.userDeleteModel(id)

@app.route("/user/patch/<id>",methods=["PATCH"])
def user_patch_controller(id):
    return obj.userPatchModel(request.form ,id)

@app.route("/user/limit/<limit>/page/<page>",methods=["GET"])
def pagination(limit,page):
    return obj.userPagination(limit ,page)

@app.route("/user/<uid>/upload/avatar",methods=["PUT"])
def user_upload_avatar_controller(uid):
    file = request.files['avatar']
    uniqueFileName = str(datetime.now().timestamp()).replace(".","")
    fileNameSplit = file.filename.split(".")
    ext = fileNameSplit[len(fileNameSplit) - 1]
    finalFilePath = f"uploads/{uniqueFileName}.{ext}"
    file.save(finalFilePath)
    return obj.user_upload_avatar_model(uid,finalFilePath)
@app.route("/uploads/<filename>")
def get_avatar_conrtoller(filename):
    return send_file(f"upload/{filename}")

@app.route("/user/login", methods=["POST"])
def user_login_controller():
    return obj.user_login_model(request.form)
