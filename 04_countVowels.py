import time #just for performance check
x = input("Enter word to count vowels \n > ")

def sol1(x):
    #Guess this solution will be quite ressource heave when approaching
    #long strings. 
    #So I added another solution and some code to check the execution time
    #as I will compare both programms performance on large strings 
    #like from loremipsum.com
    #Important: Start Time checking after user input
    start=time.time()
    #Just the Loop for i in x
    #prints out every single letter of inputted string in one single row
    #/Loops trough the whole input 
    count=0
    for i in x:
        #print(i)
        if 'a' in i:
            print("i found an a")
            count+=1
        if 'e' in i:
            print("I found and e")
            count+=1
        if 'i' in i:
            print("I found an i")
            count+=1
        if 'o' in i:
            print("I found an o")
            count+=1
        if 'u' in i:
            print("I found an u")
            count+=1
    print("I found " +str(count) +" vowels so far")
    end =time.time()
    print("This execution took :" +str(end-start))

def sol2(x):
     #this seems only to print out number of letters 
    start=time.time()
    #One golden rule I found now is to avoid nesting as much as possible
    count=0
    for i in x:
        if ('a' or 'e' or 'i' or 'o' or 'u') in i:
            print("I found a vowel")
            count+=1
            
    print("I found "+str(count)+" vowels so far")
    end=time.time()
    print("This took: "+str( start-end))

def sol3(x):
    #this doesn't work at all
    start=time.time()
    count=0
    for i in x:
        if any('a','e','i','o','u' in i)==True:
            print("Found a vowel")
            counter+=1
    print("Found " +str(counter)+" vowels")
    
    
def sol4(x):
    #This is an online solution
    start=time.time()
    counter=0
    
    #Take something as an input, string
    def checkVowel(a):
        #Lowercase just to get sure everything is included
        return a.lower() in ['a', 'e', 'i', 'o','u']
    
    #As long as counting variable i hasn't reached length of input string
    for i in range(len(x)):
        #if string at position of counting variable i is a Vowel (==True)
        #As checkVowel returns boolean 
        if checkVowel(x[i]):
            counter+=1
        
    print("Found " +str(counter) +" vowels")
    end=time.time()
    print("This took: "+str( start-end))
        

def main():
    sol1(x) #my_Version, working, but slow
    #sol2(x)
    #sol3(x)
    sol4(x)#Online Version, very lean 

if __name__ =="__main__":
    main()

