import sys 
import os 
from flask import Flask, render_template 

  

  

if getattr(sys, 'frozen', False): 

    template_folder = os.path.join(sys._MEIPASS, 'templates') 
    static_folder = os.path.join(sys._MEIPASS, 'static') 

    print(template_folder) 
    print(static_folder) 

    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder) 

else: 

    app = Flask(__name__)

  

@app.route("/") 

def hello(): 

    return render_template("main.html") 

  

if __name__ == "__main__": 

    app.run(host='127.0.0.1', port=5000) 

