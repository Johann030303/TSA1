input_digits = input("Enter a string with digits: ")
digit_sum = 0

for char in input_digits:
    if char.isdigit():
        digit_sum += int(char)

print(f"Sum of digits: {digit_sum}")