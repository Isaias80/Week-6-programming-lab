# Function to calculate the assessment value (60% of actual value)
def calculate_assessment_value(actual_value):
    return actual_value * 0.60

# Function to calculate the property tax
def calculate_property_tax(assessment_value, tax_rate_per_100):
    return (assessment_value / 100) * tax_rate_per_100

def main():
    actual_value = float(input("Enter the actual value of the property: $"))

    tax_rate_per_100 = 0.75

    assessment_value = calculate_assessment_value(actual_value)
    property_tax = calculate_property_tax(assessment_value, tax_rate_per_100)

    print(f"\nAssessment Value: ${assessment_value:.2f}")
    print(f"Property Tax: ${property_tax:.2f}")

main()

#OUTPUT:
#Enter the actual value of the property: $3,450,000

#Assessment Value: $2,070,000.00
#Property Tax: $15,525.00