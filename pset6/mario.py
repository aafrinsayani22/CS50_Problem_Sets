# Include library
from cs50 import get_int

n = get_int("Height: ")
# Forever loop utill gets valid input
while (n < 1) or (n > 8):
    n = get_int("Height: ")


# For n number of rows
for i in range(n):
    # For spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # For hashes
    for k in range(i + 1):
        print("#", end="")
    print()
