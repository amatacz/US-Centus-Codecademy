import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob


#glob.glob() <- let upload multiple csv files
all_csv = glob.glob('states*.csv')

#creating empty list of dataframes
df_list = []

# for every csv file in all_csv (uploaded files using glob) -> save each csv file in df variable -> add df to the df_list
for csv in all_csv:
  df = pd.read_csv(csv)
  df_list.append(df)

# pd.concat(list) -> lets connect every df from df_list into one big DataFrame
us_census = pd.concat(df_list)

# inspecting columns, types and first 5 rows of us_census DataFrame
print(us_census.columns)
print(us_census.dtypes)
print(us_census.head())

# str.replace() -> using regex, replace dollar sign with no sign (removing it) and this data (without $), convert object to the float (pd.to_numeric)
us_census['Income'] = pd.to_numeric(us_census['Income'].str.replace('[\$]', ''))

# split string from GenderPop column, on '_'(underscore) place. Expand=True , the split elements will expand out into separate columns. And save it in variable
genderpop_splitted = us_census['GenderPop'].str.split('_', expand=True)

# str.replace() -> pick first[0] or second[1] part of genderpop_splitted, using regex, replace sex sign(M/F) with no sign (removing it) and this data (without M/F), convert object to the float (pd.to_numeric)
us_census['Men'] = pd.to_numeric(genderpop_splitted[0].replace('[M]', '', regex=True))
us_census['Women'] = pd.to_numeric(genderpop_splitted[1].replace('[F]', '', regex=True))

# us_census.loc[] <- reference to certain cells from DataFrame, in this case "[:(<- everything) "us_census.columns != 'GenderPop'](<- every column, which is not (!=) 'GenderPop')" 
us_census = us_census.loc[:, us_census.columns != 'GenderPop']

# creating sccater plot with Women value on x and Income value on y / plt.show() displays plot
plt.scatter(us_census['Women'], us_census['Income'])
plt.show()

# .fillna() fills every NaN value with value from brackets - in this case difference between Total Population and Men Population
us_census['Women'] = us_census['Women'].fillna((us_census['TotalPop'] - us_census['Men']))

# .drop_duplicates() <- removes duplicated rows
us_census = us_census.drop_duplicates()

# same as in 40'
plt.scatter(us_census['Women'], us_census['Income'])
plt.show()

# replacing "%" with no sign, converting it to the numeric data type and filling Nan with 0
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
