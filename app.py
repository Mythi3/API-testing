# Made by Mythi3
# https://github.com/Mythi3

import re,json
from flask import Flask,jsonify,request

#local imports
from api.tests import main as run_test

#varibles
f = open("/data/data.json","f")
total_reqs = 0
get_req = 0
post_req = 0

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def site_map():
    routes = []
    
    for rule in app.url_map.iter_rules():
        routes.append('%s' % rule)
    
    return routes

@app.route("/test", methods=["GET","POST"])
def test():
    global total_reqs;global get_req;global post_req;method=request.method;total_reqs+=1;status = 200;data = request.data.decode("utf-8").strip();
    
    if method=="GET": get_req += 1
    if method == "POST": post_req +=1
    output = run_test("/test",status_code=status,method=method,data=request.data,total=total_reqs,get_num=get_req,post_num=post_req)
    return output

if __name__ == '__main__':
    app.run(debug=True) # can use host='127.0.0.1' and port=5000
