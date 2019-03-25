'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

#Empty list for prime factors
number= int(input("Give me a number to check prime factors \n > "))
all_numbers=[]

#Empty list for primes
primes=[]

#Getting all elements until our target number in a list, as indexing 
#starts with zero, we have to add +1 to number 
for i in range(0,number+1):
    all_numbers.append(i)

#Now we have to check wheter the number is a prime factor or not. 
#The Function is actually taken from here: https://bit.ly/2TXNSo8 

def isPrime(number):
    #All numers below 2 aren't primes 
    if number < 2:
        return False
    #if mumber is divisible by 2 without rest its defintely not a prime 
    #if number =2 we don't want to evaluate whether number is a prime 
    #so let's exclude it via number != 2
    elif number !=2 and number%2==0:
        return False 
    else:
        return all (number % i for i in range (3, int(number**0.5)+1)) 
    #all() method returns True when all elements in the given iterable
    # are True. If not, it returns False. 
    #Starting from 3 (as we excluded everything equal or below 2) we 
    #divide the number only until it's square root (number **0.5). 
    #Sqaure root +1 `(?) -> See line 14
    #Why Square Root? Let's say a=16, the sqaure root of 16 is 4, so we
    #don't need to evaluate until 15 to say that 16 is not a prime
    #If number is divisible by something larger than 3, the output will 
    #be False as it's not a prime then 
 
#Put all primes smaller than the entered number on a separated list     
for i in all_numbers:
    if isPrime(i): #==True 
        primes.append(i)
    #Now we have all possible primes for prime factorization in a list

#Comment this line out if you are dealing with small numbers
#print("Here you have all the primes ", primes)
 
#Empty list for prime factors 
prime_factors=[]

def isPrimeFactor(number):
    #take extracted primes in charge. (primes) 
    #As long as we haven't reached the end of our prime-number-list
    for i in primes: 
        #Check whether number divided by prime number has a rest. If not,
        #it's a prime Factor 
        if number % i == 0: 
            #Put prime factor on our list 
            prime_factors.append(i)
        
            
isPrimeFactor(number)
print("The prime factors of your input ", number, "are ", prime_factors)

#Now we just want to know what is the LARGEST prime factor of all the 
#calculated prime factors. So following my intuition there is already
#a built in function for getting the biggest element out of a list so we
#jst add it to our output. 

print("The LARGEST prime factor of ", number, "is ", max(prime_factors))

print(""" \n Calculating largest prime for 600851475143 drove my pi out  
of memory so I checked for 600851475 which also is too heavy so I tried
600851 which has a largest prime factor of 20719""")

