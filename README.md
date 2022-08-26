# NuminaChallenge

## Technology Used
- python 3.8.10
- pip 19.0.3 
- flask 2.2.2
- npm 6.14.14
- node 14.17.5
- macOS Monterey 12.5.1
- PyCharm 2022.2.1 

## Setup

### Cloning the repo
First, clone the repository: git clone https://github.com/collj27/NuminaChallenge.git

### Installing API packages
In a terminal window, navigate to the "/api" subfolder, create a virtual environment, and install the required packages with:
 - pip install -r requirements.txt

### Installing client packages
Navigate to the "/client" subfolder and run:
- npm i
 
### Starting the Flask server

In a terminal window, navigate to the "/client" subfolder and run:
-  npm run start-api

This will run the "start-api" script located in package.json. Alternatively, you can navigate to the "/api" subfolder and run:
- flask run

### Starting the web server

In another terminal window, navigate to the "/client" subfolder and run:
- npm start

### Viewing the client

If started successfully, you can view the client at http://localhost:3000/. You should see the JSON API responses for the pedestrian volume and bicycle volume.

All api requests will be proxied to http://localhost:5000/. If you use a different port for your flask server, make sure to update "proxy" in package.json.


## Next Steps

Fix Docker
Line graph - pick library
Use observables/promises; restructure front end
