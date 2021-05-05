coins = 0
print("You have 0 coins.")
x = input("Do you want another? ")

while x == "yes":
    coins += 1
    print("You have %d coins" % (coins))
    x = input("Do you want another? ")
else: 
    print("Bye")