# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
__name__ = "Github-CI"

from github_webhook import Webhook
from flask import Flask, render_template, request
import logging
from logging import Formatter, FileHandler
import os

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
webhook = Webhook(app)

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#

@app.route('/')
def home():
    return "Hello world!"


@webhook.hook()
def on_push(data):
    print("Got push with: {0}".format(data))
    return


@app.errorhandler(500)
def internal_error(error):
    return "Error 500", 500


@app.errorhandler(404)
def not_found_error(error):
    return "Error 404", 404


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#

# Or specify port manually:
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
