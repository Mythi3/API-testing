import re
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def site_map():
    routes = []
    
    for rule in app.url_map.iter_rules():
        routes.append('%s' % rule)
    
    return routes

if __name__ == '__main__':
    app.run(debug=True) # can use host='127.0.0.1' and port=5000
