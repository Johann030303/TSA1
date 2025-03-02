import csv

def load_exchange_rates(file_path):
    rates = {}
    with open(file_path, newline='', encoding="ISO-8859-1") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            code, _, rate = row  # Extract currency code and exchange rate
            rates[code] = float(rate)
    return rates

def convert_currency(amount, currency_code, rates):
    if currency_code in rates:
        converted_amount = amount * rates[currency_code]
        return converted_amount
    else:
        return None

def main():
    file_path = "currency.csv"  # Ensure the correct path
    rates = load_exchange_rates(file_path)
    
    try:
        usd_amount = float(input("How much dollar do you have? "))
        currency_code = input("What currency you want to have? ").strip().upper()
        
        converted = convert_currency(usd_amount, currency_code, rates)
        
        if converted is not None:
            print(f"\nDollar: {usd_amount} USD")
            print(f"{currency_code}: {converted:.6f}")
        else:
            print("Invalid currency code. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.")

if __name__ == "__main__":
    main()
