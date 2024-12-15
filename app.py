import os
from flask import Flask, render_template

app = Flask(__name__)
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

from lists.thinList import thinList
from text.thinText import thinText
print ("thinText", thinText)

# @app.route("/")
# def index():
#   return "Hello World!"


# @app.route("/sidebar")
# def sidebar():
#     return render_template('sidebar.html', isNavOpen=False, pillowList=thin)


@app.route("/thin")
def thin():
    return render_template('page_template.html',
                            isNavOpen=False,
                            pillowList = thinList,
                            pageText = thinText,
                            pageTitle="The Best Thin Pillows")