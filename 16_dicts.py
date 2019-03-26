#Short excursion on how to use dicts as I was trying to solve euler
#project #4 largestPalindrome by using it 

#It's best to think of a dictionary as set of key:value pairs with the 
#requirement that the keys are unique (within one dictionary)

#Ressources:
#Python documentation
#https://bit.ly/1XPsXyN

#Python for Beginners:
#https://bit.ly/2YroQMz

#_____________________Creating empty dicts______________________________
empty_dict = dict()
#or:
emtpy_dict={}

#___________________Creating dicts and assinging values_________________
new_dict=dict(a=1,b=2,c=3,d=4)
print(new_dict) #{'a': 1, 'c': 3, 'b': 2, 'd': 4}

released = {
        #key    : value    
        "iPhone":2007,
        "iPhone 3G": 2008,
        "iPhone 4": 2010
        }
print(released)
#{'iPhone 3G': 2008, 'iPhone 4': 2010, 'iPhone': 2007}


#_____________________Adding a value to a dict__________________________
#Syntax: myDict[key]=value
released["iPhone 5"]=2013
print(released)
#{'iPhone': 2007, 'iPhone 4': 2010, 'iPhone 5': 2013, 'iPhone 3G': 2008}

#________________Removing a key and a value from the dict_______________
del released["iPhone"]
print (released)

#___________________Checking the length of a dict_______________________
print(len(released))

#______________________Testing the dictionary___________________________
my_dict={'a':'one','b':'two'}
print('a' in my_dict) #True
print('c' in my_dict) #False

num_dict={1:'abc', 2:0,3:23}
print(num_dict) #{1: 'abc', 2: 0, 3: 23}

#______________________Get Value of specific Key________________________

print(released.get("iPhone 3G","none"))#2008


#__________________________get only KEYS________________________________
phones = released.keys()
print(phones)

#or print them out like this: 
print("This dictionary contains these keys: ", " ".join(released))

#or like this
print("This dictionairy contains these keys: ", "",released.keys())


#__________________________get VALUES___________________________________
print("Values: ")
for year in released:
    releases=released[year]
    print (releases)

print("This does exactly the same, just with another counting variable: ")
for i in released:
    values=released[i]
    print (values)
#2013
#2010
#2008


#_____________________Print all KEYS with a for-Loop____________________
print("iPhone releases so far: ")
for release in released:
    print (release)


#____________________Print all KEYS and VALUES__________________________
print("iPhone releases and years so far")
for key,val in released.items():
    #Print key, delimited by an arrow
    print(key, "-> ",val)
     

#_______________________SORTING the dicitonary__________________________
for i in sorted(released, key=len):
    #Printing keys as well as values 
    print (i, released[i])
#iPhone 5 2013
#iPhone 4 2010
#iPhone 3G 2008

#__________________________Counting (unique) elements___________________
count = {}
for element in released:
    count[element] = count.get(element, 0) + 1
print count

#{'iphone 3G': 1, 'iphone 4S': 1, 'iphone 3GS': 1, 'iphone': 1, 
#'iphone 5': 1, 'iphone 4': 1}
