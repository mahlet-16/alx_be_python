# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
reminder = f"Reminder: '{task}' is a {priority} priority task"

match priority:
    case "high":
        reminder += " that requires immediate attention"
    case "medium":
        reminder += " that should be completed soon"
    case "low":
        reminder += " that can be done when you have free time"
    case _:
        reminder = "Invalid priority level entered. Please restart and try again."
        print(reminder)
        exit()

# Adjust for time sensitivity
if time_bound == "yes":
    reminder += " today!"

# Final Reminder
print(reminder)

