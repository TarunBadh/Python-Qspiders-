import random 
Guess = int(input('Enter your Number : '))
print(' Player Guess ', Guess)
Bot_Guess= random.randint(1,10)
print('Bot Guess ', Bot_Guess)
while True :
    if Guess!=Bot_Guess:
        print('InCorrect Guess')
        break
    else:
        print('Correct Guess')
        break

        