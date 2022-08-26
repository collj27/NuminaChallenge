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

Download data.csv from https://numina-take-home-interview.s3.us-east-2.amazonaws.com/data.csv. Open "/api/utils.py" and update the "file" variable in the "fetch_csv()" method to point to your local system.

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

### Requesting data from the api

To request the volume of a given class, replace <class> with a valid object (i.e. pedestrian) and run the following command in terminal:
 
- curl --request GET \
--header "Accept:application/json" \
--header "Content-Type: application/json" \
http://127.0.0.1:5000/volume/<class>

To request the track points for a given track id, replace <trackid> and run the following in terminal:
- curl --request GET \
--header "Accept:application/json" \
--header "Content-Type: application/json" \
http://127.0.0.1:5000/detections/<trackid>

### Starting the web server

In another terminal window, navigate to the "/client" subfolder and run:
- npm start

### Viewing the client

If started successfully, you can view the client at http://localhost:3000/. You should see the JSON API responses for the pedestrian volume and bicycle volume.

All api requests will be proxied to http://localhost:5000/. If you use a different port for your flask server, make sure to update "proxy" in package.json.


## Next Steps


### Troubleshoot AWS S3 Download

I attempted to fetch the csv file from s3 using boto3. I received some permissions errors and opted to read the file from my local filesystem rather than wasting too much time wrestling with it.

### Troublshoot Docker Container

I tried following this tutorial to setup a docker container: https://betterprogramming.pub/how-to-dockerize-your-flask-api-cc95843ab625

Unfortunately, whenever I run the image, the container immediately dies with no error logs. With more time, I would have started by looking for a solution here: https://www.tutorialworks.com/why-containers-stop

### Create Line Graph
With more time, I would've followed this tutorial to setup the line graph of the cumulative sum of pedestrians: https://www.geeksforgeeks.org/create-a-line-chart-using-recharts-in-reactjs/
 
 
### Restructure Front End
 
App.js can be broken into more modular components. Rather than having two API calls in the useEffect hook, there could be two child components (one for bicycle volume and one for pedestrian) that call the API and return the data to be rendered by a parent component.
 
### Add Defensive Code
 
Currently, there are no validity checks for class types and track ids. Error messages for invalid inputs should be added to help debugging and improve user experience. 
 
