for i in range(6, 0, -1):
    print("* " * i)
    
rows = 6

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
# hello