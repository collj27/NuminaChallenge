import pandas as pd


def fetch_csv():
    """
    Ran into permissions issues when attempting to download from s3 and opted to read csv locally due to time constraints
    Removed bucket name since repo is public
    """
    # file_name = "data.csv"
    # s3 = boto3.resource('s3')
    # output = f"downloads/{file_name}"
    # bucket = ""
    # s3.Bucket(bucket).download_file(file_name, output)

    file = "/Users/james/downloads/data.csv"
    df = pd.read_csv(file)

    return df


# get first two characters of time string and convert to int
def get_hour_interval(x):
    return int(x[:2])
