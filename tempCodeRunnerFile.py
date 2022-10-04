import string
alphabet_list = list(string.ascii_uppercase)
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
stringofcharacters = input("Please enter a string of characters:")
if not len(stringofcharacters) == 6 and not len(stringofcharacters) == 7:
    print("The string you entered is invalid")
elif len(stringofcharacters) == 6:
    if stringofcharacters[0:3] in alphabet_list and stringofcharacters[3:5] in number_list:
        print("The string you entered is valid for older format")
    else:
        print("The string you entered is invalid")
elif len(stringofcharacters) == 7:
    if stringofcharacters[0:4] in number_list  and stringofcharacters[4:7] in alphabet_list:
        print("The string you entered is valid for newer format")
else:
    print("The string you entered is invalid")