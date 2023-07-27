print("please guess a num from 1 to 10")
print("if num you guess is = to python choice you would win")
print("="*47)
import random
x=random.randint(1,10)
x=str(x)
print("python choise is " + x)
a = input()
print("your choise is " + a)
if a == x:
  print("you win")
else:
  print("you lost")
print("="*42)
print("please upvote")
