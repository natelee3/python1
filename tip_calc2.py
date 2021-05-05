#Tip Calculator 2
#Adds the ability to split the check into equal parts between a number of people


total = int(input("Total bill amount? "))
level = input("Level of service? ")
if level == "good":
    tip = (.2 * int(total))
elif level == "fair":
    tip = (.15 * int(total))
elif level == "bad":
    tip = (.1 * int(total))
else:
    print("error")

split = int(input("Split how many ways? "))
new_total = (total + tip)
per_person = float(new_total / split)

print("Tip amount: $" + '%.2f' % float(tip))
print("Total amount: $" + '%.2f' % float(new_total))
print("Amount per person: $" + '%.2f' % float(per_person))

