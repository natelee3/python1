day = int(input("Day (0-6)? "))
if day == 0:
    print("Sleep in")
elif 1 <= day <= 5 :
    print("Go to work)
elif day == 6:
    print("Sleep in")
else:
    print("We'll try again later...")