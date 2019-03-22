#If we list all the natural numbers below 10 that are multiples of 3 or 
#5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

#Empty list for numbers 0-1000
x=[]
#Empty list for multiples
y=[]
#fill list with numbers from 0 to 1000, 1001 first number that won't be
#appended as indexing starts with 0
for i in range(0,1001):
    x.append(i)

#as long as we haven't reached end of list x 
#every element of x is temporarily stored in i during loop 
for i in range(len(x)):
    #If modulo =0, it's a mulitple
    if i%3==0 or i%5==0:
        #If multiple, put on our multiple list
        y.append(i)
        
        
#sum(y) adds up all elements of list y, ergo all multiples 
print("The total sum of all multiples of 3 and 5 below 1000 is {}".format(sum(y)))

