# Function to calculate the minimum insurance amount at 80%
def calculate_min_insurance(replacement_cost, insurance_rate=0.80):
    return replacement_cost * insurance_rate

def main():
    replacement_cost = float(input("Enter the replacement cost of the building: $"))

    min_insurance = calculate_min_insurance(replacement_cost)

    print(f"The minimum amount of insurance you should buy for the property is: ${min_insurance:.2f}")

main()

# Output: Enter the replacement cost of the building: $450000
# The minimum amount of insurance you should buy for the property is: $360000.00