
# Get the license plate from the user
license_plate = input("Enter a license plate: ")

# Check if the license plate is valid for the older style
if len(license_plate) == 6 and license_plate[0:3].isalpha() and license_plate[3:6].isdigit():
    print("The license plate is valid for the older style.")

# Check if the license plate is valid for the newer style
elif len(license_plate) == 7 and license_plate[0:4].isdigit() and license_plate[4:7].isalpha():
    print("The license plate is valid for the newer style.")

# If the license plate is not valid for either style
else:
    print("The license plate is not valid for either style.")