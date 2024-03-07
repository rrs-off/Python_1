from datetime import datetime

def date_difference_in_seconds(date1, date2):
    # Convert date strings to datetime objects
    date_format = "%Y-%m-%d %H:%M:%S"
    datetime1 = datetime.strptime(date1, date_format)
    datetime2 = datetime.strptime(date2, date_format)

    # Calculate the time difference
    time_difference = datetime2 - datetime1

    # Extract the total seconds from the time difference
    seconds_difference = time_difference.total_seconds()

    return seconds_difference

# Example usage:
date_str1 = "2024-02-25 12:00:00"
date_str2 = "2024-02-26 15:30:45"

result = date_difference_in_seconds(date_str1, date_str2)
print(f"The difference between the two dates is {result} seconds.")
