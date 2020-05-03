# -*- coding: utf-8 -*-
"""
Created on Fri May  1 15:48:07 2020

@author: lenovo
"""


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Enter input city(chicago, new york city, washington):').lower()
        if  city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Invalid city, please enter again!')

        


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter month(january,february,...), "all" to apply no month filter:').lower()
        if  month.title() in list(calendar.month_name)[1:]:
            break
        else:
            print('Invalid month, please enter again!')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter day of week (monday,tuesday,...), "all" to apply no day filter:').lower()
        if  day.title() in list(calendar.day_name):
            break
        else:
            print('Invalid day, please enter again!')

    print('-'*40)
    return city, month, day


city, month, day = get_filters()



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



df = load_data(city, month, day)






while True:
        try:
            x = (input('Enter input city(chicago, new york city, washington):')
        except ValueError:
            print('Not a valid city!')
    
    
    
try: x = int(input('Enter input city(chicago, new york city, washington):'))





except ValueError:
    print('Not a valid city!')
    
    
    
try: 
    x = int(input('Enter input city(chicago, new york city, washington):'))
except:
    print('Not valid')