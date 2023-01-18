# Made by Mythi3
# https://github.com/Mythi3

import re,json
from flask import Flask,jsonify,request,render_template
import plotly
import plotly.graph_objects as go

#local imports
from api.tests import main as run_test
from api.handle import handle as handle

#varibles
f = open("data/data.json")
total_reqs = 0
get_req = 0
post_req = 0


#templates

#--log request--#
# ua=request.headers.get('User-Agent');data = request.data.decode("utf-8").strip();handle.log(request.remote_addr,ua,"/test",request.method,data,200)


app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def site_map():
    routes = []

    for rule in app.url_map.iter_rules():
        routes.append('%s' % rule)

    #remove static
    for route in routes:
        if route == "/static/<path:filename>":
            routes.remove(route)

    return routes

@app.route("/test", methods=["GET","POST"])
def test():
    ua=request.headers.get('User-Agent');data = request.data.decode("utf-8").strip();handle.log(request.remote_addr,ua,"/test",request.method,data,200)
    global total_reqs;global get_req;global post_req;method=request.method;total_reqs+=1;status = 200;data = request.data.decode("utf-8").strip();
    if method=="GET": get_req += 1
    if method == "POST": post_req +=1
    output = run_test("/test",status_code=status,method=method,data=request.data,total=total_reqs,get_num=get_req,post_num=post_req)
    return output

@app.route('/graph', methods=['GET', 'POST'])
def graph():
    ua=request.headers.get('User-Agent');data = data = request.get_json().strip();handle.log(request.remote_addr,ua,"/graph",request.method,data,200)
    data = request.get_json()
    x_values = data['x']
    y_values = data['y']

    fig = go.Figure(data=go.Scatter(x=x_values, y=y_values))
    fig.update_layout(title='JSON Data as Graph', xaxis_title='X-Values', yaxis_title='Y-Values')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('graph.html', graphJSON=graphJSON)



if __name__ == '__main__':
    app.run(host='95.179.193.118',port=5000,debug=True) # can use host='127.0.0.1' and port=5000