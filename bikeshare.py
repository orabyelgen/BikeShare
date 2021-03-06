import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cities = ['chicago', 'new york city', 'washington']

    # TO DO: get user input for month (all, january, february, ... , june)

    months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
    
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    
    while True:
        city = input("Enter Your City >>")
        if city not in cities:
           print("Not valid input")
           continue
        else:
            break
    
    
    while True:
        month = input("Enter Your Month >>")
        if month not in months:
           print("Not valid input")
           continue
        else:
            break
    
    while True:
        day = input("Enter Your Day >>")
        if day.title() not in days:
           print("Not valid input")
           continue
        else:
            break     
        
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

    # load data file into a dataframe
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
    print("The most common month: ",df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("The most common day of week: ",df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour: ",df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station: ",df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most common End Station: ",df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination Station'] = df['Start Station'] + df['End Station']
    print("The most common combination of start station and end station: ",df['Combination Station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['hour'] = df['Start Time'].dt.hour
    print("Total travel time: " , df['hour'].sum()," Hours")

    # TO DO: display mean travel time
    print("Average travel time: " ,df['hour'].mean(), " Hour")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types: " , len(user_types))
    

    # TO DO: Display counts of gender
    print("Counts of user types: " , df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print("Earliest, most recent, and most common year of birth: ",df['Birth Year'].max())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?:").lower()
    start_loc = 0
    while view_data == 'yes':
           end = start_loc + 5
           print(df.iloc[start_loc : end])
           start_loc += 5
           view_data = input(" Do you want to see the next 5 rows of data?:").lower()
           
            
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
