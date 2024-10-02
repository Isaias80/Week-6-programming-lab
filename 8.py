# Constants for tax rates
STATE_TAX_RATE = 0.05  # 5% state tax
COUNTY_TAX_RATE = 0.025  # 2.5% county tax

# Function to calculate the county sales tax
def calculate_county_tax(total_sales):
    return total_sales * COUNTY_TAX_RATE

# Function to calculate the state sales tax
def calculate_state_tax(total_sales):
    return total_sales * STATE_TAX_RATE

# Function to calculate the total sales tax (county + state)
def calculate_total_tax(county_tax, state_tax):
    return county_tax + state_tax

def main():
    # Input: total sales for the month
    total_sales = float(input("Enter the total sales for the month: $"))

    # Calculate the county tax, state tax, and total tax
    county_tax = calculate_county_tax(total_sales)
    state_tax = calculate_state_tax(total_sales)
    total_tax = calculate_total_tax(county_tax, state_tax)

    # Output the results
    print(f"\nCounty Sales Tax: ${county_tax:.2f}")
    print(f"State Sales Tax: ${state_tax:.2f}")
    print(f"Total Sales Tax: ${total_tax:.2f}")

main()

#OUTPUT:
# Enter the total sales for the month: $4300000

# County Sales Tax: $107500.00
# State Sales Tax: $215000.00
# Total Sales Tax: $322500.00