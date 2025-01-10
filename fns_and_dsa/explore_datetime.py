from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_datetime = datetime.now()

    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    current_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Print the current date and time
    print(f"Current date and time: {current_date}")

# Part 2: Calculate a Future Date
def calculate_future_date(days_to_add):
    # Get the current date and time
    current_datetime = datetime.now()

    # Use timedelta to add days
    future_datetime = current_datetime + timedelta(days=days_to_add)

    # Format the future date as "YYYY-MM-DD"
    future_date = future_datetime.strftime("%Y-%m-%d")

    # Print the future date
    print(f"Future date: {future_date}")

# Main function to execute the program
def main():
    # Display the current date and time
    display_current_datetime()

    # Prompt the user to enter a number of days
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Calculate and display the future date
        calculate_future_date(days_to_add)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()

