import os
import time
import pandas as pd
import numpy as np
import calendar
import time

os.chdir('C:/Users/lenovo/Python learn/Python Data Science NanodegreeProject/udacity_python_bikeshare_project-master/')

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Enter input city(chicago, new york city, washington):').lower()
        if  city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Invalid city, please enter again!')

        


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter month(january,february,...) or "all" to apply no month filter:').lower()
        if  month.title() in (['All']+list(calendar.month_name)[1:]):
            break
        else:
            print('Invalid month, please enter again!')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter day of week (monday,tuesday,...) or "all" to apply no day filter:').lower()
        if  day.title() in (['All']+list(calendar.day_name)):
            break
        else:
            print('Invalid day, please enter again!')

    print('-'*40)
    return city, month, day


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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    # find the most popular month
    popular_month = list(calendar.month_name)[df['month'].mode()[0]]
    
    print('Most Popular month:', popular_month)

    # TO DO: display the most common day of week
    # find the most popular day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    
    print('Most Popular day of week:', popular_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    pop_ststation = df['Start Station'].mode()[0]
    print('Most Popular Start station:', pop_ststation)


    # TO DO: display most commonly used end station

    pop_endstation = df['End Station'].mode()[0]
    print('Most Popular End station:', pop_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    
    df['station_combination'] = df['Start Station']+' AND '+df['End Station']

    # find the most popular hour
    popular_stcombo = df['station_combination'].mode()[0]
    
    print('Most Popular Station Combination:', popular_stcombo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    print('Total trip duration : {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    
    print('Mean trip duration : {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Count of user types: ')
    print(df['User Type'].value_counts())

    #Don't do in washington as data for gender and birth yer not available
    if city.lower() == 'washington':
        print('\nGender and datebirth data for Washington not available. Sorry!')
        return
    
    # TO DO: Display counts of gender
    print('\nCount of Gender: ')
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nMost recent year of birth: {}'.format(df['Birth Year'].max()))
    print('Most earliest year of birth: {}'.format(df['Birth Year'].min()))
    print('Most common year of birth: {}'.format(df['Birth Year'].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    '''Displays 5 lines of raw data'''
    iterator = (num for num in range(0,len(df),5))
    
    prompt = input('\nWant to see 5 lines of raw data? Enter yes or no.\n').lower()
    while prompt == 'yes':
        it_val = next(iterator)
        print(df.iloc[it_val:it_val+5,:])
        prompt = input('\nWant to see more 5 lines of raw data? Enter yes or no.\n').lower()
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print('Generating Stats --------- \n')
        time.sleep(2)
        time_stats(df)
        
        time.sleep(2)
        station_stats(df)
        
        time.sleep(2)
        trip_duration_stats(df)
        
        time.sleep(2)
        user_stats(df,city)

        time.sleep(2)
        view_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
