import random
print("number guessing game")
number=random.randint(1, 9)
chances=0
print("guess a number between 1 and 9")
while chances<5:
    guess=int(input("enter your guess:"))
    if guess==number:
        print("congratulations you won")
        break
    elif guess<number:
        print("your guess was low,guess a number higher than",guess)
    else:
        print("your guess was higher,guess a number lower than",guess)
    chances+=1
if not chances<5:
    print("You loose the number is",number)
    