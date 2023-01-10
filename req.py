import requests,os

def post(data=None):
    req=requests.post('http://localhost:5000/', data=data)
    
    
post(data=None)
