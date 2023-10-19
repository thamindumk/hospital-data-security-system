from hospital.authentication.operations import *
import json

class Staff:
    
    @staticmethod
    def Create_patient():
        patient = {}
        sickness_detail = {}
        patient["id"] = operation.getPatientId()
        sickness_detail["patientId"] = operation.getPatientId()
        
        name = input("Name of the patient : ")
        age = input("Age of the patient : ")
        weight = input("weight of the patient : ")
        sickness = input("Enter the sickness details : ")
        select = input("sensitivity level of the patient\n 1 -> normal\n 2 -> serious\nSelect the level : ")
        
        if operation.name_validation(name) and operation.age_validation(age) and operation.weight_validation(weight) and operation.sickness_validation(sickness) and operation.sensitivity_validate(select):
            patient["name"] = name
            patient["age"] = age
            patient["weight"] = weight
            patient["sensitivity"] = int(select)
            sickness_detail["detail"] = sickness
            jsonFile = open("hospital\data.json", "r") # Open the JSON file for reading
            data = json.load(jsonFile) # Read the JSON into the buffer
            jsonFile.close()
                
            data["personal_details"].append(patient)
            data["sickness_details"].append(sickness_detail)
            
            jsonFile = open("hospital\data.json", "w+")
            jsonFile.write(json.dumps(data))
            jsonFile.close()
            print("successfully created a petient")
            
    @staticmethod
    def view_patient(user):
        try:
            id = int(input("Enter the patient Id : "))
        except:
            print("patient id must be a number")
        jsonFile = open("hospital\data.json", "r")
        data = json.load(jsonFile) 
        jsonFile.close()
        found = None
        
        for index in range(len(data["personal_details"])):
            if(data["personal_details"][index]["id"] == id):
                found = index
        
        if(found != None):
            if data["personal_details"][found]["sensitivity"] == 1:
                print(data["personal_details"][found])
            elif user["privilageLv"] == 1 or user["privilageLv"] == 2 or user["privilageLv"] == 5:
                print(user["privilageLv"])
                print(data["personal_details"][found])
            else:
                print("You have no access to view that patient")
        else:
            print("Invalid id")
    