def compute_sum():
    # Asking the user for the first and last term
    first_term = int(input("Enter first term number: "))
    last_term = int(input("Enter last term number: "))

    # Initialize the sum variable
    total_sum = 0

    # Loop from first term to last term (inclusive)
    for number in range(first_term, last_term + 1):
        total_sum += number

    print(f"The sum of the numbers from {first_term} to {last_term} is {total_sum}")

compute_sum()