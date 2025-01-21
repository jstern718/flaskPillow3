import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

from lists.mainList import mainList
from lists.mostPopularList import mostPopularList
from lists.thinList import thinList
from lists.coolingList import coolingList
from lists.memoryFoamList import memoryFoamList
from lists.shreddedFoamList import shreddedFoamList
from lists.pillowcaseList import pillowcaseList
from lists.dealsList import dealsList

from text.mostPopularText import mostPopularText
from text.thinText import thinText
from text.coolingText import coolingText
from text.memoryFoamText import memoryFoamText
from text.shreddedFoamText import shreddedFoamText
from text.pillowcaseText import pillowcaseText
from text.dealsText import dealsText



@app.route("/")
def main():

    return render_template('main.html',
                            mainList = mainList,
                            pageTitle="Pillowsmith - The Best Pillows",
                            pageDescription="The best pillows for every type of sleeper.")


@app.route("/most-popular")
def most_popular():

    return render_template('page_template.html',
                            pillowList = mostPopularList,
                            pageText = mostPopularText,
                            pageTitle="The Most Popular Pillows",
                            pageDescription="Find out what pillows other people like the best.",
                            type="pillow")



@app.route("/cooling")
def cooling():

    return render_template('page_template.html',
                            pillowList = coolingList,
                            pageText = coolingText,
                            pageTitle="The Best Cooling Pillows",
                            pageDescription="The best pillows for people who sleep hot.",
                            chartImage = "static/assets/cooling-chart.png",
                            type="pillow")


@app.route("/thin")
def thin():

    return render_template('page_template.html',
                            pillowList = thinList,
                            pageText = thinText,
                            pageTitle="The Best Thin Pillows",
                            pageDescription="The best low profile pillows for people who sleep on their stomach.",
                            type="pillow")


@app.route("/memory-foam")
def memory_foam():

    return render_template('page_template.html',
                            pillowList = memoryFoamList,
                            pageText = memoryFoamText,
                            pageTitle="The Best Memory Foam Pillows",
                            pageDescription="The best pillows for people who like a warm cushiony feel.",
                            chartImage = "static/assets/foam-chart.webp",
                            type="pillow")


@app.route("/shredded-foam")
def shredded_foam():

    return render_template('page_template.html',
                            pillowList = shreddedFoamList,
                            pageText = shreddedFoamText,
                            pageTitle="The Best Shredded Foam Pillows",
                            pageDescription="The best pillows for people who want memory foam without the warmth.",
                            chartImage = "static/assets/foam-chart.webp",
                            type="pillow")


@app.route("/pillowcases")
def pillowcases():

    return render_template('page_template.html',
                            pillowList = pillowcaseList,
                            pageText = pillowcaseText,
                            pageTitle="The Best Pillowcases",
                            pageDescription="The best pillowcases for every type of pillow.",
                            type="pillow")


@app.route("/deals")
def deals():

    return render_template('page_template.html',
                            pillowList = dealsList,
                            pageText = dealsText,
                            pageTitle="Deals on Pillows We Love",
                            pageDescription="The best deals available now.",
                            type="post")


@app.route("/mobile-nav")
def mobile_nav():

    return render_template('mobile_nav.html',
                           pageTitle="Pillowsmith - Mobile Navigation",
                           pageDescription="The best pillows for every type of sleeper.")


@app.route("/sitemap.xml")
def sitemap():

    return send_from_directory(app.root_path, 'sitemap.xml')