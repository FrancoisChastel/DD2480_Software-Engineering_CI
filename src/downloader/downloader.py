import os
import zipfile

import urllib2


def push_event(data, communication):
    """
    function that allows you to hold a push_event with a useful json
    :param data: a dictionary that holds all the revelant information (please see API.md)
    :param communication: communication-object (see communication.py) that can hold all the information about the process
    :return: N/A
    """
    owner = data["repository"]["owner"]["login"]
    repo = data["repository"]["name"]
    sha = data["head_commit"]["id"]
    author = data["head_commit"]["author"]["username"]
    communication.owner = owner
    communication.author = author
    communication.commit = sha
    communication.url_repo = "https://www.github.com"
    communication.repository = repo
    download_commit(communication)

def download_commit(communication):
    """
    Download the zip of the commit concerned by the testing/compiling process and unzip it
    :param communication: communication-object (see communication.py) that can hold all the information about the process
    :return: N/A
    """
    communication.url_repo = "/".join(
        [communication.url_repo, communication.owner, communication.repository, "archive",
         communication.commit + ".zip"])

    filename = ''.join(communication.commit)
    output = os.path.basename("/".join([filename + ".zip"]))

    response = urllib2.urlopen(communication.url_repo)

    with open(output, 'wb') as local_file:
        local_file.write(response.read())

    with zipfile.ZipFile(output, 'r') as zip_file:
        zip_file.extractall(filename)
        zip_file.close()

    os.remove(output)

    communication.location = "/".join([filename, communication.repository + "-" + communication.commit])
