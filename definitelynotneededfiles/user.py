total_cost = 0
cost = 0 
while True:
    age = input("Enter age: ")
    if age == "":
        break
    age = int(age)
    if age <= 2:
        cost += 0
    elif age <= 12:
        cost += 14
    elif age >= 65:
        cost += 18
    else:
        cost += 23
    total_cost += cost
print(f"Total cost: RM{cost}.00")