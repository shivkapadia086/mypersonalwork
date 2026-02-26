rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)
    
rows = 5

for i in range(rows, 0, -1):
    # Print leading spaces
    print(" " * (rows - i), end="")
    
    # Print stars
    for j in range(i):
        print("* ", end="")
    
    print()