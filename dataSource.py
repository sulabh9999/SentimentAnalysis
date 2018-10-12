import pandas as pd


def getData(input_file_path):
    input_file = input_file_path
    #print('---input_file_path--', input_file_path)
    df = pd.read_csv(input_file, sep='\t', usecols=['comments', 'ratings', 'dates'])
    return df

