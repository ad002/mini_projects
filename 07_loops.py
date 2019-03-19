'''I have to practice loops a lot'''

for x in range(0,10):
    print(str(x)+"abc")
#prints 0abc ... 9abc

list=['a','b','c','d','e','f','g','h']

#for x in list:
#    print(list[x]) #TypeError: list indices must be integers or slices, not str

for i in list:
    print(i) #this is the way to go 
    #strange, because this prints the x[i] element so there seems to 
    #be a connection made between the datatype and the counter variable
    

#<alternative>
for i in list: print(i)

#_____________________FOR LOOPS | INTRO________________________________
#https://data36.com/python-for-loops-explained-data-science-basics-5/

#For loops are like in everyday life: You go trough your shopping list 
#until you've collected every item from it. The dealer gives a card for
#each player until everyone has five and so on. 

#For loops are for iterating trough 'iterables'
#These will mostly be well known data types: lists, strings or dicts 
#and sometimes they can also be range() objects

#__________________ITERATING THROUGH A LIST______________________________
numbers=[1,5,23,45]
for i in numbers:
    print(i*i)
    
#1. We set a list of numbers with 4 elements
#2. We took the first element (because of zero indexing it's the 0th 
#   element tbh) of the list (the 1) and stored it into the i variable!
#3. Then we executed the print(i*i) function, wich returned the squared
#   value of 1 which is also one 
#4. All over again: We took the next element (the 5) and assigned it to
#   the i variable! 

#_________________PROCESS FLOW | LOGIC OF LOOPS _______________________
#1. Define an iterable (e.g. list, string, etc...) 
#2. Take the first element of the iterable, store it in "i"/store-variable 
#3. Does this element exist? 
#4. Yes: action, move back to 3
#5. No: End loop 

#__________________THE STORING VARIABLE | THE 'i'______________________
# - i is a "temporary" variable and it's only role is to store the given 
# element of the list to work with it in the given iteration of the loop
# - although mostly called i, the naming is arbitrary. The point is to 
# set a variable and then refer to it when using it inside the loop


#_________________ITERATING THROUGH STRINGS_____________________________
my_list="Hello World"
for i in my_list:
    print(i)
#Out: One letter per row 

#Remember: Strings are basically handed as sequences of characters, this 
#the for loop will work with them pretty much as it did with lists

#________________ITERATING THROUGH RANGE OBJECTS________________________
my_list = range(0,10)
for i in my_list:
    print(i)#out: 0 1 2 ... 9 each line one number

for i in range(0,10):
    print(i)#same output. Each line one number, 0 to 9 
    
# Range is a built in function we use almost exclusivily within for loop
# in a nutshell: It generates a list of numbers

my_list=range(0,10,2) #0=first element, 10=last element, 2=the "step"
#10=element 10, so numerically when starting with zero it's 10-1
#the "step" defines the difference between each element in the range 

#___________________________EXERSIZE____________________________________
my_string = "python"
#out:
#p
#py
#pyt
#pyth
#pytho
#python
#pytho
#pyth
#pyt
#py
#p

#Write a script that does this for any my_string value 

#Cutting and slicing strings
#https://www.pythoncentral.io/cutting-and-slicing-strings-in-python/

liste=my_string.split()
for i in liste:
    print(i)#prints all letters in one row
    
for i in my_string:
    print([i])
    #['p']
    #['y']
    #['t']
    #['h']
    #['o']
    #['n']
#Returns all caracters from position two until the end of the string 
print(my_string[2:len(my_string)]) #ython


#____________________________SOLUTION__________________________________

for i in range(len(my_string)):
    print(my_string[:i]) #p py pyt pyth pytho 
    #returns from the beginning to pos i 
    #returns from zeroth element to ith while i is ascending 
    #from one to two and so on
    
#We need an integer i (countable) here, so as long we haven't reached 
#the end of the string(len) with our i...
for i in range(len(my_string)):
    #prints only the ith element of the string until the last one 
    print(my_string[i:])#out: python pytho pyth pyt py p
    #returns from position i to the end of the file 
    
    

#In my head both of them should be swapped as it does make more sense 
#to me that if you print only until the ith element [:i] this should be 
#the descending string (python pytho ...) but the output teached me 
#different

print("His solution")
#His solution:
x=0
for i in my_string:
    x=x+1
    print(my_string[0:x])

for i in my_string:
    x=x-1
    print(my_string[0:x])

#So we basically did the same thing. Just with a difference in treating
#i as a counting variable. Whereas he instantiated i as a temporary
#variable of my_string, which isn't used for defining the length or the
#iterations of the loop, and used x for counting upwards or downwards

#Guess my code is a bit more pythonic as I need one variable less and 
#use the fact that you can return the first element of a string by 
#entering the list and only returning elements until the ith element 
#my_string[:i] returns from beginning  until ith position
#Whereas my_string[i:] returns from the ith position until the end  

