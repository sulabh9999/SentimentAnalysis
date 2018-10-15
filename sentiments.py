#!/usr/bin/env python
# coding: utf-8

# In[1]:


import wordcloud
import boto3
import re
import pprint
from nltk.tokenize import sent_tokenize
# %reload_ext autoreload


# In[2]:


import json
import os

config_file_path = os.environ['VIRTUAL_ENV'] + '/config.json'

with open(config_file_path) as f:
    config = json.load(f)
    # authentication 
    AWS_ACCESS_KEY = config['access_key']
    AWS_SECRET_ACCESS_KEY = config['secret_key']
    AWS_REGION = boto3.Session().region_name

    input_file_path = config['input_path']
    output_file_path = config['output_path']


# project data source file
from dataSource import getData
import pandas as pd

start_date = '27-09-2018'
end_date = '02-10-2018'
comment_list = getData(input_file_path, start_date, end_date)
print(comment_list.head(50))


