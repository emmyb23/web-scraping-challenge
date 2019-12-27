from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_scrape_app"
mongo+ PyMongo(app)

@app.route("/")
def index():
    data = mongo.db.mars_scrape_app.find_one()

    return render_template("index.html", mars_scrape_app=mars_scrape_app)


@app.route("/scrape")
def scrape():
    mars_scrape_app = scrape_mars.scrape()
    mongo.db.mars_scrape_app.update({}, mars_scrape_app, upsert=True)
    return "DONE"



if __name__ == "__main__":
    app.run(debug=True)