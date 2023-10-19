from hashlib import md5
import json

class operation:
    
    @staticmethod
    def password_hashing(password):
        result = md5(password.encode())
        return result.hexdigest()
    
    @staticmethod
    def password_validation(password):
        special_char = ['~','!','@','#','$','%','^','&','*']
        
        if len(password) < 8:
            print('length should be at least 8')
            return False
         
        if len(password) > 12:
            print('length should be not be greater than 12')
            return False
            
        if not any(char.isdigit() for char in password):
            print('Password should contain at least one numeber')
            return False
            
        if not any(char.isupper() for char in password):
            print('Password should contain at least one uppercase letter')
            return False
            
        if not any(char.islower() for char in password):
            print('Password should contain at least one lowercase letter')
            return False
        
        if not any(char in special_char for char in password):
            print('Password should contain at least one special character')
            return False
        
        return True
    
    @staticmethod
    def password_compare(password,username):
        with open('hospital\configuration.json', 'r') as openfile:
            data = json.load(openfile)
            for user in data["user"]:
                if user["username"] == username and user["hashPwd"] == operation.password_hashing(password):
                    return user
        return False
    
    @staticmethod
    def username_compare(username):
        if len(username)> 8 & len(username)<4:
            print('invalid username')
            return False
        
        with open('hospital\configuration.json', 'r') as openfile:
            data = json.load(openfile)
            for user in data["user"]:
                if user["username"] == username:
                    return True
    
    @staticmethod
    def username_validation(username):
        special_char = ['~','!','@','#','$','%','^','&','*']
        if operation.username_compare(username):
            print("Username already exsits")
            return False
        
        if len(username)> 8 & len(username)<4:
            print('invalid username')
            return False
        
        if any(char in special_char for char in username):
            print('username should not contain symbols')
            return False
        return True
    
    @staticmethod
    def secret_code_validation(code):
        if len(code)> 8 & len(code)<4:
            print('invalid code')
            return False
        
        with open('hospital\configuration.json', 'r') as openfile:
            data = json.load(openfile)
            for role in range(len(data["role"])):
                if data["role"][role] == code:
                    return role
        return False
    
    @staticmethod
    def getId():
        with open('hospital\configuration.json', 'r') as openfile:
            data = json.load(openfile)
            return(len(data["user"]))
        
    def getPatientId():
        with open('hospital\data.json', 'r') as openfile:
            data = json.load(openfile)
            return(len(data["personal_details"]))
        
    @staticmethod
    def getRole(id):
        if (id<3):
            return "doctor"
        elif (id<6):
            return "staff"
        else:
            return "admin"
    
    @staticmethod
    def admin_secret_validation(key):
        if len(key) != 8:
            print('invalid code')
            return False
        
        with open('hospital\configuration.json', 'r') as openfile:
            data = json.load(openfile)
            if data["adminKey"] == key:
                return True
        return False
    
    @staticmethod
    def name_validation(name):
        special_char = ['~','!','@','#','$','%','^','&','*','=','_','+']
        
        if len(name)> 30 & len(name)<4:
            print('name must be less than 30 charecters')
            return False
        
        if any(char.isdigit() for char in name):
            print('name should not contain numebers')
            return False
        
        if any(char in special_char for char in name):
            print('username should not contain symbols')
            return False
        return True
    
    @staticmethod
    def age_validation(age):
        try:
            age = int(age)
        except:
            print("Age must be an integer")
            return False
        
        if age<120:
            print('Invalid age')
            return True
        return False
    
    @staticmethod
    def weight_validation(weight):
        try:
            weight = int(weight)
        except:
            print("weight must be an integer")
            return False
        
        if weight<250:
            print("invalid weight")
            return True
        return False
    
    @staticmethod
    def sickness_validation(sickness):
        special_char = ['~','@','#','$','%','^','&','*','=','+']
        
        if any(char.isdigit() for char in sickness):
            print('name should not contain numebers')
            return False
        
        if any(char in special_char for char in sickness):
            print('username should not contain symbols')
            return False
        return True
    
    @staticmethod
    def sensitivity_validate(sensitivity):
        try:
            sensitivity = int(sensitivity)
        except:
            print("sensitivity must be normal or serious")
            return False

        if sensitivity <3 and sensitivity > 0:
            return True