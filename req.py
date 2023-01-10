# Made by Mythi3
# https://github.com/Mythi3

import requests,os,time

def post(data=None):
    req=requests.post('http://localhost:5000/test', json=data)
    print(req.status_code)
    print(req.content)
def get():
    req=requests.get('http://localhost:5000/test')
    print(req.status_code)
    print(req.content) 
data={"test": "test"};method = input("Request or Post (g/p): ")

if method == "g":
    get()
if method == "p":
    post(data=data)
