import random

def guess(x):
    rand_num = random.randint(1,x)
    guess = 0
    while guess != rand_num:
        guess = int(input(f"Guess a number betweem 1 and {x}"))
        print(guess)
        if guess < rand_num:
            print("sorry, guess again. Too low.")
        elif guess > rand_num:
            print("Sorry, guess again. Too high.")

    print(f"You have guessed the number {rand_num} correctly")

    def comp_guess(x):
        low = 1
        high = x
        feedback = ""
        while feedback != "c": 
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low       
                feedback = input(f"Is {guess} too high (H), too low (L), or correct (C) ?? "). lower()
            if feedback == "H":
                high = guess - 1
            elif feedback == "L":
                low = guess + 1
        print(f"The computer guessed your number, {guess} correctly")

guess(10)