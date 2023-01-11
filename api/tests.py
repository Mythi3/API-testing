# Made by Mythi3
# https://github.com/Mythi3

from flask import Flask,jsonify

def main(path,status_code,method,data,total,get_num,post_num):
    '''Handler for /test path'''
    print(path)
    print(method)
    print(data)
    data = data.decode("utf-8").strip()
    if path == "/test":
        if data == "" or data == "ImmutableMultiDict([])":
            data="None"

        return jsonify(
            response=status_code,
            data=data,
            method=method,
            req_number=total,
            get_num=get_num,
            post_num=post_num
        )
