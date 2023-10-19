from hashlib import md5
from hospital.authentication.signUp import *
from hospital.authentication.sighIn import *
from hospital.function import *

def route():
    user = None
    select = None
    while True:
        print("1 -> Sign Up \n2 -> Log In")
        try:
            select = int(input("Select the options : "))
        except:
            print("selection must be a number")
            
        if select == 1:
            sign_up.createUser()
        elif select == 2:
            user = sign_in.getUser()
            break
        else:
            print("invalid input")
    Handle.controll(user)     
    
if __name__ == "__main__":
    route()