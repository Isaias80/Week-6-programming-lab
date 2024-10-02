# Function to convert kilometers to miles
def convert_km_to_miles(kilometers):
    return kilometers * 0.6214

kilometers = float(input("Enter distance in kilometers: "))
miles = convert_km_to_miles(kilometers)

print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")

# Output: Enter distance in kilometers: 5
# 5.0 kilometers is equal to 3.11 miles.