x=input("Enter words to be counted: \n > ")

#Option to count words in longer texts
y=open("text.txt","r")

def count_all(x,y):
    inp= input("Do you want string or text to be analysed? \n <s/t> ")
    if inp=='s':
        #Backwards: Split string returns list, get length of list, transform int
        #to string, split splits by space in default
        print("Your text has "+ str(len(x.split()))+" words")#counts any word
    
    if inp=='t':
        #returns a list 
        y=y.readlines()
        for line in y:
            Type=line.split()
        print(y)
        #y.close()
        


def checkifDouble(x,y):
    #set() sorts all the elemnts in the list in ascending order
    #returns true if there is a least one double elment
    return len(x.split()) != len(set(x.split()))


def countUnique(x,y):
    print("Check if doubled words: " +str(checkifDouble(x)))

#if there is any double in the dataset, exclude them from counting 

def main():
    count_all(x,y)
    



if __name__ == "__main__":
    main()

#Checking functionality of set()
#Works for every iterable sequence like list, tuple or dictionary
#returns sorted, non repeating elements
#e.g. When used for a list full of numbers, numbers get sorted and doubles
#are removed
#When used for a string, they are not sorted, but at least doubles are 
#removed
#print("There shouldn't be any doubles now: " +str(set(x.split())))
