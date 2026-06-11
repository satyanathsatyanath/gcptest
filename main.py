from flask import Flask, render_template, request
import os   
app = Flask(__name__)

@app.route('/') 
def hello():
    return "Hello, World! of Satya"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
