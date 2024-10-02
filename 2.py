def calculate_state_tax(subtotal, state_tax_rate):
    return subtotal * state_tax_rate

def calculate_country_tax(subtotal, country_tax_rate):
    return subtotal * country_tax_rate

def calculate_total_tax(state_tax, country_tax):
    return state_tax + country_tax

def calculate_total_amount(subtotal, total_tax):
    return subtotal + total_tax

def main():
    subtotal = float(input("Enter the purchase amount: $"))
    state_tax_rate = float(input("Enter the state tax rate (e.g., 0.05 for 5%): "))
    country_tax_rate = float(input("Enter the country tax rate (e.g., 0.03 for 3%): "))

    state_tax = calculate_state_tax(subtotal, state_tax_rate)
    country_tax = calculate_country_tax(subtotal, country_tax_rate)
    total_tax = calculate_total_tax(state_tax, country_tax)
    total_amount = calculate_total_amount(subtotal, total_tax)

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"State tax: ${state_tax:.2f}")
    print(f"Country tax: ${country_tax:.2f}")
    print(f"Total tax: ${total_tax:.2f}")
    print(f"Total amount: ${total_amount:.2f}")

main()

# Output:: Enter the purchase amount: $19.99
# Enter the state tax rate (e.g., 0.05 for 5%): 0.10
# Enter the country tax rate (e.g., 0.03 for 3%): 0.03 
# Subtotal: $19.99
# State tax: $2.00
# Country tax: $0.60
# Total tax: $2.60
# Total amount: $22.59