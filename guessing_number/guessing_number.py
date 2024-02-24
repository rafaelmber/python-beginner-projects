import random

# def main():
#     print("""The computer will choose a random number from 1 to 100 and you must to guess the number.
# the computer will give you hints if the inserted number is greater or lower than the selected one
#           """)
#     rand_number = random.randint(1,100)

#     attempts = 0

#     print("The random number was selected...")
#     while True:
#         user_number = int(input("Enter a number: "))

#         attempts += 1

#         if(rand_number > user_number):
#             print(f"The random number is greater than {user_number}")
#         elif(rand_number < user_number):
#             print(f"The random number is lower than {user_number}")
#         else:
#             break
#     print(f"Congratulations, the random number was {rand_number}. It took you {attempts} attempts")

def user_guess(x):
    """The user must guess the computers random number
    """
    random_number = random.randint(1, x)

    guess  = 0
    while guess != random_number:
        guess  = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)

        if(guess < random_number):
            print("Sorry, guess again. Too low.")
        elif(guess > random_number):
            print("Sorry. guess again. Too high.")

    print(f'Yay, congrats. You have guessed the number {random_number} correctly')

def computer_guess(x):
    """The computer must guess the users random number"""
    print("""The computer must guess your number, write:
    C if the computer guess is correct
    L if the computer guess is lower 
    H if the computer guess id higher
          """)

    low = 1
    high = x

    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess  = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct(C)?: ").lower()

        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay, I guess the number {guess} correctly')

if __name__ == '__main__':
    # user_guess(10)
    computer_guess(10)