import json
from hashlib import md5
from hospital.authentication.operations import *

class sign_up:
    
    @staticmethod
    def createUser():
        user = {}
        count = 0;
        print("You should have a secret code that is given to you by adminstration")
        code = input("Enter the secret code : ")
        while count != 2:
            privilageLevel = operation.secret_code_validation(code)
            if privilageLevel != False:
                print("Create a username with length 8 to 12 characters excluding symbols(~!@#$%^&*) ")
                username = input("Enter your username : ")
                while True:
                    if operation.username_validation(username):
                        print("Create a password with length 8 to 12 characters should include at least an uppercase, a lowercase, a number and a symbol(~!@#$%^&*)")
                        password = input("Enter the password : ")
                        while True:
                            if operation.password_validation(password):
                                con_pass = input("Confirm password : ")
                                if con_pass == password:
                                    result = md5(password.encode())
                                    user["userId"] = operation.getId()
                                    user["hashPwd"] = result.hexdigest()
                                    user["username"] = username
                                    user["role"]= operation.getRole(privilageLevel+1)
                                    user["privilageLv"] = privilageLevel+1
                                    
                                    jsonFile = open("hospital\configuration.json", "r") # Open the JSON file for reading
                                    data = json.load(jsonFile) # Read the JSON into the buffer
                                    jsonFile.close()
                                        
                                    data["user"].append(user)
                                    
                                    jsonFile = open("hospital\configuration.json", "w+")
                                    jsonFile.write(json.dumps(data))
                                    jsonFile.close()
                                    break
                                else:
                                    print("confirm password not match try again")
                            else:
                                print("Invalid password")
                                password = input("re-enter the password : ")
                    else:
                        username = input("re-enter a username : ")
                    break   
            else:
                code = input("Re-Enter the code : ")
            count = count + 1
            break
        print("You entered the invalid code 2 time please check again and try later")    
            