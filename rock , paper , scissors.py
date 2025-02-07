
import random

#key -> values
# ROCK -> 🪨
ROCK = 'r'
PAPER= 'p'
SCISSORS = 's'

emojis = { ROCK :'🪨',
           SCISSORS : '✂️',
           PAPER : '📃'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input('ROCK,PAPER OR SCISSOR ? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice !')
    
def display_choices(user_choice , computer_choice):
    print(f'you chose{emojis[user_choice]}')
    print(f'computer choice{emojis[computer_choice]}')  
    
def determine_winner(user_choice , computer_choice):
    if user_choice == computer_choice:
        print("Tie")
    elif(user_choice == ROCK and computer_choice == SCISSORS or
        user_choice == SCISSORS and computer_choice == PAPER or
        user_choice == PAPER and computer_choice == 'r'):
        print('You Win!')
    else:
        print('You Lose!')
        
def play_game():
    while True:
        user_choice = get_user_choice()
        
        computer_choice = random.choice(choices)
        
        display_choices(user_choice,computer_choice)
        
        determine_winner(user_choice,computer_choice)
        
        should_continue = input('Do want to continue ? (y/n): ').lower()
        if should_continue == 'n':
            print('Thankyou for playing !')
            break
        
play_game()

    
          
    
    

    

    
          
        


    

