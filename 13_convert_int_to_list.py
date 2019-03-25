number=int(input("Give me a number \n > "))


#_______________________CONVERTING INT TO LIST__________________________


#__________________________SOLUTION 1___________________________________
#This puts all elements from zero till the number in a list
def convert2List1(number, numbers =[]):
    for i in range(0,number+1):
        numbers.append(i)
    print("This is solution #1 \n ", str(numbers))
convert2List1(number)



#________________________SOLUTION 2_____________________________________
#This just splits the inputted number in its single digits and puts 
#them in a list one by one 
def convert2list2(number):
    #Convert int to str first, then use map to apply int on it 
    print("This is solution #2 \n ", list(map(int,str(number))))#returns a map object
convert2list2(number)



#_____________________________SOLUTION 3________________________________
numbers=[int(x) for x in str(number)]
print("This is solution #3 \n ", numbers)



#_____________________________SOLUTION 4_______________________________
numbers=[]
for i in str(number):
    numbers.append(i)
print("This is solution #4 \n ", numbers) #output: ['1', '2', '3']

    
#____________________________SOLUTION 5_________________________________
print("This is solution #5 \n ", list(str(number))) #['1', '2', '3']
