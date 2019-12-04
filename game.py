import time
import random


welcome_message = 'welcome to the magic number game!'

print(welcome_message)

ask_user_for_number = int(input('Can you please select a number between 0-10?  '))

time.sleep(0.5)

magic_number = random.randint(0,10)

magic_number_message = f'The magic number for this round was {magic_number}, you selected {ask_user_for_number}'

print(magic_number_message)
tries = [1,2,3,4,5]

for count in tries:

    if ask_user_for_number == magic_number:
        print('You Have Won This Round!')
        break
        print ('Well done !')

    elif ask_user_for_number > magic_number:
        print('Your guess was above the magic number, Try Again!')
        ask_user_for_number = int(input('Can you please select a number between 0-10?  '))
        continue

    else:
        print('Your guess was below the magic number, Try again')
        ask_user_for_number = int(input('Can you please select a number between 0-10?  '))
        continue

