from random import randint   #|| Importing the randint function to generate a random integer.
import os    #|| Importing the os module to use system commands
os.system('cls')   #|| Clears the terminal screen (specific to Windows).

print("3D NATIONAL Swertres")   #|| Prints the game title.
result = randint(100, 999)   #|| randint(100, 999): Generates a random number between 100 and 999.
res = str(result)    #||  Converts the number to a string to facilitate string comparison later.


print(f"Ang Number nga mo gawas {result}.")   #|| Displays the generated number to the user.

user = input("TARGET/RAMBOL NATIONAL numbers: ")   #|| Prompts the user to enter their guessed number.

if user == res:       #|| Checks if the user's guess matches the generated number exactly.
    print("Daog ka sa target!!.")   #|| Informs the user they won by guessing the exact number.

elif (sorted(user) == sorted(res)) and (user != result):  #|| Checks if the user's guess contains the same digits in any order but is not an exact match.
    print("daog kas rambol!!")   #|| Informs the user they won by guessing the correct digits in a different order.

elif len(user) == 4:   #|| Checks if the user entered a four-digit number, which is invalid.
    print("tulo ra taman brad!!") #|| Informs the user that the input should be three digits long.
    
else: #|| Handles all other cases where the user did not win.
    print(f"pildi man ka brad!! {result}.")   #|| : Informs the user they lost and shows the generated number.