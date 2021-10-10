#!/usr/bin/env python
# coding: utf-8

# In[23]:


import time
import datetime
import pandas as pd
import numpy as np


# In[24]:


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# In[25]:


cities=['chicago','new york city','washington']
months=['january','february','march','april','may','june','all']
days=['saturday', 'sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday',  'all']


# In[26]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while(True):
        try:
            city=input("Which city do you want to explore? ex:(chicago, new york city, washington)").lower()
            if city in cities:
                print("valid entry")
                break;
        except unvalid_entry:
            print("unvalid_enty")

    # get user input for month (all, january, february, ... , june)
    while(True):
        try:
            month=input("Which month do you want to explore? ex:(all, january, february, ... , june)").lower()
            if month in months:
                print("valid entry")
                break;
        except unvalid_entry:
            print("unvalid_enty")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while(True):
        try:
            day=input("Which day do you want to explore? ex:(all, monday, tuesday, ... sunday)").lower()
            if day in days:
                print("valid entry")
                break;
        except unvalid_entry:
            print("unvalid_enty")

    print('-'*40)
    return city, month, day


# In[27]:


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
    df=pd.read_csv(CITY_DATA[city]);
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.strftime("%A")
    return df


# In[28]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    Most_Comman_Month=df['month'].value_counts().idxmax()
    print("The Most Common Month Is :",Most_Comman_Month)

    # display the most common day of week
    Most_Comman_Day=df['day'].value_counts().idxmax()
    print("The Most Common Day Of Week Is :",Most_Comman_Day)

    # display the most common start hour
    Most_Comman_Start_Hour=df['Start Time'].dt.strftime("%H").value_counts().idxmax()
    print("The Most Common Start Hour Is :" ,Most_Comman_Start_Hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[29]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Most_Comman_Start_Station=df['Start Station'].value_counts().idxmax()
    print("The Most Common Start Station Is :" ,Most_Comman_Start_Station)
    # display most commonly used end station
    Most_Comman_End_Station=df['End Station'].value_counts().idxmax()
    print("The Most Common End Station Is :" ,Most_Comman_End_Station)

    # display most frequent combination of start station and end station trip

    Most_frequent_combination= df[['Start Station', 'End Station']].mode().loc[0]
    print("The most frequent combination of start station and end station trip : {}, {}".format(Most_frequent_combination[0],Most_frequent_combination [1]))    
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[30]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("The Total Travel Time/ " ,total_travel_time )

    # display mean travel time
    Mean_travel_time=df['Trip Duration'].mean()
    print("Mean Travel Time ",Mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[31]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    Counts_Of_User_Types=df['User Type'].value_counts()
    print("Counts Of User Types " ,Counts_Of_User_Types)

    # Display counts of gender
    if 'Gender' in df.columns:
        counts_of_gender=df['Gender'].value_counts()
        print("counts_of_gender " ,counts_of_gender)
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns :
        earliest_year=df['Birth Year'].min()
        most_recent_year=df['Birth Year'].max()
        most_comman_year=df['Birth Year'].value_counts().idxmax()
        print("Earlist Year Of Birth Is : " , earliest_year)
        print("Most Recent Year Is " ,most_recent_year)
        print("Most comman Year Is " ,most_comman_year)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


# In[32]:


def show_data(df):
    print("Do you want to see five rows of data ? [yes,no]")
    row_data =input().lower();
    if row_data == 'yes':
        print(df.head())
        print('-'*60)
    elif row_data == 'no':
        print('ok!')
        print('-'*60)
    counter =0; 
    while row_data == 'yes':
        print('Do you want to see five rows of data ? [yes , no ]')
        row_data =input().lower();
        if row_data == 'yes':
            counter=counter+5
            print(df[counter:counter+5])
            print('-'*60)
        elif row_data == 'no':
            print('-'*60)
            break;


# In[ ]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        show_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:





# In[ ]:




