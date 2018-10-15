import pandas as pd
from datetime import datetime

# return dataframe between given dates
def getData(file_Path, start_date=None, end_date=None):
    df = pd.read_csv(file_Path, sep='\t', usecols=['comments', 'ratings', 'dates']) 

    if (start_date and end_date) is not None:
        df['formatedDate']=pd.to_datetime(df['dates'])
#         print('...datw..', df['formatedDate'])
        df.sort_values(by=['formatedDate'], ascending=True, inplace=True)
        dateField = df['formatedDate']
        start = datetime.strptime(start_date, '%d-%m-%Y') 
        end = datetime.strptime(end_date, '%d-%m-%Y')
        df = df.loc[(dateField>=start) & (dateField<=end)]
    return df


    