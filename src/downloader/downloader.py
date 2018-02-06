import os
import urllib2
import zipfile

#Pull information from the commit and fill the communication object with relevant info

def push_event(data, communication):
    owner = data["repository"]["owner"]["login"]
    repo = data["repository"]["name"]
    sha = data["head_commit"]["id"]
    communication.author = owner
    communication.commit = sha
    communication.url_repo = "https://www.github.com"
    communication.repository = repo
    download_commit(communication)

def download_commit(communication):
    url = "/".join([communication.url_repo, communication.author, communication.repository, "archive",
                    communication.commit + ".zip"])

    filename = ''.join(sha)
    output = os.path.basename("/".join([filename + ".zip"]))

    response = urllib2.urlopen(url)

    with open(output, 'wb') as local_file:
        local_file.write(response.read())

    with zipfile.ZipFile(output, 'r') as zip_file:
        zip_file.extractall(filename)
        zip_file.close()

    os.remove(output)

    communication.location = "/".join([filename, communication.repository + "-" + communication.commit])
    communication.url = url
