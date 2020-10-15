for row in range(1, 10):
    for s in range(10-row):
        print(' ', end=' ')
    for j in range(1, row):
        print(j, end=' ')
    for j in range(row,0,-1):
        print(j, end=' ')
    print()
    
for row in range(1,10):
    for s in range(row+1):
        print(' ', end=' ')
    for j in range(1, 10-row):
        print(j, end=' ')
    for j in range(8-row,0,-1):
        print(j, end=' ')
    print()
    
for i in range(3):
    for j in range(3):
        print("*", end="")
    print()


for i in range(5):
    for j in range(5):
        print(i, j)
