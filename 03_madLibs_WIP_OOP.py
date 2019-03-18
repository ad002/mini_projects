##THIS WAS AN EXPERIMENT TO FIND AN OOP SOLUTION: FOUND ONE WITH 2 LINES 
##of CODE EACH. THIS IS A WORK IN PROGRESS VERSION###

#How it works: 
#"Once that _____ (adjedtive) music comes down, it's time to shut 
#down your acceptance speech"
#"Basketball is the _______(bodypart) sport in the world"

#So we have
#1. empty sentences 
#2. Adjectives
#3. Nouns
#4. Verbs

#We'll fit in verbs in verb-missing sentences, adjectives in adjective
#missing sentences and so on. 

#I guess we'll go with a list for the words. After the user input we'll 
#shuffle them and insert them in the preset sentences that are missing 
#words, but have some placeholder varibale like:
#exampleSentence = print("We love it how you " +verb+ "with you mother")

import random 


def getInput():
    '''Get input from user and directly put it on empty list'''
    adj_in=input("Please enter some adjectives: \n > ")
    verbs_in=input("Please enter some verbs: \n > ")
    nouns_in=input("Please enter some nouns: \n > ")
    
    return adj_in, verbs_in, nouns_in
    
    #An addition would be that the user can input, press enter and enter
    # another or at least: That every input seperated by a space or a , 
    #gets stored as a single string! 
    #So if we say: Please enter adjectives seperate by a comma, we have
    #to split the string at that position and append them all independently
    #The split method returns a new array. 
    #Example: txt = 'Hello, this is a cool string, or not?'
    #x=txt.split(', ')
    #print(x) 
    #['Hello','this is a cool string', 'or not?']
def experiment():
    txt= 'This, is, such, a cool string'
    x=txt.split(',')
    print(x) #['This', ' is', 'such', ' a cool string']
    
    txt2='Whereas this string will be separated by spaces'
    y=txt2.split(' ')
    print(y)#['Whereas', 'this', 'string', 'will', 'be', 'separated', 'by', 'spaces']
    
    txt3='This, is, another, example, better separated than txt/x'
    z=txt3.split(', ')
    print(z)#['This', 'is', 'another', 'example', 'better separated than txt/x']


def generateSentence(adj_in, verbs_in, nouns_in):
    '''Place user input into sentences after being shuffled'''
    #Generate a random number (which isn't  greater 
    #than the last element-position-number of  our verb list 
    #List index:     0 1 2 3 4 5 
    #List element:   1 2 3 4 5 6
    adj_in.split()
    verbs_in.split()
    nouns_in.split()
    #print("Example sentence where the " +verbs[random.randint(0,(len(verbs)-1))]+" comes into place.")
    print(adj_in, verbs_in, nouns_in)
    return adj_in, verbs_in, nouns_in


def main():
    print('''Welcome to the mad libs game. We'll generate some crazy 
    #sentences based on your input-words''')
    getInput()
    #print("You have entered " +str((len(adjectives)+len(verbs)+len(nouns))) +" words.")
    generateSentence(adj_in, verbs_in, nouns_in)
    #experiment()
    
    

if __name__=="__main__":
    main()
    
