#Work or Sleep in?
#Prompt the user for a day of the week and print "Go to work" or "Sleep in" depending on if it's a workday

day = int(input("Day (0-6)? "))
if day == 0 or day == 6:
    print("Sleep in")
elif 1 <= day <= 5 :
    print("Go to work")
else:
    print("We'll try again later...")