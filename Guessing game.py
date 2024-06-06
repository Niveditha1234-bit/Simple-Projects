print('Lets Play guessing game')
import random
print('I am guessing a number from 0 to 100')
r=random.randint(0,100)
t=1
while(t<=25):
  guess=int(input('Guess the number:'))
  if(guess==r):
    print('Won Successfully')
    break
  elif(guess>r):
    print('try guessging in lower number')
  elif(guess<r):
    print('try guessging in higher number')
  if(t==25):
    print('sorry ...better luck next time')
