#The goal is to simulate rolling a dice

#So first, we import the random module
import random

#I had to look up the single functions, but seems like random.randrange
#will give me an Int from 0 to 5 inclusive, so no 6!
#https://docs.python.org/3/library/random.html

#print(random.randrange(6))

#That's not exactly what we want. We have the right range (6 Numbers), but
#starting with zero, which is bullshit
#print(random.randrange(1,7))
#Now we have a range from 1 to 7, 7 inclusive?

#Let's do a simple for-Loop to see possible results and whether 7 is in it
#or not

#This produces exacly 70 results. Let's say propability for a 7 to occurr in
#the numbers is 1/7, with 70 results we should see about 10 times a seven,
#or to see whether we have a wrong range: at least once

#for i in range(1,70):
#    print(random.randrange(1,7))

#Output seems fine, so the operation random.randrage(1,7) produces a random int
#in the range from 1 to 6, 7 exclusive or to say: 6 inclusive, so 1,2,3,4,5 or 6

#So now we can move on to the, let's say, visual part:

print("Let's roll a dice. Your result: ", random.randrange(1,7))

result=input("Would you like to roll again? Y/N >> ")

if result == "Y" or result =="y":
    print("Ok, once again. Your result: ", random.randrange(1,7))
if result == "N" or result =="n":
    print("Ok. Bye.")
