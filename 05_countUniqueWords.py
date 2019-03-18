#import collections #for duplictes
x=input("Enter words to be counted: \n > ")

#Option to count words in longer texts
#y=open("text.txt","r")

def count_all(x):
    '''Counts all words w/o considering doubles'''
    #Splits input-string in single words stored in a list, then just 
    #takes the length of the list and typecasts it into a string
    print("Your text has "+ str(len(x.split()))+" words in total")

#USELESS#
def checkifDouble(x):
    #set() sorts all the elemnts in the list in ascending order
    #returns true if there is a least one double elment
    return len(x.split()) != len(set(x.split()))

#USELESS#
def printifDouble(x,y): #returns true or false
    print("Check if doubled words: " +str(checkifDouble(x)))
    
#USELESS#
def removeDoubleKeepRest(x): #Doesn't work for strings as it appears
    #https://www.peterbe.com/plog/uniqifiers-benchmark
    seen = set()
    seen_add = seen.add
    return [i for i in x if not (i in seen or seen_add(i))]
    

#USELESS#
def deleteExceptDoubles(x): #deletes everything except the letters apperaring 
    #more than once
    print([item for item, count in collections.Counter(x).items()if count>1])


#USELESS
def delDuplicates(x):
    global unique 
    unique=[]
    #Put item on unique-list until we have reached the end of the list x
    #as long as item has not already moved from list x to list unique
    [unique.append(item) for item in x if item not in unique]


def uniqueWords(x):
    '''Keep only unique words'''
    #Split input string by space (split() w/o parameters splits by 
    #space, returns a list, then list converted into a set 
    #which will by default have only unique values
    print(str(len(set(x.split())))+" of these words are only appearing once")
    



def main():
    count_all(x)
    uniqueWords(x)
    
    
    

if __name__ == "__main__":
    main()

