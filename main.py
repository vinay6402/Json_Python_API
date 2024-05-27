# Tasks:
# 1. get,
# 2. by user id
# 3. post - create user
# 4. update user - like name change

from flask import Flask, jsonify, request
import json
import json_functions as JF #custom json functions in json_functions.py file

#json data in multiline string format
users_str = '''
[
  {
    "name": "vinay",
    "id": 1
  },
  {
    "name": "kiran",
    "id": 2
  }
]
'''
users_json = json.loads(users_str) #In json format

app = Flask(__name__) 

@app.route('/', methods = ['GET']) #GET - home page with instruction
def home():
    return ''' localhost:port/users for list of users.   
    localhost:port/users/id for individual user name.   
    localhost:port/update_user/ for user name update'''


@app.route('/users/', methods=['GET']) #GET - display all users
def users_list_disp():
    return jsonify(users_json)

@app.route('/users/<int:id_num>', methods=['GET']) #GET - get user's name by id
def get_user_by_id(id_num):
    print(JF.user_by_id(users_json, id_num))
    return JF.user_by_id(users_json, id_num)

@app.route('/add_user', methods=['POST']) #POST - add new user
def add_new_user():
    new_name = request.json
    JF.add_new_user(users_json,new_name["name"])
    return users_json

@app.route('/update_user', methods=['PUT']) #PUT - update existing user's name
def update_user():
    updated_user_name_json = request.json
    return JF.update_user(users_json,updated_user_name_json["id"],updated_user_name_json["name"])

if __name__ == '__main__': 
    app.run(debug = True) 