#___________________ACCESSING STRINGS EXPLAINED_________________________
s='Don Quijote'

#https://thispointer.com/python-how-to-access-characters-in-string-by-index/

#In Python indexing of strings starts from 0 till n-1, where n is the 
#size of the string. 
#Acessing elements happens just like when accessing elements of a list 

print(s[5]) #will return the element at index 5, which is the 6th element in 
#total as indexing starts with 0. 
#So in that case it's the 'u' as string index 0 is 'D'

#________________ACCESSING STRINGS BY NEGATIVE INDEX____________________
print(s[-1]) #returns last character of the string, in that case 'e'
print(s[-2]) #returns second last character of string, 't'
#if string size is n then string[n-1] will return the first character 
#of a string, n  is expressed by len(string)
print("First character of string:",s[-len(s)])

#_________________SLICING STRINGS EXPLAINED_____________________________
#https://www.pythoncentral.io/cutting-and-slicing-strings-in-python/

#If you want to extract a chunk of more than one character with known 
#position and seize, you can use slicing. By defining the starting pos. 
#of the piece we want and the end
print(s[0:2])#prints elements from 0 to index 2 excluding index 2 so 
#this will be the elements/characters at index 0 1 ('Do')
#So let's think of the 2 as specifiying the first character i don't want
#Everything UP to 2, not including 

#For any value of index n the value of s[:n] + s[s:] will always be the 
#original string
n=2 #for example
print(s[:n] + s[n:]) #out: 'Don Quijote' 
#-> If the indexing mechanisms were inclusive, the char. at position n 
#would appear twice! 

#If left empty:
print(s[:2]) #defaults to zero as first element 
print(s[2:]) #defaults to highest position in string as end 
print(s[:]) #prints the whole original string

#Just as before, you can use negative numbers as indices, in which case
#the counting starts at the end of a string (with an index of -1) instead
#of the beginning
print(s[-7:-3]) #out: 'Quij'

#_________________SKIPPING CHARACTERS WHILE SPLITTING STRINGS___________
#________________________3rd PARAMETER: STRIDE______________
#add a third (and last) parameter which specifies the 'stride' (Schritt)
#or: How many characters you want to move forward after each character is 
#retrieved from the original string. Just easy: The step size when re-
#trieving characters

#The first retrieved character always corresponds to the index before the
#colon; but thereafter, the pointer moves forward however many characters 
#you specify as your stride, and retrieves the character at that position.
#And so on, until the endinh index is reached or exceeded

#If, like just before, the paramter is omitted (ausgelassen), it defaults 
#to 1, so that every character in the specified segment is retrieved. 
print(s[4:8]) #out: 'Quij'
print(s[4:8:1]) #changes nothing, as 1 is our default step size 
print(s[4:8:2]) #returns every second character, out: Qi

#You can specify a negative stride, too. As you might expect, this indicates
#you want python to go backwards when retrieving characters
print(s[8:4:-1]) #walks backwards from element 8 to element 4 exclusive, 
#so basically from element 8 to element 5
#out: 'ojiu'
#0 1 2 3 4 5 6 7 8 9 10 
#D o n   Q u i j o t e

#Since going backwards it makes sense for the starting index (the first 
#of the two) to be higher thn the ending index. Otherwise nothing 
#would be retuned 
print(s[4:8:-1)]) #out: ''

#For that reason, when specifiying a negative stride, but omit (leave out)
#either the first or the second index, Python defaults the missing value to 
#whatever makes sense in the cicumstances. The start index to the end 
#of the string, and the end index to the beginning of the string. 
#So here we also switch directions, not just concerning step size. 
print(s[4::-1]) #End index defaults to the beginning of the string
#out: 'Q noD'
print(s[:4:-1])#Beginning index defaults to the end of the string
#out: 'etojiu'


