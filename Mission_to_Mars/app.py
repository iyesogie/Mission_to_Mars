
from flask import Flask, render_template, redirect
from pymongo import MongoClient
from flask_pymongo import PyMongo
from . import scrape_mars
client = MongoClient()

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


mars = mongo.mars.find_one()
# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    mars = mongo.mars.find_one()
    return render_template("Mission_to_Mars/template/index.html", mars=mars)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():


#@main.route('/')
#def index():
    #return redirect(url_for('main.home'))

 
    mars_data = scrape.scrape_all()
    scrape.update({}, mars_data, upsert=True)
    return "Scraping Successful"


if __name__ == "__main__":
    app.run(debug=True)