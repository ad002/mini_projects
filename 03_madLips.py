import random 

print("""Welcome to MadLips Game. You'll have to enter some words and
we'll generate funny sentences out of it """)

#Getting user input and splitting it in single words
nouns = input("Enter nouns separated by space\n"+"> ").split()
verbs= input("Enter verbs separated by space\n"+"> ").split()
adj= input("Enter adjectives separated by space\n"+"> ").split()

#Split returned list. Now Shuffle elements and put one in sentence
print("a premade " +nouns[random.randrange(0,len(nouns))]+" for testing")
print("a premade " +verbs[random.randrange(0,len(verbs))]+" for testing")
print("a premade " +adj[random.randrange(0,len(adj))]+" for testing")


