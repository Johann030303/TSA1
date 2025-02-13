from datetime import datetime

def format_date():
    date_input = input("Enter the date (mm/dd/yyyy): ")
    try:
        date_object = datetime.strptime(date_input, "%m/%d/%Y")
        formatted_date = date_object.strftime("%B %d, %Y")
        print(f"Date Output: {formatted_date}")
    except ValueError:
        print("Invalid date format. Please enter the date in mm/dd/yyyy format.")

format_date()
