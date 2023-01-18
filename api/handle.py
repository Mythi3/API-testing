# Made by Mythi3
# https://github.com/Mythi3

import json
import random
import string
from flask import Flask, jsonify
from datetime import datetime
from datetime import date

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

class handle():
    
    def __init__(self):
        self.time_now = datetime.now();self.time_now = self.time_now.strftime("%H:%M:%S | %d/%m/%Y ")
    
    def log(ip,useragent,path,method,data,response):
        #characters possible to generate id
        all_chars = list(string.ascii_letters + string.digits)
        #time stuff
        time_now = datetime.now();formatted = time_now.strftime("%H:%M:%S | %d/%m/%Y ")
        time = time_now.strftime('%H:%M:%S')
        date = time_now.strftime('%d/%m/%Y')
        #create a request id
        request_id = ''.join(random.choices(all_chars, k=12))

        # Load the existing JSON array file and check for duplicate ray ids
        with open("data/logs.json", "r") as json_file:
            arrays_list = json.load(json_file)

            #check if id is used before (need a way of doing more then once because it might be regen wrong)
            for json_object in json_file:
                if json_object["id"] == request_id:
                    request_id = ''.join(random.choices(all_chars, k=12))

        try:
            data = data.decode("utf-8").strip()
        except:
            #lol
            one = 1
        if data == "" or data == "ImmutableMultiDict([])":
            data="None"
        
        #create the json data
        json_format = {
            "request_id": request_id,
            "time": formatted,
            "response": response,
            "ip": ip,
            "User_agent": useragent,
            "method": method,
            "data": data,
            "path": path
        }

        # Append the loaded JSON object to the list
        arrays_list.append(json_format)

        # Write the entire list to the same file
        with open("data/logs.json", "w") as json_file:
            json.dump(arrays_list, json_file)

        print(f"{time}{ENDC} | {date}{ENDC} | Request Response Code:{ENDC} {response}{ENDC} | Request ID:{ENDC} {request_id} | Request User Agent: {useragent} | Request ip:{ENDC} {ip}{ENDC} | Request Method:{ENDC} {method}{ENDC} | Request Data Recieved:{ENDC} {data}{ENDC} | Request Path:{ENDC} {path}{ENDC}")
