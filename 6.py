# Function to calculate income from ticket sales
def calculate_income(class_a_tickets, class_b_tickets, class_c_tickets):
    # Prices for each class of seats
    class_a_price = 20.0
    class_b_price = 15.0
    class_c_price = 10.0

    # Calculate total income for each class
    income_a = class_a_tickets * class_a_price
    income_b = class_b_tickets * class_b_price
    income_c = class_c_tickets * class_c_price

    # Total income from all classes
    total_income = income_a + income_b + income_c

    return total_income

def main():
    # Input: number of tickets sold for each class
    class_a_tickets = int(input("Enter the number of Class A tickets sold: "))
    class_b_tickets = int(input("Enter the number of Class B tickets sold: "))
    class_c_tickets = int(input("Enter the number of Class C tickets sold: "))

    # Calculate the total income
    total_income = calculate_income(class_a_tickets, class_b_tickets, class_c_tickets)

    # Output the total income generated from ticket sales
    print(f"\nTotal income generated from ticket sales: ${total_income:.2f}")

# Call the main function to run the program
main()

# OUTPUT:
# Enter the number of Class A tickets sold: 100
# Enter the number of Class B tickets sold: 50
# Enter the number of Class C tickets sold: 25

# Total income generated from ticket sales: $3000.00