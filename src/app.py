# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

import logging
import os
from logging import Formatter, FileHandler

from flask import Flask
from github_webhook import Webhook

import communication
from compilation import compilation
from downloader import downloader

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
webhook = Webhook(app)


# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#

@app.route('/')
def home():
    return "Hello world!"


@webhook.hook()
def on_push(data):
    result = communication.Result()
    downloader.push_event(data, result)
    compilation.to_compile(result)

    return


@app.errorhandler(500)
def internal_error(error):
    return "Error 500", 500


@app.errorhandler(404)
def not_found_error(error):
    return "Error 404", 404


app.debug = True

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

def main():
    port = int(os.environ.get('PORT', 80))
    app.run(port=port)


# Or specify port manual:
if __name__ == "__main__":
    main()
