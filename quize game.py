
questions = ("Who was the first woman Prime Minister of India?",
             "Which river is known as the 'Ganga of the South'?",
             "Which city is known as the 'Silicon Valley of India'?",
             "What is the national animal of India?",
             "Who wrote the Indian national anthem 'Jana Gana Mana'?")

options = (("A. Indira Gandhi", "B. Sarojini Naidu", "C. Pratibha Patil",'D. Sonia Gandhi'),
           ("A. Krishna", "B. Yamuna", "C. Godavari",'D. Kaveri'),
           ("A. Hyderabad", "B. Bengaluru", "C. Pune ",'D. Chennai '),
           ("A. Lion ", "B. Tiger ", "C. Elephant ",'D. Peacock '),
           ("A. Rabindranath Tagore ", "B. Bankim Chandra Chatterjee ", "C. Mahatma Gandhi ",'D. Chandra Bose'))           
    
answers = ( 'A','C','B','B','A')

guesses = []
score = 0
question_num = 0

print("Welcome to quize play!\n")
ask_user = input("Do you want to play game ? \n ")

if ask_user != "yes":
    quit()
    
for question in questions:
    print("\n************************\n")
    print(question)
   
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
    else:
            print('INCORRECT!')
            print(f'{answers[question_num]} is the correct answer')
            
    question_num += 1
print('answers: ', end= ' ') 
for answer in answers:
    print(answer, end = " ")
print('\nguesses: ', end = ' ')
for guess in guesses:
    print(guess , end = ' ')

score = int(score / len(questions)* 100)
print(f'\nYour score is: {score}%')