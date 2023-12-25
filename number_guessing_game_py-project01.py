import random

number_to_guess = random.randint(1, 10)

while True:
    number_to_guess_user = int(input("Enter the number between 1 to 10 you guessed: "))

    if number_to_guess_user < 1:
        print("Sorry, negative numbers are not considered and also less than expected.\n Try Again!")
    elif number_to_guess_user > 10:
        print("Sorry, the number you guessed is greater than expected.\n Try Again!")
    elif number_to_guess_user == number_to_guess:
        print("Congratulations!, you guessed the correct number: ", number_to_guess_user)
        break
    elif number_to_guess_user < number_to_guess:
        print("Guessed, too low.\n Try Again!")
    elif number_to_guess_user > number_to_guess:
        print("Guessed, too high.\n Try Again!")
