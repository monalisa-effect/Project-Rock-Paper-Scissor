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

chioce = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

chioce = int(chioce)

if chioce == 0:
  print(rock)
  print('rock')
elif chioce == 1:
   print(paper)
   print('paper')
elif chioce == 2:
  print(scissors)
  print('scissors')

comp = random.randint(0,3)
if comp == 0:
  print(rock)
  print('rock')
elif comp == 1:
   print(paper)
   print('paper')
elif comp == 2:
  print(scissors)
  print('scissors')


if chioce == comp:
  print('draw')

elif chioce == 0 and comp == 1:
  print('your lose')

elif chioce == 1 and comp == 0:
  print('your win')
  
elif chioce == 1 and comp == 2:
  print('your lose')

elif chioce == 2 and comp == 1:
  print('your win')

elif chioce == 0 and comp == 2:
  print('your win')

elif chioce == 2 and comp == 0:
  print('your lose')