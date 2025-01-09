''' This script will ask the user for a single task, its priority level, and if it is time-sensitive '''

# Get user input for task description
task = input("Enter your task description: ")

# Get user input for priority
priority = input("Enter the priority (high, medium, low): ").lower()

  # Get user input for time sensitivity
time_bound = input("Is this task time-bound (yes or no): ").lower()

  # Create the reminder message based on priority and time sensitivity
reminder = f"The task '{task}' has a {priority} priority. "

  # Use match case for priority and add urgency for time-bound tasks
match priority:
    case "high":
      reminder += "Reminder: This is a high-priority task!"
    case "medium":
      reminder += "Reminder: The sooner you complete this task the better it will be. "  # No additional message for medium priority
    case "low":
      reminder += "Note: You can complete this at your convenience."
    case _:
      reminder = "Invalid priority. Please enter high, medium, or low."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"

  # Print the reminder message
print(reminder)
        
    

