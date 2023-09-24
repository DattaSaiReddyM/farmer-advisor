from Firebase_config import firebase,auth,db
import datetime
import json

def Register_firebase(data,password):
    try:
        # print(username,password,name)
        user = auth.create_user_with_email_and_password(data["email"],password) 
        print(user)
        id= auth.get_account_info(user['idToken'])
        key = id["users"][0]['localId']
        if isinstance(key, str): 
            # data={"username":username,"password":password,"name":name,"Registered_on": datetime.datetime.now(),"id":key,"interests":interests,"address":address}
            # print(data,key)
            key_dict = {"id":key}
            data.update(key_dict)
            db.collection('users').document(key).set(data)
        return "Success"
    except Exception as e:
        print(e)
        return "Failed"



def Login_firebase(username,password):
    try:
        print(username,password)
        name=""
        user = auth.sign_in_with_email_and_password(username,password)
        id= auth.get_account_info(user['idToken'])
        key = id["users"][0]['localId']
        if isinstance(key, str): 
            data={"last_login": datetime.datetime.now()}
            db.collection('users').document(key).update(data)
            n= db.collection('users').where("email","==" ,username).get()[0]
            name=n.to_dict()['name']
        return name
    except Exception as e:
        print(e)
        return "Failed"

def get_faq():
    faq = db.collection('faq').get()
    q_a = []
    for doc in faq:
        q_a.append(doc.to_dict())
    print(q_a)
    return q_a

def get_user_data(email):
    user = db.collection('users').where("email","==" ,email).get()
    for doc in user:
        user_data = doc.to_dict()

    return user_data
#     rewards = a.to_dict()['rewards']
#     return rewards

# a= Login_firebase("test@abc.coaa","12345") 
# print(a)
# print(type(id["users"][0]['localId']))
# a= db.collection('users').where("name","==" ,"test").get()[0].id
# print(a)

# def get_rewards_firebase(username):
#     a = db.collection('users').where("username","==" ,username).get()[0]
#     rewards = a.to_dict()['rewards']
#     return rewards

# def add_rewards_firebase(username,amt,action):
#     try:
#         a = db.collection('users').where("username","==" ,username).get()[0]
#         key=a.to_dict()['id']
#         rewards = a.to_dict()['rewards']
#         db.collection('users').document(key).update({"rewards":rewards+amt})
#         return "Updated"
#     except Exception as e:
#         print(e)
#         return "Failed"

# def get_user_info(username):
#     user_info = db.collection('users').where("username","==" ,username).get()[0]
#     return user_info.to_dict()


