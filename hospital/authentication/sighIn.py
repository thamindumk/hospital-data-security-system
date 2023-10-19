import json
from hashlib import md5
from hospital.authentication.operations import *

class sign_in:
    
    @staticmethod
    def getUser():
        username = input("Enter the username : ")
        while True:
            if operation.username_compare(username):
                password = input("Enter the password : ")
                while True:
                    user = operation.password_compare(password,username)
                    if user != False:
                        del user['hashPwd']
                        return user
                    else:
                        print("invalid password")
                        password = input("re-enter the password : ")
            else:
                print("Invalid username")
                username = input("re-enter the username")