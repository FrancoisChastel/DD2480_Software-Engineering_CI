#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

import logging
import os
import argparse
from logging import Formatter, FileHandler

import pytest
from flask import Flask
from github_webhook import Webhook

from communication import communication
from compilation import compilation
from downloader import downloader
from notification import notification
from testing import testing

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
    testing.to_test(result)

    notification.send_notifications(result)

    return "Check your e-mail to get the result of the CI", 200


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


def test():
    arg = ["src/test_ci.py"]
    pytest.main(args=arg)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Launch a CI that catch the GitHub webhook (see README).')
    parser.add_argument('--test', help='execute the test of the CI',
                        dest='testing', action='store_true', default=False)
    parser.add_argument('--run', help='run the CI',
                        dest='running', action='store_true', default=False)

    args = parser.parse_args()

    if args.running and not args.testing:
        main()
    elif args.testing and not args.running:
        test()
    elif not args.testing and not args.running:
        print ("ERROR - please try --help")
    else:
        print ("ERROR - You need to chose between running and testing")

