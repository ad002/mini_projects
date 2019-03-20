#Take user input 
x=input("Gimme some text to reverse it \n > ")
#Using slicing as it is the shortest version
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

#or how I would call it: the necklace method 
def reverse(x):
    #Create empty string 
    str=''
    #store list elements of x temporarily in i, in this case the first one
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
	#the string(i+str), which consists of the 's' already so now we have 
	#'ts'
	#-> It's like putting the first, second, third element of the string
	#always as the new first element of the str variable which results
	#in the first element of our input to be the last of the output, 
	#-> Just like putting beads from one necklace to another 
	# --a--b--c--d-- 1st necklace
	# --b--a-------	 2nd necklace, always taking the first element of
	#		 one to be the new first element of two until the next
    return str

#___________________Solution 3: using recursion________________________



#during my reasearch I found the built in list function reverse() but 
#as it seems this function only switches elements in a list and doesn't
#change anything on the string. See documentation here: 
#https://www.programiz.com/python-programming/methods/list/reverse 
