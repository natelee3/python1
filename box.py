rows = int(input("Width? "))
columns = int(input("Height? "))

for i in range(rows):
    for j in range(columns):
        if (i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
            print('*', end = '  ')
        else: 
            print(' ', end = '  ')
    print()