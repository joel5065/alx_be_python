import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current date and time:", current_date)

def calculate_future_date():
    num_of_days = int(input("Enter the number of days to add to the current date: "))
    now = datetime.date.today()
    future_date = now + datetime.timedelta(days=num_of_days)
    print("Future date:", future_date)
