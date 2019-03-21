x=input("""Please give me a word to check wheter it's a palindrome or 
not \n > """)

#First thought about datatype set() which is an unordered collection of 
#unique elements. But doesn't make sense as being readable forwards and 
#backwards has nothing to do with unique elements 

def checkPalindrome(x):
    #If the string in backward order = string in forward order
    #Put both to lowercase to disregard capitalization 
    #Another things is that I have to remove spacing as there are 
    #palindromes being longer than 1 word so I replace whitespace " " 
    #with no space ("")
    #If there is a . at the end of a palindrome, remove it. 
    x=x.lower().replace(" ","").replace(".", "")
    
    if x[::-1]==x.lower():
        print("It's a palindrome!") 
    else:
        print("It's not a palindrome!")
    
checkPalindrome(x)



#__________________________REMOVING (WHITE)SPACE________________________
#https://www.journaldev.com/23763/python-remove-spaces-from-string
teststr=("""A string to remove whitespace \s as well as newlines \n 
 and \t tabs and carriage returns \r (bascically just
newline as \n) to be removed""")
#\n \t \s \r [...] are so called 'Escape Codes'

#1 Replace Method
#Replacing " " whitespace with nospace ""
print(teststr.replace(" ",""))

#2 Translate method (import string)
#Gets rid of all whitespaces as well as newlince characters using string
#The SAFEST method
import string
print(teststr.translate({ord(c): None for c in string.whitespace}))

# Sub Fucntion (import RegEx) 
#Gets rid of all the white space 
import re 
print("Remove whitespace w/ re \n", re.sub(r"\s+", "", teststr), sep='')
#th \s removes whitespace as \s is Escape Code for that   

