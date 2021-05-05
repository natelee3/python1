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


print("Tip amount: $" + '%.2f' % float(tip))
print("Total amount: $" + '%.2f' % float(total + tip))
