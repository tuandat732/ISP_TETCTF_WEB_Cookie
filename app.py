from flask import Flask, render_template, request, make_response, flash, redirect
import urllib.parse as urlparse
from urllib.parse import parse_qs
from http import cookies
app = Flask(__name__)



@app.route('/')
def index():
   
    flag="C00ki3_1s_v3ry_d3l1c10u5<3"
    resp = make_response(render_template('index.html'))
    if(request.cookies != {}):
      if(request.cookies['role'] == '21232f297a57a5a743894a0e4a801fc3'):
        return render_template('index.html',flag=flag)
    resp.set_cookie('role', 'ee11cbb19052e40b07aac0ca060c23ee' )
    return resp


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 