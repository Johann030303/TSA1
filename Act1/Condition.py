# Function to determine the highest number
def find_highest_number(num1, num2, num3):
    if num1 >= num2:
        if num1 >= num3:
            return num1  # num1 is the highest
        else:
            return num3  # num3 is the highest
    else:
        if num2 >= num3:
            return num2  # num2 is the highest
        else:
            return num3  # num3 is the highest

# Function to display numbers in descending order
def display_descending_order(num1, num2, num3):
    if num1 >= num2:
        if num1 >= num3:
            if num2 >= num3:
                return [num1, num2, num3]  # num1, num2, num3
            else:
                return [num1, num3, num2]  # num1, num3, num2
        else:
            return [num3, num1, num2]  # num3, num1, num2
    else:
        if num2 >= num3:
            if num1 >= num3:
                return [num2, num1, num3]  # num2, num1, num3
            else:
                return [num2, num3, num1]  # num2, num3, num1
        else:
            return [num3, num2, num1]  # num3, num2, num1

# Main program
if __name__ == "__main__":
    # Input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Find and display the highest number
    highest = find_highest_number(num1, num2, num3)
    print(f"The highest number is: {highest}")

    # Display numbers in descending order
    descending_order = display_descending_order(num1, num2, num3)
    print("Numbers in descending order: ", descending_order)