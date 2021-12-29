# twitter-api-fastapi

#### Description:
twitter-api-fastapi is an api designed to query tweets and users available in a test database. This was developed to practice with FastAPI.

* Retrive, create and update all the users and tweets from the test database
* Retrive, create and update specific users and tweets from the test database

#### Environment:
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

#### Installation:
* Clone this repository: `git clone "git@github.com:Jaricapa-holberton/twitter-api-fastapi.git"`
* Access Hunty_Test: `cd twitter-api-fastapi`
* Create the virtual environment: `virtualenv venv`
* Activate virtualenv: `source venv/bin/activate`
* install dependencies: `pip install -r requirements.txt`
* install ngrok: `curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok`  
* Start a tunnel `ngrok http 8000`         
* Activate local server: `uvicorn main:app --reload`
* Open the web app in a browser: `http://127.0.0.1:8000/`

#### Examples of use:
interact with the application in the browser writing the necessary endpoints in the browser

#### Bugs:
No known bugs at this time. 

#### Authors:
Jaime Aricapa - [Github](https://github.com/Jaricapa-holberton)

#### License:
Public Domain. No copy write protection. 
