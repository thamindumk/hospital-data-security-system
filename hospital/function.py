from hospital.userRoles.admin import *
from hospital.userRoles.staff import *
from hospital.userRoles.doctor import *

class Handle:
    
    @staticmethod
    def controll(user):
        privilageLv = user["privilageLv"]
        if(privilageLv == 1):
            while True:
                print("1 -> update a patient account\n2 -> view a specific patient\n3 -> view all patient personal details\n4 -> Exit")
                try:
                    select = int(input("Select the options : "))
                except:
                    print("selection must be an integer")
                    
                if select == 1:
                   Doctor.update_patient()
                elif select == 2:
                   Doctor.view_patient() 
                elif select == 3:
                    Doctor.view_all_patient() 
                elif select == 4:
                    exit()
                else:
                    print("invalid input")
        if(privilageLv == 2):
            while True:
                print("1 -> update a patient account\n2 -> view a specific patient\n3 -> Exit")
                try:
                    select = int(input("Select the options : "))
                except:
                    print("selection must be an integer")
                if select == 1:
                   Doctor.update_patient()
                elif select == 2:
                   Doctor.view_patient()
                elif select == 3:
                    exit() 
                else:
                    print("invalid input")
        if(privilageLv == 3):
            while True:
                print("1 -> create a patient account\n2 -> Exit")
                try:
                    select = int(input("Select the options : "))
                except:
                    print("selection must be an integer")
                if select == 1:
                   Staff.Create_patient() 
                elif select == 2:
                    exit()
                else:
                    print("invalid input")
            
        if(privilageLv == 4):
            while True:
                print("1 -> view a specific patient\n2 -> Exit")
                try:
                    select = int(input("Select the options : "))
                except:
                    print("selection must be an integer")
                if select == 1:
                   Staff.view_patient(user)
                elif select == 2:
                    exit()  
                else:
                    print("invalid input")
            
        if(privilageLv == 5):
            while True:
                print("1 -> create a patient account\n2 -> view a specific patient\n3 -> Exit")
                try:
                    select = int(input("Select the options : "))
                except:
                    print("selection must be an integer")
                if select == 1:
                   Staff.Create_patient()
                elif select == 2:
                   Staff.view_patient(user)
                elif select == 3:
                    exit()  
                else:
                    print("invalid input")
        
        if(privilageLv == 6):
            while True:
                print("1 -> view secret codes to give users \n2 -> delete user accounts\n3 -> Exit")
                try:
                    select = int(input("Select the options : "))
                except:
                    print("selection must be an integer")
                if select == 1:
                    Admin.view_user_role_code() 
                elif select == 2:
                    Admin.remove_user_by_Id()
                elif select == 3:
                    exit()
                else:
                    print("invalid input")