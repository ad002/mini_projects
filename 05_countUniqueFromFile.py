
#x=open("text.txt","r") now type: '_io.TextIOWrapper', has no split() 


#flatten input file into a single flat list of words 
#with open('text.txt','r') as f:
#    [word for line in f for word in line.split()]

with open('05_text.txt','r') as f:
    x=f.read().replace('\n', '')

def count_all(x):
    '''Counts all words w/o considering doubles'''
    #the length of the list = words in it, typecast it into a string
    print("Your text has "+ str(len(x))+" words in total")

def uniqueWords(x):
    '''Keep only unique words'''
    #list of words converted into a set 
    #which will by default have only unique values
    print(str(len(set(x)))+' of these words are only appearing once')
    

def main():
    count_all(x)
    uniqueWords(x)
    
    
if __name__=="__main__":
    main()
