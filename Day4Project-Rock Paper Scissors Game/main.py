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
game_images = [rock, paper, scissors]
game_is_on = True
while game_is_on:
    user_choice = int(input("What do you choose?. Type 0 for Rock, 1 for Paper and 3 for Scissor.\n"))
    if user_choice >= 3 or user_choice < 0:
        print("Invalid Choice")
    else:
        print(f"User Choice {game_images[user_choice]}")
        computer_choice = random.randint(0, 2)
        print(f"Computer Choice {game_images[computer_choice]}")
        if computer_choice == 0 and user_choice == 2:
            print("You Lose.")
        elif user_choice == 0 and computer_choice == 2:
            print("You Win")
        elif computer_choice > user_choice:
            print("You Lose")
        elif user_choice > computer_choice:
            print("You Win")
        elif user_choice == computer_choice:
            print("It is a Draw")