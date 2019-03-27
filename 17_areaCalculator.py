'''The user will be prompted with a menu where he/she will select a shape 
Then the user will give the appropriate information needed to solve for 
the area, and the computer will give the area! Hope you all have taken 
geometry!'''

#Basics
#Rectangle      axb
#Square         axa
#Triangle       1/2ah (where a is length of ground site and h is height
#Circle         πxr**2 (where r is the radius)

#Fancy
#Parallelogramm axh (where a is length of ground site and h is the heigth)
#Trapezoid      1/2 (a+c ) xh where a is the ground, c the opposite site 

#I'll just do one of them so everything else can be solved via adapting
#my procedure for the rectangle

#As I found out when doing a multi-line-string with ''' Python also 
#takes care of newlines and other formatting by itself. 
form=input("""Hello. I'll do your geometry homework. What shape do you
want me to calculate the area for? 

a) Rectangle 
b) Square 
c) Triangle
d) Circle
e) Parallelogramm  
f) Trapezoid \n 
Enter letter here  \n > """)
 
if form == 'a':
    print("""
    You chose recangle:
            
                a
       ~~~~~~~~~~~~~~~~~
       |               |
     b |               |   
       ~~~~~~~~~~~~~~~~~
        
    Please give me the lenth a and the height b of the rectangle, 
    both in the same length unit""")
        
    length= input("The length is \n > ")
    height= input("The heigth is \n > ")
    print("Calculating the area...")
    print("\nThe area for your rectangle with length ",length, " and height " ,height, "is ",int(length)*int(height)) 
