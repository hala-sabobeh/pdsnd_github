import time
import pandas as pd
import numpy as np
import statistics as stat

def get_city():
    """
    Prompt the user to enter a city name and validate the input.

    Returns:
        str: The validated city name.
    """
    cities = ['chicago', 'new_york_city', 'washington']
    while True:
        city = input("Enter the city you like to explore (chicago, new_york_city, washington): ").lower()
        if city in cities:
            return city
        print(f'Data for {city} is not available. Please choose from {cities}.')

def get_month():
    """
    Prompt the user to enter a month or 'all' and validate the input.

    Returns:
        list: A list containing the selected month(s).
    """
    months = ['all', 'jan', 'feb', 'mar', 'apr', 'may', 'jun']
    while True:
        month = input("Enter the month (Jan-Jun) or 'all': ").lower()[:3]
        if month in months:
            return [month] if month != 'all' else months[1:]
        print(f"Data for {month} is not available. Please enter a valid month or 'all'.")

def get_day():
    """
    Prompt the user to enter a day or 'all' and validate the input.

    Returns:
        list: A list containing the selected day(s).
    """
    days = ['all', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    while True:
        day = input("Enter the day or 'all': ").lower()[:3]
        if day in days:
            return [day] if day != 'all' else days[1:]
        print(f"Data for {day} is not available. Please enter a valid day or 'all'.")

def load_data(city, month, day):
    """
    Load and filter the data based on the selected city, month, and day.

    Args:
        city (str): The city for which data is to be loaded.
        month (list): The month(s) to filter the data.
        day (list): The day(s) to filter the data.

    Returns:
        DataFrame: A filtered DataFrame based on the selected city, month, and day.
    """
    print("Loading data...")
    df = pd.read_csv(f"{city}.csv")
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month-str'] = df['Start Time'].dt.strftime('%b').str.lower()
    df['day'] = df['Start Time'].dt.strftime('%a').str.lower()
    df['hour'] = df['Start Time'].dt.strftime('%H')
    return df[df['Month-str'].isin(month) & df['day'].isin(day)]

def time_stats(df):
    """
    Calculate and display the most common month, day, and hour from the dataset.

    Args:
        df (DataFrame): The DataFrame containing the data.

    Returns:
        tuple: The most common month, day, and hour.
    """
    print("Calculating time statistics...")
    return df['Month-str'].mode()[0], df['day'].mode()[0], df['hour'].mode()[0]

def station_stats(df):
    """
    Calculate and display the most common start station, end station, and trip combination.

    Args:
        df (DataFrame): The DataFrame containing the data.

    Returns:
        tuple: The most common start station, end station, and trip combination.
    """
    print("Calculating station statistics...")
    return df['Start Station'].mode()[0], df['End Station'].mode()[0], (df['Start Station'] + " to " + df['End Station']).mode()[0]

def user_stats(df, city):
    """
    Calculate and display user statistics, including user types, gender counts, and birth year statistics.

    Args:
        df (DataFrame): The DataFrame containing the data.
        city (str): The city for which statistics are being calculated.
    """
    print("Calculating user statistics...")
    print(f"User Type Counts:\n{df['User Type'].value_counts()}")
    if city in ['chicago', 'new_york_city']:
        print(f"Gender Counts:\n{df['Gender'].value_counts()}")
        print(f"Birth Year:\nEarliest: {df['Birth Year'].min()}\nMost Recent: {df['Birth Year'].max()}\nMost Common: {df['Birth Year'].mode()[0]}")

def trip_duration_stats(df):
    """
    Calculate and display the total and average trip duration.

    Args:
        df (DataFrame): The DataFrame containing the data.
    """
    print("Calculating trip duration statistics...")
    print(f"Total Travel Time: {df['Trip Duration'].sum()}\nAverage Travel Time: {df['Trip Duration'].mean()}")

def display_data(df):
    """
    Display 5 rows of raw data at a time based on user input.

    Args:
        df (DataFrame): The DataFrame containing the data.
    """
    start_loc = 0
    while True:
        view_data = input("Do you want to see 5 rows of data? Enter yes or no: ").lower()
        if view_data == 'yes':
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
        else:
            break

def main():
    """
    Main function to run the program, allowing the user to explore data and restart the process.
    """
    while True:
        city = get_city()
        month = get_month()
        day = get_day()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()