def print_star_pattern():
   
    for i in range(3):
        for j in range(3 - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()
    
    
    for i in range(1, -1, -1):
        for j in range(3 - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()

print_star_pattern()
