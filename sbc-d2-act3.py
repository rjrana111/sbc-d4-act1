from random import randint as com

# Clear screen function for cross-platform compatibility
import os
os.system('cls')


# Prompt user for input
p1 = int(input("Enter Your number (0 - Unfold, 1 - Fold): "))
c1, c2 = com(0, 1), com(0, 1)  # Generate random choices for computers

# Function to select the string representation of the choices
def selected(x, y, z):
    select = ["Unfold", "Fold"]
    return select[x], select[y], select[z]

# Function to process and determine the winner
def process(p1, c1, c2):
    if p1 != c1 and p1 != c2:
        return "P1 wins"
    elif c1 != p1 and c1 != c2:
        return "C1 wins"
    elif c2 != p1 and c2 != c1:
        return "C2 wins"
    else:
        return "DRAW!!!"

# Validate user input
if p1 not in [0, 1]:
    print("Invalid Selection")
else:
    player, com1, com2 = selected(p1, c1, c2)  # Get string representations of the choices
    print(f"P1 = {player}\nC1 = {com1}\nC2 = {com2}\n")  # Print choices
    print(process(p1, c1, c2))  # Print the result
