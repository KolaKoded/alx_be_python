# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Draw the square pattern using nested loops
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after completing the row
    row += 1