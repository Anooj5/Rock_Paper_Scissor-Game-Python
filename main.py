import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
images=[rock,paper,scissors]

he = int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for Scissors.\n"))
if (he>2) or (he<0):
  print("Wrong number")
else:
  print(images[he])

  he1=random.randint(0,2)
  print(he1)
  print(images[he1])
  # if (he == 0)& (he1 == 1):
  #   print("You lose")
  # elif (he == 1)&(he1 == 2):
  #   print("You lose")
  # elif(he == 2)&(he1 == 0):
  #   print("you lose")
  
  if(he==0) and (he1==2):
    print("You Win!")
  elif(he1==0) and (he==2):
    print("You Lose")
  elif(he1>he):
    print("you Lose")
  elif(he>he1):
    print("You Win")
  elif(he==he1):
    print("Draw")
  
  



# rock = 2
# paper = 1
# scissors = 0
# print(he)
# he1 = print("Computer choice:")
# he2 = random.random[0,2]
# print(he2)

