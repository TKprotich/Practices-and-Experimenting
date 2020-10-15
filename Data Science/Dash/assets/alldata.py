import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from itertools import chain
from collections import Counter

import calendar


def filehandle(path, sheetname):
    fh = pd.read_excel(path, sheet_name = sheetname)
#     Age
    fh['Age'] = fh['AGE'].str.split(' ').str.get(0).astype(int)
    # Departements
    department = pd.read_excel(r"C:\Users\user\Downloads\oeh.medical.physician.xls")
    mydict = dict(zip(department['Name'].str.split(' ').str.get(-1), department['Speciality']))
    fh['Department'] = fh['DOCTOR'].str.split().str.get(-1)
    fh['Department'] = fh.Department.replace(mydict)
    fh['Department'] = fh.Department.replace('Abboud', 'Obstetrics & Gynecology')
    # Date handling
    fh['DATE'] = pd.to_datetime(fh.DATE)
    fh['month'] = fh['DATE'].apply(lambda x : x.month)
    fh['year'] = fh['DATE'].apply(lambda x: x.year)
    fh['month'] = fh['month'].apply(lambda x : calendar.month_abbr[x])
    return fh


def counttext(column):
    column = pd.Series(column).dropna()
    column = list(chain(*column))
    counter = Counter(column)
    return counter



def dgdmydict( fh, analyzecolumn, filtercolumn, filteritem, DELIMETER):
    fh1 = fh[fh[filtercolumn] == filteritem]
    return counttext(fh1[analyzecolumn].str.lower().str.split(DELIMETER))



def analyzenow(fh, analyzecolumn, filtercolumn, filteritem):
    if analyzecolumn == 'GENDER':
        DELIMETER = " "
    elif analyzecolumn == 'COMPLAIN':
        DELIMETER = " + "
    elif analyzecolumn == 'IMAGING':
        DELIMETER = ","
    elif analyzecolumn == 'INVESTIGATION':
        DELIMETER = ","
    elif analyzecolumn == 'DOCTOR':
        DELIMETER = ""
    newfh = fh[analyzecolumn].replace(' ', np.nan, inplace=True)
    newfh = fh[analyzecolumn].dropna(inplace=True)
    want = dgdmydict(fh, analyzecolumn, filtercolumn, filteritem, DELIMETER)
    thedict = dict(want.most_common())
    df = pd.DataFrame(want.most_common())
    df = df.rename(columns={0 : analyzecolumn, 1 : "Counts"})
    return df

opdfh = filehandle(r"C:\Users\user\Downloads\Out Patient Statistical Report (4).xlsx", "Report")





# Querying The diseases

dataframe1 = pd.DataFrame()

for i in opdfh.Department.unique():
    dataframe = analyzenow(opdfh, 'COMPLAIN', 'Department', i)
    try:
        dataframe['COMPLAIN'] = dataframe.COMPLAIN.str.capitalize().str.strip()
        
    except:
        print("try another")
        
    try:
        df = dataframe.query('COMPLAIN != "Follow up"').iloc[:3]
    except:
        df = dataframe.iloc[:3]
    df['metadata'] = i
    dataframe1 = dataframe1.append(df)


cols = ['metadata', 'COMPLAIN', 'Counts']

dataframe1[cols]