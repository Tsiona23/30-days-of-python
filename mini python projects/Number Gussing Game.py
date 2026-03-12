import random
number = random.randint(1, 10) # random numebr between 1 and 10
guess = 0
print ("guess the number between 1 and 10")
while guess != number:
    guess = int(input("Your guess: "))
    
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct! You guessed the number.")