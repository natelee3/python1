#Print a Square 2
#This time, user dictates the length of each side of the square before it is printed

side = int(input("How big is the square? "))

for i in range(side):
    for i in range(side):
        print('*', end = '  ')
    print()