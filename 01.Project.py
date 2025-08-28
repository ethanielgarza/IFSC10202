def convert_seconds_to_time_units():
    """
    Prompts for a length of time in seconds and converts it into
    years, days, hours, minutes, and remaining seconds.
    """
    try:
        total_seconds = int(input("Enter the length of time in seconds: "))
        if total_seconds < 0:
            print("Please enter a non-negative number of seconds.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer for seconds.")
        return

    # Constants for time conversion
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_YEAR = 365

    SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR
    SECONDS_PER_DAY = SECONDS_PER_HOUR * HOURS_PER_DAY
    SECONDS_PER_YEAR = SECONDS_PER_DAY * DAYS_PER_YEAR

    years = total_seconds // SECONDS_PER_YEAR
    remaining_seconds_after_years = total_seconds % SECONDS_PER_YEAR

    days = remaining_seconds_after_years // SECONDS_PER_DAY
    remaining_seconds_after_days = remaining_seconds_after_years % SECONDS_PER_DAY

    hours = remaining_seconds_after_days // SECONDS_PER_HOUR
    remaining_seconds_after_hours = remaining_seconds_after_days % SECONDS_PER_HOUR

    minutes = remaining_seconds_after_hours // SECONDS_PER_MINUTE
    seconds = remaining_seconds_after_hours % SECONDS_PER_MINUTE

    print(f"\nGiven {total_seconds} seconds:")
    print(f"Number of years: {years}")
    print(f"Number of days: {days}")
    print(f"Number of hours: {hours}")
    print(f"Number of minutes: {minutes}")
    print(f"Number of seconds: {seconds}")
# Call the function to execute the program
convert_seconds_to_time_units()