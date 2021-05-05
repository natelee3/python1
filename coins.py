#How Many Coins?
#Prompts you for how many coins you want one by one

coins = 0
print("You have 0 coins.")
x = input("Do you want another? ")

while x == "yes":
    coins += 1
    print("You have %d coins" % (coins))
    x = input("Do you want another? ")
else: 
    print("Bye")