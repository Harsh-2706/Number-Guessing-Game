import random

top_of_range = input("Type in a number:")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("Please type in a number greater than zero")
        quit()
else:
    print("Please type in valid input")
    quit()

random_number = random.randint(0, top_of_range)
guesses=0

while True:
    guesses+=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a valid integer again")
        continue

    if user_guess == random_number:
        print("You Got it Correct!:)")
        print("The number is", random_number)
        break
    elif user_guess > random_number:
        print("Your guess was above the actual number")
    else:
        print("Your guess was below the number")
print("You got it in", guesses, "guesses")
