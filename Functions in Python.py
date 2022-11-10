#Functions in Python 

#Simple Function

def greet():                                        #defining the function
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
    
greet()                                              #calling the function 

#Functions that allows for input 

def greet_with_name(name):                           #in the brackets () name is the parameter
    print (f"Hello {name}")
    print(f"How do you do {name} ?")
    print(f"Isn't the weather nice today {name} ?")
    
greet_with_name("Kunj Maheshwari")                   #in the bracket() "Kunj Maheshwari" is the argument

#Functions with more than one parameter

def greet_with_name_and_location(name,location):
    print(f"Hello {name}")
    print(f"How's the weather of {location}?")    
    
greet_with_name_and_location("Kunj", "Vidisha")

