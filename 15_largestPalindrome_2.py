'''A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers'''

#So I think what I first have to do is get all possible factorials. 

#Guess the largest possible palindrome made from two 3 digit numbers 
#would be 999999 BUT: Can it be calculated by two three digit numbers?

def checkPalindrome(number):
    #For explanation on string slicing see ' 06_reverseString' or 
    #'07_strings+slicing' 
    if str(number)==str(number)[::-1]:
        return True
    else: 
        return False


def returnFactorial(number):
    #Set i as in the same range as the number, exclude 0 to have no 
    #division by zero 
    for i in range(1,number+1):
        if number % i == 0:
            print(i)


def returnThreeDigitFactors(number):
    #set i as same range as the number we want the factors to, exclude
    #0 to have no division by zero 
    for i in range(1,number+1):
        #If number divided by counter (counting till the length of the 
        #number) it is a divisor/factor 
                            #Just a BIT of typecasting
        if number%i==0 and len(str(number%i))==3:
            print(i)
            
#returnFactorial(320)



#Get all possibe 6 digit palindromes 
palindromes=[]
for i in range(0,1000001):
        
        #if str of number read forwards = str of number read backwards it's 
        #a palindrome
        #One digit long words were also counted as palindromes so we exclude
        #that 
    if str(i) == str(i)[::-1] and len(str(i))!=1:
        palindromes.append(i)

#What I have to do now is move the palindrome list backwards, because we
#want to find the gand find the largest palindrome. And the one that 
#can be made of two 3 digit factors

#I think I need a dict datatype for this kind of question. So for every
#palindrome, store the 3 digit factors because else I'll get a wild 
#collection of factors not allocated to it's fitting palindrome 

#What I observed is following: 
#See for example palindrome 1221. The factorials are following:
#1
#3
#11
#33
#37
#111
#407
#1221
#-> It's always the first and the last element that make a factor-pair, 
#so e.g. 1x1221, 3x407 etc. 

    

dict_for_value_pairs={}
#Adding palindromes as keys to the dict
#for i in palindromes:
    #as values take the Factors for this Palindrome
    #dict_for_value_pairs[i]=returnFactorial(i)
    #->>>> Problem here is that returnFactorial() prints the factorials
    #and I have no clue how to insert them directly fitting to it's palindrome
    



print(returnFactorial(palindromes[1988]), " are the factors for palindrome ", palindromes[1988])    
print(len(palindromes))#1989 Palindromes 
#print(palindromes)

#print(returnThreeDigitFactors(palindromes[1988]), "are the three digit factors for palindrome ", palindromes[1988])
print(dict_for_value_pairs)



#_______________TUTORIAL: GET LIST ELEMENTS IN REVERSED ORDER___________
#You can move through a range in negative direction via 
def rangeReverse1():
    for i in range(0,10,-1):
        print(i) 

#or you could do: 
def rangeReverse2(palindromes):
    #but this will only print a 1,2,3,4...991 for every element we have 
    #in the palindromes list as we use the len() function 
    for i in reversed(range(len(palindromes))):
        print (i) 

#While this gives us what we want: The list palindromes in reversed order
def rangeReverse3(palindromes):
    for i in reversed(palindromes):
        print(i)



