import random
print("Welcome to rock paper scissor")
a=input("select one choice from rock , paper, scissor: ")
choices=['rock', 'paper', 'scissor']
b=random.choice(choices)
if a not in choices:
  raise ValueError("you select invalid choice")
rock=0
paper=1
scissor=2
def check(a,b):
  if(a==b):
    return 0
  elif(a==0 and b==1) and (a==2 and b==0) and (a==1 and b==2):
    return -1
  return 1
score=check(a,b)
print("computer choose: ", b)
if(score==0):
  print("Draw")
elif(score==-1):
  print("You Lost")
elif(score==1):
  print("you won")
