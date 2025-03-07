#1. Display a menu with 3 choices* with numbering:

#'menu' is the name of the variable that holds the message and choices to be displayed to a user. 

#3 quotes is used in this case to create a multi-lined string (NOT a comment) for readability.

menu = """

Want to know your zodiac sign? Choose the number(1-3) that represents your birth month from the menu below:

1: January, February, March, April 

2: May, June, July, August

3: September, October, November, December

"""

print(menu) #outputs the value of the variable named 'menu'



#2. Read an Integer, which is the choice selected by a user, from console:

#Takes an input from the user, converts the string number to an integer and assign it to a variable named 'choose'.

choose = int(input('Which number has your birth month:'))



#3. Output a predefined message* for the user’s choice:

#Creates a conditional statement; this outputs a predefined message depending on the value inputted by the user.

if choose == 1:  #if the user inputs 1, output this message:

  print('Charismatic! Your zodiac sign is Aries')

elif choose == 2: #if the user inputs 2, output this message:

  print('Dynamic! Your zodiac sign is Gemini')

elif choose == 3:  #if the user inputs 3, output this message: 

  print('Charming! Your zodiac sign is Libra')

else:  #if the user inputs any number greater than 3 OR less than 1, output this message:

  print('The number you have entered is not on the menu! Choose a number from the menu.')