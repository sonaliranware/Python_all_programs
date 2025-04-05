#canddy jar game
import random
ans='y'
print("*****welcome to caddy jar game")
name=input("enter your name")
print("hi"+name+" Guess the  how many candies in jar !!!")
print("you guess the number in bewenn 40,55 ")
guesscntr=0
guess=0
num=random.randint(40,55)
print(num)
while guess!=num and guesscntr<5:
    guess=int(input("enter your guess"))
    guesscntr=guesscntr+1
    if guess<num:
        print("number is a little higher")
    elif guess>num:
        print("number is little lower")
    else:
        print("congrats your answer is correct !enjoy your candies")
if guesscntr==5 and guess!=num:
    print("sorry you have run out of guesses......good bye") 
print("Thank you for playing game.......")                   
    
