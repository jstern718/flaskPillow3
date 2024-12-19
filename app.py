import os
from flask import Flask, render_template, request

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

from text.mostPopularText import mostPopularText
from text.thinText import thinText
from text.coolingText import coolingText
from text.memoryFoamText import memoryFoamText
from text.shreddedFoamText import shreddedFoamText
from text.pillowcaseText import pillowcaseText


@app.route("/")
def main():

    return render_template('main.html',
                            mainList = mainList,
                            pageTitle="Main Page")


@app.route("/most-popular")
def most_popular():

    return render_template('page_template.html',
                            pillowList = mostPopularList,
                            pageText = mostPopularText,
                            pageTitle="The Best Most Popular Pillows")



@app.route("/cooling")
def cooling():

    return render_template('page_template.html',
                            pillowList = coolingList,
                            pageText = coolingText,
                            pageTitle="The Best Cooling Pillows",
                            chartImage = "static/assets/cooling-chart.png")


@app.route("/thin")
def thin():

    return render_template('page_template.html',
                            pillowList = thinList,
                            pageText = thinText,
                            pageTitle="The Best Thin Pillows",
                          )


@app.route("/memory-foam")
def memory_foam():

    return render_template('page_template.html',
                            pillowList = memoryFoamList,
                            pageText = memoryFoamText,
                            pageTitle="The Best Memory Foam Pillows")


@app.route("/shredded-foam")
def shredded_foam():

    return render_template('page_template.html',
                            pillowList = shreddedFoamList,
                            pageText = shreddedFoamText,
                            pageTitle="The Best Shredded Foam Pillows")


@app.route("/pillowcases")
def pillowcases():

    return render_template('page_template.html',
                            pillowList = pillowcaseList,
                            pageText = pillowcaseText,
                            pageTitle="The Best Pillowcases")


@app.route("/mobile-nav")
def mobile_nav():

    return render_template('mobile_nav.html',
                            pillowList = pillowcaseList,
                            pageText = pillowcaseText,
                            pageTitle="The Best Pillowcases")