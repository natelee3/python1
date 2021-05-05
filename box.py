rows = int(input("Width? "))
columns = int(input("Height? "))


#for width_box in range(n):
 #   for height_box in range(2*n):
  #      print('*' if width_box in(0,n-1) or height_box in(0,(2*n)-1) else ' ', end = ' ')
   # print()

for i in range(rows):
    for j in range(columns):
        if (i == 0 or i == rows -1 or j == 0 or j == columns - 1):
            print('*', end = '  ')
        else: 
            print(' ', end = '  ')
    print()