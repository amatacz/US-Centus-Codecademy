import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

all_csv = glob.glob('states*.csv')
df_list = []

for csv in all_csv:
  df = pd.read_csv(csv)
  df_list.append(df)

us_census = pd.concat(df_list)

print(us_census.columns)
print(us_census.dtypes)
print(us_census.head())

us_census['Income'] = us_census['Income'].str.replace('[\$]', '')
gender_splitted = us_census['GenderPop'].str.split('_', expand=True)
us_census['Men'] = pd.to_numeric(gender_splitted[0].replace('[M]', '', regex=True))
us_census['Women'] = pd.to_numeric(gender_splitted[1].replace('[F]', '', regex=True))

us_census = us_census.loc[:, us_census.columns != 'GenderPop']

plt.scatter(us_census['Women'], us_census['Income'])
plt.show()

us_census['Women'] = us_census['Women'].fillna((us_census['TotalPop'] - us_census['Men']))

us_census = us_census.drop_duplicates()

plt.scatter(us_census['Women'], us_census['Income'])
plt.show()

us_census['Hispanic'] = pd.to_numeric(us_census['Hispanic'].str.replace('[%]', '')).fillna(0)
us_census['White'] = pd.to_numeric(us_census['White'].str.replace('[%]', '')).fillna(0)
us_census['Black'] = pd.to_numeric(us_census['Black'].str.replace('[%]', '')).fillna(0)
us_census['Native'] = pd.to_numeric(us_census['Native'].str.replace('[%]', '')).fillna(0)
us_census['Asian'] = pd.to_numeric(us_census['Asian'].str.replace('[%]', '')).fillna(0)
us_census['Pacific'] = pd.to_numeric(us_census['Pacific'].str.replace('[%]', '')).fillna(0)

us_census.hist(column='Hispanic');
plt.show()
us_census.hist(column='White');
plt.show()
us_census.hist(column='Black');
plt.show()
us_census.hist(column='Native');
plt.show()
us_census.hist(column='Asian');
plt.show()
us_census.hist(column='Pacific');
plt.show()