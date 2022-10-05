#Question 1
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]
fall = ["September", "October", "November"]
winter = ["December", "January", "February"]


monthinput = input("Please enter the name of the month as a string:")
dayofthemonth  = int(input("Please enter the day of the month as an integer:"))

if monthinput in spring:
    if dayofthemonth < 20:
        print("The season is winter")
    elif dayofthemonth >= 20:
        print("The season is spring")
elif monthinput in summer:
    if dayofthemonth < 21:
        print("The season is spring")
    elif dayofthemonth >= 21:
        print("The season is summer")
elif monthinput in fall:
    if dayofthemonth < 22:
        print("The season is summer")
    elif dayofthemonth >= 22:
        print("The season is fall")
elif monthinput in winter:
    if dayofthemonth < 21:
        print("The season is fall")
    elif dayofthemonth >= 21:
        print("The season is winter")
else:
    print("The month you entered is not valid")

#Question 2
sports = ["Football", "Basketball"]
newsport = input("Please enter a sport:")
sports.append(newsport)
sports.sort()
print(sports)

#Question 3
tencolors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "white", "gray"]
startindexofcolor = input("Please enter the starting index of the color you want to see between 0 and 4:")
endindexofcolor = input("Please enter the ending index of the color you want to see between 5 and 9:")
print(tencolors[int(startindexofcolor):int(endindexofcolor)])

#Question 4
import random
randomlist = [9, (), [], {}, "John", 3.14, True, None, [[],[]]]
print(random.choice(randomlist))

#Question 5
list1= [1, 1, 3, 4, 4, 5, 6, 7]
list2= [0, 1, 2, 3, 4, 4, 5, 7, 8]
sumofeveryelement = sum(list1) + sum(list2)
numberofelements = len(list1) + len(list2)
averageofeveryelement = sumofeveryelement / numberofelements
print(averageofeveryelement)

#Question 6
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
        

