# Part 2: Displaying the numbers in descending order
def display_descending():
    # Asking the user to enter three numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Determine the order in descending
    if num1 >= num2:
        if num1 >= num3:
            first = num1
            if num2 >= num3:
                second = num2
                third = num3
            else:
                second = num3
                third = num2
        else:
            first = num3
            second = num1
            third = num2
    else:
        if num2 >= num3:
            first = num2
            if num1 >= num3:
                second = num1
                third = num3
            else:
                second = num3
                third = num1
        else:
            first = num3
            second = num2
            third = num1

    print(f"The numbers in descending order are: {first}, {second}, {third}")

display_descending()