#Mwenje Kiff

class Human :

    type ="Mammal"
    legs = 2
    brain = True
    city = "Nairobi"

    #we then create a constructor for the class /object
    #The contractor will be used
kiff = Human("kiff" , 18)
tessie = Human("tessie" ,10)
#LET THE HUMANS CREATED DO THINGS
kiff.tell_story()
print ("kiff's age is" ,  kiff.human_age)
#MODIFY ONE OF THE OBJECTS
kiff.city = "thika"
kiff.city = ("kiff's city is" , kiff.city)
tessie.city = ("tessie's city is" , tessie.city)

