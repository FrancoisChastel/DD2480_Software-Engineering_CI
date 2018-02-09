# Minimal CI-Tools for python on Github
The goal of this assignment is to master the core of continuous integration. 
To achieve this goal, the students (us) are asked to implement a small continuous integration CI server. 
This CI server will only contain the core features of continuous integration. The features are all specified below.

## Main Features 
 * Run static analysis on a well-formed python project
 * Run test on a well-formed python project
 * E-Mail the result of the testing on a well-formed python project

## How to run it ?
We first checkout this repository:
```
https://github.com/FrancoisChastel/DD2480_Software-Engineering_CI.git
cd DD2480_Software-Engineering_CI
```

We then install the required dependencies:
```
brew install python
```

For linux user :
```
curl -LO --tlsv1 https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip 
```

For Mac user:
```
curl -LO --tlsv1 https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-386.zip
unzip ngrok-stable-darwin-386.zip
```

We then execute installing python and pip you can type in your terminal :
```
sudo make all
sudo make run
```
It will start a web server on localhost:5000.

We configure our Github repository:
* go to `Settings >> Webhooks`, click on `Add webhook`.
* paste the forwarding URL (eg `http://8929b010.ngrok.io`) in field `Payload URL`) and send click on `Add webhook`. In the simplest setting, nothing more is required.

You can now try to push on this repository :)

## How to Run Tests
Type into terminal 
```
sudo make all
sudo make test
```

## Quit the program
We shutdown everything:
* `Ctrl-C` in the ngrok terminal window
* `Ctrl-C` in the ngrok python window
* delete the webhook in the webhook configuration page.
* `make clean` in the directory `DD2480_Software-Engineering_CI`

## Languages
Python

## Authors
This project was developed by : 
 * François Chastel : francois@chastel.co
 * Anu Devarmanai : adevar2@illinois.edu
 * Brian Ritter : bmritt@gmail.com
 * Jiayu Sun : 
 
 ## Statement of Contributions
 * Feature #1 (Compilation) was done by François Chastel. 
 * Feature #2 (Testing) was done by Jiayu Sun and Anu Devarmanai. 
 * Feature #3 (Notification) was done by Brian Ritter. 
 
 ## Compilation Feature
 The complication feature was implemented using pylint in compilation.py. The compilation process is then tested in test_ci.py in the corresponding compilation unit tests. 
 
 ## Testing Feature
 The testing feature was implemented and tested using pytest in test_ci.py. 
 
 ## Notification Feature
 The notification feature has been implemented by sending an email to the email address DD2480.CI@gmail.com with the message body containing information about the compilation and testing results (specifically state of compilation/tests, Author of the commit, commit number, repo URL, and compiling messages). This feature was tested in test_ci.py in the corresponding unit test by checking if the email is sent correctly and contains the correct information. 
