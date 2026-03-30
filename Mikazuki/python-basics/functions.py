


def cook_egg ():
    oil = "200ml"
    pan = True 
    fire = True
    eggs = 2

    print (f"The pan is {pan},and the fire is {fire} ,add {oil} amount of oil and cook {eggs} eggs")
print ("Here is statement 1")
print ("Here is statement 2")
print ("Here is statement 3")
cook_egg()


#RIDE FARE FUNCTION
def create_fare (route ,distance , is_rush_hour):
    fare = distance *10
    if is_rush_hour == True:
        fare = fare * 1.5
        print(f"The fare on route {route} is {fare}")
        return fare

rush_hour = True
returned_fare = create_fare("Juja-thika" , 7 , rush_hour)
print(f"The returned fare is : {returned_fare}")
#PASSING A LIST AS A PARAMETER
def write_all_interests(interests):
    for interest in interests:
        print(f"I love {interest}")
all_interests = ["girls","children"]
write_all_interests(all_interests)
