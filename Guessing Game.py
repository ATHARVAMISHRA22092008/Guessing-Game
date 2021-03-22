from random import*
comp=randint(1,10)
p=int(input("Type a number"))   
while p!=comp:
   if p<comp:
      print("That's too low, try higher")
   if p>comp:
      print("That's too high, go lower")
   p=int(input("Type a number"))
print("Congrats, You got it")
