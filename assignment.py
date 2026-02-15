# SIN/COS/TAN(-180-+180,30)
import math
# for x in range (-180,180,30):
#     print (math.sin(x))
#     print (math.cos(x))
    # print (math.tan(x))
    
# TABLE OF SQUARES

# Define the range for the table
# limit = 10

# print(f"{'Number':<10} | {'Square':<10}")
# print("-" * 23)

# for n in range(1, limit + 1):
#     square = n ** 2
#     print(f"{n:<10} | {square:<10}")

# GEOMETRIC PROGRESSION
a = int(input("Enter  a : "))
r = int (input("Enter r : "))
n = int( input ("Enter n :"))
# nth_term = a*r**(n-1)
# print (f"The nth term is{nth_term} ")
sum_1 = ((a*(1-r**n))/1-r)
sum_2 = ((a*(r**n-1))/r-1)
if r < 1 :
    print (f"The sum of numbers if r < 1 is {sum_1}")
if r > 1 :
    print(f"The sum of numbers if r > 1 is {sum_2}")