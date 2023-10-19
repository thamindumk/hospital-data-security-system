from hospital.authentication.operations import *
import json

class Doctor:
    
    @staticmethod
    def view_patient():
        try: 
            id = int(input("Enter the patient Id : "))
        except:
            print("patient Id must be a number")
        jsonFile = open("hospital\data.json", "r")
        data = json.load(jsonFile) 
        jsonFile.close()
        found = None
        
        for index in range(len(data["personal_details"])):
            if(data["personal_details"][index]["id"] == id):
                found = index
        
        if(found != None):
             print(data["personal_details"][found])
        else:
            print("Invalid id")
    
    @staticmethod
    def update_patient():
        id = int(input("Enter the patient Id : "))
        jsonFile = open("hospital\data.json", "r")
        data = json.load(jsonFile) 
        jsonFile.close()
        found = None
        
        for index in range(len(data["personal_details"])):
            if(data["personal_details"][index]["id"] == id):
                found = index
                
        if(found != None): 
            try:    
                select = int(input(" 1 -> update drug prescription\n 2 -> update lab test presvription\nSelect the option : "))
            except:
                print("Selection must be an integer try again")
            if select == 1:
                drug = {}
                drug["patientId"] = found
                description = input("description of the drug : ")
                drug["description"] = description

                jsonFile = open("hospital\data.json", "r") 
                data = json.load(jsonFile) 
                jsonFile.close()
                    
                data["drug_prescriptions"].append(drug)
                
                jsonFile = open("hospital\data.json", "w+")
                jsonFile.write(json.dumps(data))
                jsonFile.close()
                print("successfully update the drug prescription of the patient")
            elif select == 2:
                lab_test = {}
                lab_test["patientId"] = found
                description = input("description of the drug : ")
                lab_test["description"] = description

                jsonFile = open("hospital\data.json", "r") 
                data = json.load(jsonFile) 
                jsonFile.close()
                    
                data["lab_test_prescriptions"].append(drug)
                
                jsonFile = open("hospital\data.json", "w+")
                jsonFile.write(json.dumps(data))
                jsonFile.close()
                print("successfully update the lab test prescription of the patient")
            else:
                print("Invalid option select")
        else:
            print("Invalid patient id") 
    
    @staticmethod
    def view_all_patient():
        jsonFile = open("hospital\data.json", "r") 
        data = json.load(jsonFile) 
        jsonFile.close()    
        
        for detail in data["personal_details"]:
            print(detail)   
        