from flask import Flask
from utils import fetch_csv, get_hour_interval

app = Flask(__name__)


@app.route('/volume/<detected_class>')
def get_volume_by_detected_class(detected_class):

    # fetch data and filter dataframe by needed columns
    df = fetch_csv().filter(items=['trackid', 'class', 'time'])

    # filter data by object class
    class_df = df[df.loc[:, 'class'] == detected_class]

    # get hour interval from time
    class_df.loc[:, 'hour'] = class_df.loc[:, 'time'].apply(get_hour_interval)

    # drop columns and get unique track ids for given hour
    volume_df = class_df.drop(columns=['time', 'class'])
    volume_df = volume_df.groupby('hour', as_index=False).nunique().cumsum().rename(columns={"trackid": "volume"})

    return volume_df.to_json(orient='records')


@app.route('/detections/<track_id>')
def get_detections_by_track_id(track_id):
    df = fetch_csv()
    return df[df.loc[:, 'trackid'] == track_id].to_json()







