import json
import requests


def ObjectToPaymentData(obj): 
    #removing unnecesary brackets
    json_string = json.dumps(obj.__dict__)
    json_string = json_string.replace("[","")  
    json_string = json_string.replace("]","")
    return json.loads(json_string)   


def ExecuteTransaction(transaction):
    #function for executing API request. It takes transaction object as input.
    headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization": getattr(transaction,"auth")}
    
    
    data = {"payment_transaction": ObjectToPaymentData(transaction)
        }
    request = requests.post(getattr(transaction,"url"), headers=headers, json=data) #passing multiple parameters irrelevant ot the API
    return request
    
    

def readStatus(response):
    #function for reading the status code and if it is 200 the whole response.
    print("Status code: " + str(response.status_code)) 
    if (response.status_code != 200):
        return response.status_code
    else:
        pretty_json = json.loads(response.text)
        print(json.dumps(pretty_json, indent=2))