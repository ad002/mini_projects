'''A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers'''

#Tasks:
#Check whether Palindrome : Convert int to str, Check whether string 
#(=number) forwards == str backwards

#Find the largest divisors of this number using % modulo (???)

#Largest Palindrome made from product of two 3 digit numbers would be 
#a 6 Digit Palindrome 

number=9009

def checkPalindrome(number):
    #For explanation on string slicing see ' 06_reverseString' or 
    #'07_strings+slicing' 
    if str(number)==str(number)[::-1]:
        return True
    else: 
        return False

print("Number Palindrome == ",checkPalindrome(number))  

factorials=[]

def getFactorial(number):
    #List where we put all numbers which are possible factorials of 
    #the number 
    all_factorials = []
    #starting with one as we would have a problem in line 44 when modulo
    #by zero
    for i in range(1,number+1):
        all_factorials.append(i)
    
    #print(str(all_factorials))
    
    #Start with 1 as we can't divide by zero (line 44) 
    for i in range(1,len(all_factorials)):
        #if our number is evenly dividable ( with zero rest) by any 
        #factorial of all our factorials, put it on the list 
        if number %i ==0: 
            factorials.append(i)

getFactorial(number)
print("Factorials of ", number, " are: ", factorials)


#now what we have to do is get only the second digit factorials from 
#the list all_factorials 
two_digit_factorials=[]

#Loop trough all the factorials
for i in factorials: 
    #if the element of factorials represented by i is 2 digits 'long'
    if len(str(i))==2:
        #add it to the list 
        two_digit_factorials.append(i)

#Get the first largest factorial 
max1=max(two_digit_factorials)
#Remove the last element from list with pop as it is now saved in 
#max1 variable so we can get the "second" largest factorial which is
#now the new max of the list
max2=max(two_digit_factorials)
#max2=max(two_digit_factorials)

print(max1,max2)
 
#Problem is: Now I have to Reverse-Engineer this. Because I have to find 
#the largest two factorials consisting of a three digit number forming
#a six digit palindrome. 




    
