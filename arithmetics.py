#Mwenje kiff
# 13/02/2026
# PROGRAM TO PERFOM ARITHMETIC OPERATIONS

f_number =12 
s_number= 34
sum_numbers = f_number + s_number 
diff_numbers = f_number - s_number
mult_numbers = f_number * s_number
div_numbers = f_number / s_number#

print ("The sum of the numbers is %d" %sum_numbers)
print ("The difference of the numbers is %d" %diff_numbers)
print ("The multiplication of the numbers is %d" %mult_numbers)
print ("The division of the numbers is %0.2f" %div_numbers)

#MODULUS/REMAINDER
print (7%3)

# EVEN AND ODD NUMBERS 
for x in range (0,20):
    if x%2 == 1:
        print (f"{x} is odd")
    elif x%2 == 0 :
        print(f"{x}is even")