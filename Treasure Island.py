
#Treasure Island Project
print("Treasure Island Project\n")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("Welcome to Treasure Island. Your Mission is to find the treasure\n")
locs=int(input('''
where you want to go left or right.
Type 1 for  Left and 2 for  Right
\n
'''))
if locs==1:
  print("Swim or wait\n")
  ques=input('''
  Do you want to swim or wait\n
  Type s for swim and w for wait
  ''').lower()
  if ques=="s" :
    print("Attacked By Trout.Game Over\n")
  elif  ques=="w":
    dors=str(input('''
    Which door you want to choose? Blue,Red,
    Yellow or Purple \n
    ''')).lower()
    if dors== "blue":
      print("Eaten By Beasts.Game Over\n")
    if dors== "red":
      print("Burned by fire.Game Over")
    if dors== "yellow":
      print("You found the treasure!You win")
    if dors== "purple":
       print("Eaten By Sharks and Crocodiles\n")
if locs==2:
    print("Game Over\n")