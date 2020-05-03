import os
os.chdir('C:/Users/lenovo/Python learn/Python Data Science NanodegreeProject/udacity_python_bikeshare_project-master/')


import pandas as pd

df = pd.read_csv("chicago.csv")
print(df.head(2))  # start by viewing the first few rows of the dataset!


pd.set_option('display.max_columns', 25)
pd.set_option('display.max_rows', 6)
pd.set_option('display.min_rows', 6)
pd.set_option('display.expand_frame_repr', True)

df.info()


###Practice Problem #1: Compute the Most Popular Start Hour

import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv('chicago.csv',parse_dates = True)

# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour

# find the most common hour (from 0 to 23)
popular_hour = df['hour'].mode()[0]
    
print('Most Frequent Start Hour:', popular_hour)


##################################################################

'''count user types'''



# print value counts for each user type
user_types = df['User Type'].value_counts()

print(user_types)


##################################################################

''' Filter the dataset'''

import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = 

    # extract month and day of week from Start Time to create new columns
    df['month'] = 
    df['day_of_week'] = 


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = 
    
        # filter by month to create the new dataframe
        df = 

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = 
    
    return df
    
df = load_data('chicago', 'march', 'friday')


