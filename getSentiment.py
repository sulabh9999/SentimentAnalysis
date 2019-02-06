import boto3
import json
import os


config_file_path = '/home/nawaz/.virtualenvs/AWSComp/config.json'##os.environ['V_ENV'] + '/config.json'
print('file path is:', config_file_path)
with open(config_file_path) as f:
    config = json.load(f)
    # authentication 
    AWS_ACCESS_KEY = config['access_key']
    AWS_SECRET_ACCESS_KEY = config['secret_key']
    AWS_REGION = boto3.Session().region_name

# configuration AWS
client_comprehend = boto3.client(
    'comprehend',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# return sentiment per comment
def getSentiment(text):
    response_sentiment = client_comprehend.detect_sentiment(
        Text=text,
        LanguageCode='en'
    )
    sentimentScore = response_sentiment['SentimentScore']['Negative'] 
    return sentimentScore

# if __name__ == '__main__':
#     print('....AWS configured....')
#     config()