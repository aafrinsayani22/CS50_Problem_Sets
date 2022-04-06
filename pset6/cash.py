# Include library
from cs50 import get_float
# Initialize counter
counter = 0
# Loop until valid input
while True:
    changeOwed = get_float("change owed: ")
    if (changeOwed > 0):
        break
# Round to cents
cents = round(changeOwed * 100)

# loops for choosing the coins
while (cents >= 25):
    counter += 1
    cents = cents - 25
while (cents >= 10):
    counter += 1
    cents = cents - 10
while (cents >= 5):
    counter += 1
    cents = cents - 5
while (cents >= 1):
    counter += 1
    cents = cents - 1
print(f"{counter}")