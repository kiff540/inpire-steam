# HOW TO DRAW A PYRAMID 
n = 5  # Adjust this to change the size

# 1. Top Half (including the middle row)
for i in range(n):
    # Print spaces + Print stars
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# 2. Bottom Half
for i in range(n - 2, -1, -1):
    # Print spaces + Print stars
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

print("")

# HOW TO DRAW A TRIANGLE
rows = 5
for i in range(1, rows + 1):
    # Print spaces first, then stars
    print(" " * (rows - i) + "*" * (2 * i - 1))