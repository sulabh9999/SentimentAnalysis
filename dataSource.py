import pandas as pd


def getData(input_file_path):
    input_file = input_file_path
    df = pd.read_csv(input_file, sep='\t', usecols=['Name', 'Comment'])
    return df['Comment'].values

