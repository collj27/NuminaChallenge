from flask import Flask
import pandas as pd

app = Flask(__name__)

# DOcker https://www.tutorialworks.com/why-containers-stop/

def fetch_csv():
    """
    Ran into permissions issues when attempting to download from s3 and opted to read csv locally due to time constraints
    """
    #file_name = "data.csv"
    #s3 = boto3.resource('s3')
    #output = f"downloads/{file_name}"
    #bucket = "numina-take-home-interview.s3.us-east-2.amazonaws.com"
    #s3.Bucket(bucket).download_file(file_name, output)

    file = "/Users/james/downloads/data.csv"
    df = pd.read_csv(file)


    return df


def get_hour_interval(x):
    return int(x[:2])

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/volume/<detected_class>')
def get_volume_by_detected_class(detected_class):

    # fetch data and filter by needed columns
    df = fetch_csv().filter(items=['trackid', 'class', 'time'])

    # filter data by object class
    class_df = df[df['class'] == detected_class]

    # get hour interval from time
    class_df['hour'] = class_df['time'].apply(get_hour_interval)

    # drop columns and get unique track ids for given hour
    volume_df = class_df.drop(columns=['time', 'class'])
    volume_df = volume_df.groupby(['hour']).nunique()

    return volume_df.to_json()

@app.route('/detections/<trackid>')
def get_detections_by_track_id(track_id):
    df = fetch_csv()

    return df[df['trackid'] == track_id].to_json()







