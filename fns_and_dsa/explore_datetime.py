from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", current_date)

def calculate_future_date():
    num_of_days = int(input("Enter the number of days to add to the current date: "))
    now = datetime.now()
    future_date = now + timedelta(days=num_of_days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))