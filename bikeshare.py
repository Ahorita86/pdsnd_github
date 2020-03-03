import time
import pandas as pd
import numpy as np

### the following data was given by the programm

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              
### the data was merged and now the data applies

def get_filters():
    cities_list=["chicago", "new york city", "washington"]
    months_list =["all","january","february","march","april","may","june","juli","august","september","october","november","december"]
    days_list = ["all","monday", "tuesday","wednesday","thursday","friday","saturday","sunday"]

    print("Hello! Let\s explore some US bikeshare data!")

    city = input("From which city would you like to see data from?Please choose between \"Chicago\",\"New York City\",\"Washington\"?").lower()

    while((city not in cities_list)):
        print("I am sorry but the answer did not match one of the options. Please try again.")
        city = input("Please enter your input?").lower()
    print("Ok. Answer was understood.")

    month = input("From which month would you like to see the data? Please choose a specific month or if you want to see the data from all months combined type \"all\".").lower()

    while((month not in months_list)):
        print("I am sorry but the answer did not match one of the options. Please try again.")
        month = input("Please enter your input?").lower()
    print("Ok. Answer was understood.")

    day = input("From which day would you like to see the data? Please choose a specific day or if you want to see the data from the entire week type \"all\".").lower()

    while((day not in days_list)):
        print("I am sorry but the answer did not match one of the options. Please try again.")
        day = input("Please enter your input?").lower()

    print("Ok. Answer was understood.")
    print("Thank you for your answers. We will now provide the data.")

    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.weekday_name

    if month != "all":
        months = ["january", "february", "march", "april", "may", "june","july","august","september","november","december"]
        month = months.index(month) + 1

    if day != "all":
        days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
        day = days.index(day)+1

    return df

def time_stats(df):
    print("The System is calculating the most frequent times of travel.")
    start_time = time.time()

    df["month"] = df["Start Time"].dt.month
    popular_month = df["month"].mode()[0]

    df["day"] = df["Start Time"].dt.weekday_name
    popular_weekday = df["day"].mode()[0]

    df["hour"] = df["Start Time"].dt.hour
    popular_hour = df["hour"].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))

    print("Most Popular month is:",popular_month)
    print("Most Popular weekday is:",popular_weekday)
    print("Most Popular hour is:",popular_hour)

def station_stats(df):
    print("This are the most popular stations and trips:")
    start_time = time.time()

    popular_start_station = df["Start Station"].mode()
    popular_end_station = df["End Station"].mode()
    journee = df["Start Station"] + df["End Station"]
    popular_journee = journee.mode()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("Most Popular start station is:",popular_start_station)
    print("Most Popular end station is:",popular_end_station)
    print("Most Popular journee is:",popular_journee)

def trip_duration_stats(df):
    print("This are the statistics concerning the durations of travel:")
    start_time = time.time()

    total = df["Trip Duration"].sum()
    average = df["Trip Duration"].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("This is the total amount of travel time for your filter:",total)
    print("This is the average travel time for your filter:", average)

def user_stats(df):
    print("This are the statistics concerning the user:")
    start_time = time.time()

    user_type = df["User Type"].value_counts()
    gender = df["Gender"].value_counts()
    earliest_birthyear = df["Birth Year"].min()
    most_recent_birthyear = df["Birth Year"].max()
    most_common_birthyear = df["Birth Year"].mode()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("This is the counts per user type:", user_type)
    print("This is the counts per gender:", gender)
    print("This is the the earlist year of birth from the data:", earliest_birthyear)
    print("This is the the most recent year of birth from the data:", most_recent_birthyear)
    print("This is the the most common year of birth from the data:", most_common_birthyear)

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        count = 0
        while True:

            display = input("Do you want to see only the next five rows then please enter \"yes?\" and if not please enter \"no\".").lower()
            if display =="yes":
                print(df.iloc[count:count+5])
                count +=1
            else:
                break

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
