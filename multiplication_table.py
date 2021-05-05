x = 1
y = 1


for x in range(1,11):
    for y in range(1,11):
        print(str(x) + " X " + str(y) + " = " + str(x*y))
        y += 1
    x+=1#