import random
user_input = int(input("Guess a number between 0 and 10: "))
magic_number = random.randint(0,10)

if user_input == magic_number:
    print("You got it! It was %d" % (magic_number))
else:
    print("That's not it! It was %d" % (magic_number))