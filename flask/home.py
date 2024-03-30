from flask import Flask,render_template
from markdown import get_markdown_list
import mistune
import os
from path import *
app = Flask(__name__)



@app.route('/')
def hello():

    a,b = get_markdown_list('项目结构')
    return render_template('index.html', content=b[0])

if __name__ == '__main__':
    app.run(debug=True,port=5003,host='0.0.0.0')
