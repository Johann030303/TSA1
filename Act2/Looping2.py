def is_prime():
    # Asking the user for a number
    number = int(input("Enter a number greater than 1: "))

    # Check if the number is less than 2
    if number < 2:
        print(f"{number} is not a prime number.")
        return

    # Assume number is prime until proven otherwise
    is_prime = True

    # Loop from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

is_prime()