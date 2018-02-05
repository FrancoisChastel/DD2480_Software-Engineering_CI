import os
import urllib2
import zipfile


def push_event(data, communication):
    owner = data["repository"]["owner"]["login"]
    repo = data["repository"]["name"]
    sha = data["head_commit"]["id"]
    communication.author = owner
    communication.commit = sha

    download_commit(communication, repository=repo, repository_owner=owner, sha=sha)


def download_commit(communication,
                    repository,
                    repository_owner,
                    sha,
                    based_url="https://www.github.com",
                    directory="downloads"):
    url = "/".join([based_url, repository_owner, repository, "archive", sha + ".zip"])
    filename = ''.join(sha)
    output = os.path.basename("/".join([filename + ".zip"]))

    response = urllib2.urlopen(url)

    with open(output, 'wb') as file:
        file.write(response.read())

    with zipfile.ZipFile(output, 'r') as zip_file:
        zip_file.extractall(filename)
        zip_file.close()

    os.remove(output)

    communication.location = "/".join([filename, repository + "-" + sha])
    communication.url = url
