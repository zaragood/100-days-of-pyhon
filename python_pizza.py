print("Welcom to python pizza\nWhat type of pizza would you like to oder?")
print("Small Pizza: $15\nMedium Pizza: $25\nLarge Pizza: $25")
size = input("S for small, M for medium, L for large; ")

bill = 0;
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
    
add_peperoni = input("Do you want peperoni? Y / N: ")
if add_peperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
cheese = input("Do you want cheese? Y / N:? ")
if cheese == "Y":
    bill += 1
    
print(f"Y our total cost is {bill}")
    


    