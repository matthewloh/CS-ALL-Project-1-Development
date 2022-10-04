# #Question 1
# spring = ["March", "April", "May"]
# summer = ["June", "July", "August"]
# fall = ["September", "October", "November"]
# winter = ["December", "January", "February"]


# monthinput = input("Please enter the name of the month as a string:")
# dayofthemonth  = int(input("Please enter the day of the month as an integer:"))

# if monthinput in spring:
#     if dayofthemonth < 20:
#         print("The season is winter")
#     elif dayofthemonth >= 20:
#         print("The season is spring")
# elif monthinput in summer:
#     if dayofthemonth < 21:
#         print("The season is spring")
#     elif dayofthemonth >= 21:
#         print("The season is summer")
# elif monthinput in fall:
#     if dayofthemonth < 22:
#         print("The season is summer")
#     elif dayofthemonth >= 22:
#         print("The season is fall")
# elif monthinput in winter:
#     if dayofthemonth < 21:
#         print("The season is fall")
#     elif dayofthemonth >= 21:
#         print("The season is winter")
# else:
#     print("The month you entered is not valid")

# #Question 2
# sports = ["Football", "Basketball"]
# newsport = input("Please enter a sport:")
# sports.append(newsport)
# sports.sort()
# print(sports)

#Question 3
# tencolors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "white", "gray"]
# startindexofcolor = input("Please enter the starting index of the color you want to see between 0 and 4:")
# endindexofcolor = input("Please enter the ending index of the color you want to see between 5 and 9:")
# print(tencolors[int(startindexofcolor):int(endindexofcolor)])

# #Question 4
# import random
# randomlist = [9, (), [], {}, "John", 3.14, True, None, [[],[]]]
# print(random.choice(randomlist))

# #Question 5
# list1= [1, 1, 3, 4, 4, 5, 6, 7]
# list2= [0, 1, 2, 3, 4, 4, 5, 7, 8]
# sumofeveryelement = sum(list1) + sum(list2)
# numberofelements = len(list1) + len(list2)
# averageofeveryelement = sumofeveryelement / numberofelements
# print(averageofeveryelement)

#Question 6
import string
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
stringofcharacters = input("Please enter a string of characters:")
if not (5<len(stringofcharacters)<8):
    print("The string you entered is ")
elif len(stringofcharacters) == 6:
    if (list(stringofcharacters[0:3])in alphabet_list and stringofcharacters[3:6] in number_list):
        print("The string you entered is valid for older format")
    else:
        print(stringofcharacters)
        print(stringofcharacters[0:3], stringofcharacters[3:6])
        a = list(stringofcharacters[0:3])
        print(a in alphabet_list)
        print(a)
elif len(stringofcharacters) == 7:
    if stringofcharacters[0:4] in number_list  and stringofcharacters[4:7] in alphabet_list:
        print("Second last line")
else:
    print("Last line")
        

