animals = ["Lion", "Elephant", "Dolphin", "Kangaroo", "Panda",  
    "Eagle", "Parrot", "Penguin", "Peacock", "Owl",      
    "Crocodile", "Snake", "Lizard", "Tortoise", "Chameleon",  
    "Frog", "Salamander", "Toad", "Newt",               
    "Shark", "Salmon", "Clownfish", "Seahorse", "Tuna", 
    "Butterfly", "Ant", "Bee", "Grasshopper", "Ladybug"]
import random
k = random.choice(animals)
list_name= []
for i in range(len(k)):
      list_name.append(k[i])
b = ""
for l in range(len(list_name)):
        b+="_"

count = 0
num = len(k)
print(f"guess the {num} lettered animals")
is_on = True
while is_on == True:
      y = input("enter your letter")
      if y not in list_name:
             count+=1
      if count == 1:
            print('''
                  +---+
                  |   |
                  O   |
                  /|\  |
                  / \  |
                        |
                  =========
                  ''')
      if count == 2:
            print( '''
                  +---+
                  |   |
                  O   |
                  /|\  |
                  /    |
                        |
                  =========
                  ''')
      if count == 3:
                  print( '''
                  +---+
                  |   |
                  O   |
                  /|\  |
                        |
                        |
                  =========
                  ''')
      if count ==4:
                  print('''
                  +---+
                  |   |
                  O   |
                  /|   |
                        |
                        |
                  =========''')
      if  count == 5:
                  print('''
                  +---+
                  |   |
                  O   |
                  |   |
                        |
                        |
                  =========
                  ''')
      if count==6:
                  print('''
                  +---+
                  |   |
                  O   |
                        |
                        |
                        |
                  =========
                  ''')
      if count ==7:
            print("you have lost the game")
            print('''
            +---+
            |   |
                  |
                  |
                  |
                  |
            =========
            ''')
            print(k)
            is_on = False
      if y in k:
            if y in list_name:
                  indic = list_name.index(y)
                  b = b[:indic]+y+b[indic+1:]
                  list_name[indic] = None
                  print(b,"is the original word in animals")
      if b == k:
            print("congrats party ledha pushpa")
            print("party ivvakapothe nuvvu gay gadivi")
            is_on = False
