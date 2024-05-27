#get user's name by id-------------
def user_by_id(users_json, id_num):
    for each_userdata in users_json:
        if each_userdata["id"] == id_num:
            return each_userdata["name"]
#add user to json------------------
def get_max_id(users_json): #this get_max_id will give max id, which helps while assigning new id for new user
    IDs = set()
    for each_userdata in users_json:
        IDs.add(each_userdata["id"])
    return max(IDs)

def add_new_user(users_json, n_name):
    new_user = { "name": n_name, "id": get_max_id(users_json)+1}
    return users_json.append(new_user)
    

#update user using id and updated name----------------
def update_user(users_json,id_num, updated_user_name):
    for each_userdata in users_json:
        if each_userdata["id"] == id_num:
            each_userdata["name"] = updated_user_name
    return users_json