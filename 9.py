# Function to convert feet to inches
def feet_to_inches(feet):
    return feet * 12

def main():
    # Input: number of feet from the user
    feet = float(input("Enter the number of feet: "))

    # Convert feet to inches using the function
    inches = feet_to_inches(feet)

    print(f"{feet} feet is equal to {inches:.2f} inches.")

main()

#OuTpUt:
# Enter the number of feet: 6
# 6.0 feet is equal to 72.00 inches.