from flask import Flask
import jinja2
import datetime
import os
from dotenv import load_dotenv
from flask import Flask,render_template,request
from pymongo import MongoClient
load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.getenv("MONGODB_URI"))
    app.db = client.microblog
    @app.route("/",methods=["GET","POST"])
    def home():
        if request.method=="POST":
            entry_content=request.form.get("content")
            formatted_date=datetime.datetime.today().strftime("%y-%m-%d")
            new_formatted_date=datetime.datetime.today().strftime("%b %d")
            app.db.Entries.insert_one({"content":entry_content,"date":formatted_date,"new_date":new_formatted_date})
        return render_template("home.html",entriess=app.db.Entries.find({}))
    return app