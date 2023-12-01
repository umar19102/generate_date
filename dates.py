import json
from datetime import datetime, timedelta

def generate_month_dates():
    # Get the current date
    current_date = datetime.now()

    # Get the first day of the current month
    first_day_of_month = current_date.replace(day=1)

    # Calculate the last day of the current month
    if first_day_of_month.month == 12:
        next_month = first_day_of_month.replace(year=first_day_of_month.year + 1, month=1)
    else:
        next_month = first_day_of_month.replace(month=first_day_of_month.month + 1)

    last_day_of_month = next_month - timedelta(days=1)

    # Generate a list of dates for the current month
    dates_of_month = [first_day_of_month + timedelta(days=x) for x in range((last_day_of_month - first_day_of_month).days + 1)]

    # Convert dates to strings
    formatted_dates = [date.strftime("%Y-%m-%d") for date in dates_of_month]

    return formatted_dates

def save_to_json(dates, filename="current_month_dates.json"):
    with open(filename, "w") as json_file:
        json.dump({"dates": dates}, json_file, indent=4)
    print(f"JSON file '{filename}' created successfully.")

if __name__ == "__main__":
    # Generate current month dates
    month_dates = generate_month_dates()

    # Save dates to JSON file
    save_to_json(month_dates)
