def divide(a, b):
    if b == 0:
        return None
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        return None
    return a % b

def summation(a, b):
    if a > b:
        return None
    return sum(range(a, b + 1))

def main():
    while True:
        print("\nMathematical Operations:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == 'Q':
            print("Exiting program.")
            break
        
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            
            if choice == 'D':
                result = divide(a, b)
            elif choice == 'E':
                result = exponentiate(a, b)
            elif choice == 'R':
                result = remainder(a, b)
            elif choice == 'F':
                result = summation(a, b)
            else:
                print("Invalid choice. Try again.")
                continue
            
            if result is None:
                print("Invalid input for the selected operation.")
            else:
                print("Result:", result)
        
        except ValueError:
            print("Please enter valid integers.")

if __name__ == "__main__":
    main()
