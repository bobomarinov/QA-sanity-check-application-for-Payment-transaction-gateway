import json
import requests


def ObjectToPaymentData(obj): #function for converting the object to the format required by the API
    json_string = json.dumps(obj.__dict__) #converting the object to json string
    json_string = json_string.replace("[","")  
    json_string = json_string.replace("]","")   
    return json.loads(json_string) 


def ExecuteTransaction(transaction):
    #function for executing the transaction
    headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization": getattr(transaction,"auth")} #setting the headers for the request
    
    
    data = {"payment_transaction": ObjectToPaymentData(transaction) } #converting the object to the format required by the API and setting the data for the request
    request = requests.post(getattr(transaction,"url"), headers=headers, json=data) #passing multiple parameters irrelevant of the API
    return request
    
    

def readStatus(response):
    #function for reading the status of the transaction
    print("Status code: " + str(response.status_code)) 
    if (response.status_code != 200): #if the status code is not 200 then the transaction failed
        return response.status_code #return the status code
    else: #if the status code is 200 then the transaction was successful
        pretty_json = json.loads(response.text) #converting the response to json and loading it into a variable
        print(json.dumps(pretty_json, indent=2)) #printing the json in a pretty format
