import time
import pandas as pd
import numpy as np

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")
    citeies = ["chicago", "new york city", "washington"]
    months = ["january", "february", "march", "april", "may", "june"]
    days = [
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
    ]
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city = input(
                "Please chose one of (chicago, new york city, washington) to select the city you want to explore\n"
            ).lower()
            if city in citeies:
                break
            else:
                print(
                    "please chose only one of these cities (chicago, new york city, washington)and write it as it is shown\n"
                )
                continue
        except ValueError as e:
            print(
                f"{e} please chose only one of these cities (chicago, new york city, washington)and write it as it is shown\n"
            )
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input(
                "Please chose one of (january, february, march, april, may, june, or all) months to select the month you want to explore on\n"
            ).lower()
            if month in months or month == "all":
                break
            else:
                print(
                    "please chose only one of these (january, february, march, april, may, june, or all) options and write it as it is shown\n"
                )
                continue
        except ValueError as e:
            print(
                f"{e} please chose only one of these (january, february, march, april, may, june, or all) options and write it as it is shown\n"
            )
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input(
                "Please chose one of the weekdays or all to select the day you want to explore on\n"
            ).lower()
            if day in days or day == "all":
                break
            else:
                print(
                    "please chose only one of these ( sunday, monday, tuesday, wednesday, thursday, friday, saturday, or all) options and write it as it is shown\n"
                )
                continue
        except ValueError as e:
            print(
                f"{e} please chose only one of these (sunday, monday, tuesday, wednesday, thursday, friday, saturday, or all) months and write it as it is shown\n"
            )
            continue
    print("-" * 40)

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
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    if month == "all":
        df["month"] = df["Start Time"].dt.month
    else:
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df[df["month"] == month]

    if day == "all":
        df["day_of_week"] = df["Start Time"].dt.weekday_name
    else:
        # days=["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()
    print(df)
    # TO DO: display the most common month
    mon = df["month"].mode()[0]
    months = ["january", "february", "march", "april", "may", "june"]
    print(f"The most common month is {months[mon-1].title()}")
    # TO DO: display the most common day of week
    dayy = df["day_of_week"].mode()[0]
    print(f"The most common day is {dayy}")
    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    hour = df["hour"].mode()[0]
    print(f"The most common hour is {hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # TO DO: display most commonly used start station
    start = df["Start Station"].mode()[0]
    print(f"The most common start station is: {start.title()}")

    # TO DO: display most commonly used end station
    end = df["End Station"].mode()[0]
    print(f"The most common end Station is: {end.title()}")

    # TO DO: display most frequent combination of start station and end station trip
    combin = (df["Start Station"] + "," + df["End Station"]).mode()[0]
    print(
        f"The most common combination of start station and end station is:"
        + str(combin.split(","))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # TO DO: display total travel time
    tt = df["Trip Duration"].sum()
    print(
        f"The total travel time:\nin seconds {tt}\nin minutes {int(tt/60)}\nin hours {int((tt/60)/60)}\n"
    )
    # TO DO: display mean travel time
    mt = df["Trip Duration"].mean()
    print(f"The total travel time:\nin seconds {mt}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types
    users_count = df["User Type"].value_counts()
    print(f"The number of each user type:\n{users_count}")
    # TO DO: Display counts of gender
    if "Birth Year" in df and "Gender" in df:
        gender_count = df["Gender"].value_counts()
        print(f"The number of each user type:\n{gender_count}")

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = int(df["Birth Year"].min())
        most_recent = int(df["Birth Year"].max())
        most_common = df["Birth Year"].mode()[0]
        print(f"The erliest year of birth: {earliest}\n")
        print(f"The most recent year of birth: {most_recent}\n")
        print(f"The most common year of birth:{int(most_common)}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def raw_data(df):
    nexth = 0
    while True:
        ask = input(
            "Would you like to view the next five trips data? Enter yes or no.\n"
        ).lower()
        if ask != "yes":
            break
        else:
            nexth += 5
            print(df.iloc[nexth : nexth + 5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            rawdata = input(
                "would you like to view the first five trips? Enter yes or no.\n"
            ).lower()
            if rawdata != "yes":
                break
            else:

                head = 5
                print(df.head(head))
                raw_data(df)
                break

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()
