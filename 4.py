# Function to calculate the total monthly cost
def calculate_total_monthly_cost(loan, insurance, gas, oil, tires, maintenance):
    return loan + insurance + gas + oil + tires + maintenance

# Function to calculate the total annual cost
def calculate_total_annual_cost(monthly_cost):
    return monthly_cost * 12

# Main program
def main():
    # Input: monthly costs for different automobile expenses
    loan = float(input("Enter the monthly loan payment: $"))
    insurance = float(input("Enter the monthly insurance cost: $"))
    gas = float(input("Enter the monthly gas cost: $"))
    oil = float(input("Enter the monthly oil cost: $"))
    tires = float(input("Enter the monthly tire cost: $"))
    maintenance = float(input("Enter the monthly maintenance cost: $"))

    # Calculate total monthly and annual costs
    total_monthly_cost = calculate_total_monthly_cost(loan, insurance, gas, oil, tires, maintenance)
    total_annual_cost = calculate_total_annual_cost(total_monthly_cost)

    print(f"\nTotal Monthly Cost: ${total_monthly_cost:.2f}")
    print(f"Total Annual Cost: ${total_annual_cost:.2f}")

main()

#OUTPUT: 
# Enter the monthly loan payment: $241.37
# Enter the monthly insurance cost: $150
# Enter the monthly gas cost: $110
# Enter the monthly oil cost: $10
# Enter the monthly tire cost: $10
# Enter the monthly maintenance cost: $10

# Total Monthly Cost: $531.37
# Total Annual Cost: $6376.44