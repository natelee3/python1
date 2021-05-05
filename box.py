width_box = input("Width? ")
height_box = input("Height? ")


for width_box in range(n):
    for height_box in range(2*n):
        print('*' if width_box in(0,n-1) or height_box in(0,(2*n)-1) else ' ', end = ' ')
    print()