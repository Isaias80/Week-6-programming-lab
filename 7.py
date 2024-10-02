# Function to calculate the number of gallons of paint required
def calculate_gallons_required(square_feet):
    return square_feet / 112

# Function to calculate the hours of labor required
def calculate_labor_hours(square_feet):
    return (square_feet / 112) * 8

# Function to calculate the cost of the paint
def calculate_paint_cost(gallons_required, price_per_gallon):
    return gallons_required * price_per_gallon

# Function to calculate the labor charges
def calculate_labor_charges(labor_hours, labor_rate=35.0):
    return labor_hours * labor_rate

# Function to calculate the total cost of the paint job
def calculate_total_cost(paint_cost, labor_charges):
    return paint_cost + labor_charges

# Main program
def main():
    # Input: square feet of wall space and price per gallon of paint
    square_feet = float(input("Enter the square feet of wall space to be painted: "))
    price_per_gallon = float(input("Enter the price of paint per gallon: $"))

    # Calculate gallons required, labor hours, paint cost, labor charges, and total cost
    gallons_required = calculate_gallons_required(square_feet)
    labor_hours = calculate_labor_hours(square_feet)
    paint_cost = calculate_paint_cost(gallons_required, price_per_gallon)
    labor_charges = calculate_labor_charges(labor_hours)
    total_cost = calculate_total_cost(paint_cost, labor_charges)

    # Output the results
    print(f"\nGallons of paint required: {gallons_required:.2f}")
    print(f"Hours of labor required: {labor_hours:.2f}")
    print(f"Cost of the paint: ${paint_cost:.2f}")
    print(f"Labor charges: ${labor_charges:.2f}")
    print(f"Total cost of the paint job: ${total_cost:.2f}")

# Call the main function to run the program
main()


# OUTPUT:
# Enter the square feet of wall space to be painted: 4000
# Enter the price of paint per gallon: $12

# Gallons of paint required: 35.71
# Hours of labor required: 285.71
# Cost of the paint: $428.57
# Labor charges: $10000.00
# Total cost of the paint job: $10428.57