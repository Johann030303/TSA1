def is_palindrome(num):
    return str(num) == str(num)[::-1]

def process_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue
        numbers = [int(x) for x in line.split(',')]
        total = sum(numbers)
        palindrome_status = 'Palindrome' if is_palindrome(total) else 'Not a palindrome'
        print(f"Line {i}: {line} (sum {total}) - {palindrome_status}")

process_file('numbers.txt')
