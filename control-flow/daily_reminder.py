''' This script will ask the user for a single task, its priority level, and if it is time-sensitive'''

task = str(input("Enter your task: "))
priority = str(input("Enter the task priority(high/medium/low):"))
time_bound = str(input("Is it time-bound? (yes/no): ")).lower()

match priority:
    case priority if priority == "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is not time bounded. Consider completing it when you have free time.")
    case priority if priority == "medium":
        if time_bound == "yes":
            print(f"Reminder: The task '{task}' is a medium priority task that requires attention today!")
        else:
            print(f"Note: The task '{task}' is not time bounded. Consider completing it when you have free time.")
    case priority if priority == "low":
        if time_bound == "yes":
            print(f"Note: The task '{task}' is  time bounded but low priority. Consider completing the sooner.")
        else:
            print(f"Note: The task '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Error! Make sure to pick the right answer!")
        
    

