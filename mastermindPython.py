#Nischal Shrestha
#9/19/2015
#MASTERMIND GAME

import random

alphabet = 'ABCDEF'
code = ''.join(random.sample(alphabet, 4))
print (code)

number_of_guesses_left = 10
code_broken = False
guess_number = 0

print('Welcome to MasterMind')

while number_of_guesses_left > 0:
    print ('Guesses left:',(number_of_guesses_left - guess_number), end = ' ')
    guess = input('Enter exactly 4 letters from ABCDEF: ')
    
    correct_position = 0
    correct_letters = 0
    tempguess = list(guess)
    tempcode = list(code)
    number_of_guesses_left -= 1

    for i in range(4):
        if code[i] == guess[i]:
            correct_position += 1
            
    for j in range(4):
        if tempcode[j] in tempguess:
            correct_letters += 1           
           
    print ('Correct in place: ', correct_position)
    print ('Correct letters: ', correct_letters)
                       
    if guess == code:
        print('You won! Congratulations!')
        number_of_guesses_left = 0
        code_broken = True
        
if not code_broken:
    print ('The code is', code)
    print('Too bad, you lost.')
