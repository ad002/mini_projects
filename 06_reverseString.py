#Take user input 
x=input("Gimme some text to reverse it \n > ")
#Using slicing/stride as it is the shortest version
print("Your reversed string is " +x[::-1])


#____________________OPTIONS FOR STRING REVERSING______________________
#https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/

#___________________Solution 1: Using Slicing/Stide_____________________
def stride(x):
    print(x[::-1] )
#-> Just retrieving all characters of a string moving with step size -1
# (stride) as the first two parameters define a section you want to 
#retrieve and the third one defines the step size while doing so.
 
#-> For more INFORMATION on strings, slicing and stride see 
#'07_strings+slicing' and to see an exersice in which I used
#slicing to solve another problem see '08_loops+slicing_ex'

#___________________Solution 2: Using loops_____________________________

#or how I would call it: the pearl necklace method 
def necklaceReverse(x):
    #Create empty string 
    str=''
    #store list elements of x temporarily in i, in this case the first 
    #one
    for i in x:
        #in str, put the ith element of x 
        str=i+str
	#The trick is to put the ith element first and then add the empty
	#string, so every i item gets added up and moves trough the line
	#to the end from being the first new element in the string to be 
	#the last one
	#So let's say our string to reverse is 'string', 
	#the i takes the 's' and is added to the empty string first.
	#With another loop the new i, in this case 't', is put before
	#the string(i+str), which consists of the 's' already so now we 
	#have 'ts'
	#-> It's like putting the first, second, third element of the 
	#string always as the new first element of the str variable which 
	#results in the first element of our input to be the last of the 
	#output
	#-> Just like putting beads from one pearl necklace to another 
	# --a--b--c--d-- 1st necklace
	# --b--a-------	 2nd necklace, always taking the first element of
	#		 one to be the new first element of two until 
	#the next
    return str



#___________________Solution 3: using recursion________________________

def recursionReverse(x):
	#until the string entered into the function isn't empty 
	if len(x)==0:
		return x
	else:
		#Calling the function inside the function again  
		return recursionReverse(x[1:])+x[0]

#https://bit.ly/2FkhbdG
#Short intro to recursion: basically a function calling itself again, 
#and with every recursive call the solution of the problem is downsized.
#Each step, the problem is reduced to a simpler version of the 
#problem until you can solve it, the so called 'base case': 
#The problem is now so simple, that it can be solved without any 
#further recursion. Then the function  
#terminates and starts counting it's steps on the way back.  
#-> Very important: W/out termination you have infinite loop

#An example would be: you sit in a large auditorium in he last row. You 
#want to know how many rows there are but you are a lazy piece of shit
#and refuse to to count the rows. So you decide to ask someone in the 
#row before you. He doesn't know so he asks the one in the row before 
#him and so on until we get to Alice. Because Alice is sitting in first 
#row and can answer that there is no more row in front of her we now 
#have the base case. The guy behind Alice adds 1 to her answer until 
#we've reached the last row and have the exact amount of rows.  

#Breaking down the recursive Statement:
# x[1:]		From element one (including), meaning letter 2 of string
#		onwards until the end of the string 
#		-> all elements except first letter

# x[0]		element at index zero, meaning the first string letter

# 0 [SPLIT] 1 2 3 4 5 6 7 8 9 

#String is splitted in two parts, part from index one onwards gets fed
#back into the algorithm, while first character is taken out and gets
#stored into a stack of memory temporarily until the recursive method
#ends. 
#This is why with each step we have len(-1) left as we take one character
#out of the String with each iteration. The first, to be exact. So with
#each iteration (what recursion basically is in some case) we delimit the
#string by one. 
#Now it is quite similar to the 'necklace loop' because on the memory
#stack, we have a FILO-sorting (First in, last out). 
#So the last character pushed onto the stack will be the first character
#pulled from the stack and vice versa. This is why we reach a reversed
#sorting in the end. 
#--a--b--c--d-- string
# --b--a------- stack

#This video explaines it perfectly: 
#https://www.youtube.com/watch?v=0087XazbD3U

#-> The trick is to call the function by itself again and just THEN 
#adding the x[0], so the first element. -> recursionReverse(x[1:])+x[0]
#-> +x[0] outside the brackets of function calling 
#So we generate a finite loop of removing the first element and putting 
#it FILO on the stack until we have reached the last element, 
#where len(x)==0.


#_______________________solution 4: using stack_________________________

			
# Function to create an empty stack.  
# It initializes size of stack as 0 

# Function to determine the size of the stack 
def size(stack): 
    return len(stack) 
  
# Stack is empty if the size is 0 
def isEmpty(stack): 
    if size(stack) == 0: 
        return true 
  
# Function to add an item to stack .  
# It increases size by 1  
def push(stack,item): 
    stack.append(item) 
  
#Function to remove an item from stack.  
# It decreases size by 1 
def pop(stack): 
    if isEmpty(stack): return
    return stack.pop() 
  
# A stack based function to reverse a string 
def reverseStack(x): 
    n = len(x) 
      
    # Create a empty stack 
    stack = []
  
    # Push all characters of string to stack 
    for i in range(0,n,1): 
        push(stack,x[i]) 
  
    #Making the string empty since all  
    #characters are saved in stack  
    x=''
  
    #Pop all characters of string and  
    #put them back to string 
    for i in range(0,n,1): 
        x+=pop(stack) 
          
    return str(stack) 

#What this function does is basically just exactly what the pearl bracelet
#method does. Items are pushed in correct order onto the stack. So the 
#stack then consists of --a--b---c.
#The pop function then removes the list element at given index when called 
#with pop(index). If no index is given the function defaults 
#to popping out the last item of the list like in our example.
#-> So after string is being emptied the items get popped on it in reversed
#order --c---b----a--
#So basically we are using this little insight on pop() and let the work
#be done by this built in list function. 



#___________________________APPENDIX____________________________________

#during my reasearch I found the built in list function reverse() but 
#as it seems this function only switches elements in a list and doesn't
#change anything on the string. See documentation here: 
#https://www.programiz.com/python-programming/methods/list/reverse 
