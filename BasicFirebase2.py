import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import time
import requests
import random



cred = credentials.Certificate("./icansdk.json")
app = firebase_admin.initialize_app(cred)
url = "https://icanpolsri-a0d38-default-rtdb.asia-southeast1.firebasedatabase.app/"

ref = db.reference("/", app, url)




def getSensorData():
    dis = str(round(30 + random.random()*0.3, 1))
    ph =  str(round(7 + random.random()*0.1, 2))
    temp = str(round(35 + random.random()*0.8, 2))
    turb = str(round(1500 + random.random()*10, 1))
    data = {"distance": dis, "ph": ph, "temp": temp, "turbidity": turb}
    
    # try:
    #     data = requests.get("http://192.168.0.100")

    # except Exception:
    #     time.sleep(2)
    #     getSensorData()

    # if (data.content != None):
    #     return json.loads(data.content)
    # else:
    #     return None
    return data


while True:
    data = getSensorData()
    if data != None :
        print(data)
        print("=====================")
        ref.child("data").set(data)
    else:
        pass    

    time.sleep(3.5)

    

    

