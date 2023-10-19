import json
from hospital.authentication.operations import *

class Admin:
    
    @staticmethod
    def remove_user_by_Id():
        try:
            id = int(input("Enter the user Id : "))
        except:
            print("user id must be a number")
        jsonFile = open("hospital\configuration.json", "r")
        data = json.load(jsonFile) 
        jsonFile.close()
        found = None
        for index in range(len(data["user"])):
            if(data["user"][index]["userId"] == id):
                found = index
        
        if(found != None):
            secret_key = input("Input admin secret key : ")
            if operation.admin_secret_validation(secret_key):
                del data["user"][found]
                print("successfully deleted")
            else:
                print("Secret key unmatched try again")
        else:
            print("Invalid id")
        jsonFile = open("hospital\configuration.json", "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()
        
    @staticmethod
    def view_user_role_code():
        secret_key = input("Enter the admin secret key : ")
        print(operation.admin_secret_validation(secret_key))
        if operation.admin_secret_validation(secret_key):
            jsonFile = open("hospital\configuration.json", "r")
            data = json.load(jsonFile) 
            jsonFile.close()
            for id in range(len(data["role"])):
                if id == 0:
                    print('''
1 ->    User role           : Doctor
        Privilage level     : 1
        Capable of doing    : update patient detail
                              view a specific patient's details
                              view all patients detail list
        Secret code         : '''+data["role"][id])
                if id == 1:
                    print('''
2 ->    User role           : Doctor
        Privilage level     : 2
        Capable of doing    : update patient detail
                              view a specific patient's details
        Secret code         : '''+data["role"][id])
                if id == 2:
                    print('''
3 ->    User role           : Staff
        Privilage level     : 3
        Capable of doing    : create patient accounts
        Secret code         : '''+data["role"][id])
                if id == 3:
                    print('''
4 ->    User role           : Staff
        Privilage level     : 4
        Capable of doing    : view a specific patient's details
        Secret code         : '''+data["role"][id])
                if id == 4:
                    print('''
5 ->    User role           : Staff
        Privilage level     : 5
        Capable of doing    : create patient accounts
                              view a specific patient's details
        Secret code         : '''+data["role"][id])
                if id == 5:
                    print('''
6 ->    User role           : Admin
        Privilage level     : 6
        Capable of doing    : view secret codes to give users
                              delete user accounts
        Secret code         : '''+data["role"][id])
                    
        else:
            print("Invalid secret key")