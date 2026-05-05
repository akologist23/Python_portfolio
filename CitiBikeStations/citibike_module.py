import requests
import pprint
import json

class CitiBike:
    def __init__(self):
        self.url = "https://gbfs.citibikenyc.com/gbfs/en/station_information.json"

    def retrieve_data(self):     
        response = requests.get(self.url)
        data = response.json()
        #pprint.pprint(data)
        # for (key, value) in data["data"].items():
        #     print(key)
        print(data["data"]["stations"])
        
        if data["data"]["stations"]:
            return data["data"]["stations"]
        
        else:
            data = json.load(open("station_info.json"))
            return data["data"]["stations"]


bike = CitiBike()
print(bike.retrieve_data())