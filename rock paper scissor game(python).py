
import random
user_choice=int(input("enter 0 for rock, 1 for paper and 2 for scissor"))
computer_choice=random.randint(0,2)
# ASCII Art for each choice
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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissor]

if user_choice>=3 or user_choice<0:
    print("you entered invalid number")

else:
    print(game_images[user_choice])
    print("computer has chosen",computer_choice)
    print(game_images[computer_choice])
    
    if computer_choice==0 and user_choice==2:
        print("you loose")
    elif computer_choice==2 and user_choice==0:
        print("you win")

    elif user_choice<computer_choice:
        print("you loose")
    elif user_choice>computer_choice:
        print("you win")
    elif computer_choice==user_choice:
        print("draw")



