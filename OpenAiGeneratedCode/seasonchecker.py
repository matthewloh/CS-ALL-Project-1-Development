"""
The year is divided into four seasons: spring, summer, fall (or autumn) and winter. While the
exact dates that the seasons change vary a little bit from year to year because of the way that
the calendar is constructed, we will use the following dates for this exercise:

Create a program that reads a month and day from the user. The user will enter the name of the
month as a string, followed by the day within the month as an integer. Then your program should
display the season associated with the date that was entered.
"""


def main():
    month = input("Enter the month: ")
    day = int(input("Enter the day: "))

    if month == "January" or month == "February":
        if month == "January" and day < 20:
            print("Winter")
        elif month == "February" and day < 19:
            print("Winter")
        else:
            print("Spring")
    elif month == "March" or month == "April":
        if month == "March" and day < 21:
            print("Spring")
        elif month == "April" and day < 20:
            print("Spring")
        else:
            print("Summer")
    elif month == "May" or month == "June":
        if month == "May" and day < 22:
            print("Summer")
        elif month == "June" and day < 21:
            print("Summer")
        else:
            print("Fall")
    elif month == "July" or month == "August":
        if month == "July" and day < 23:
            print("Fall")
        elif month == "August" and day < 22:
            print("Fall")
        else:
            print("Winter")
    elif month == "September" or month == "October":
        if month == "September" and day < 23:
            print("Winter")
        elif month == "October" and day < 22:
            print("Winter")
        else:
            print("Spring")
    elif month == "November" or month == "December":
        if month == "November" and day < 22:
            print("Spring")
        elif month == "December" and day < 21:
            print("Spring")
        else:
            print("Summer")


if __name__ == "__main__":
    main()