# Mwenje kiff
# 12/02/2026
# STRING FORMATTING

# Get string length
sentence = "I love children"

string_length = len(sentence)

print(f"the length is {string_length}")

# Splitting string
# sentence_2 = "math physics"

# split = sentence_2,split("")

# print(f"the first subject is:", split[1])

# Make everything capital
code = "ub2fgfdsv"
capitalized = code.upper()
print("New code: ", capitalized)
# Make to lower
small = code.lower()
print("New code : " , small)

# Replacing characters in string

balance = "100kes"
amount_added = "50kes"
cleaned_balance = balance.replace("kes" , "")
print ("cleaned_balance: " , cleaned_balance)

cleaned_amount_added = amount_added.replace("kes" , "")
print("cleaned amount added:" , cleaned_amount_added)

new = int(cleaned_balance) + int(cleaned_amount_added)
print(f"the new balance is : new" ,new )

# Mpesa message
amount = "Ksh40"
first = "CONFIRMED"
third = " you have received"
fourth = "from Bob.New Mpesa balance is 50 kes"

mpesa = capitalized + " " + first + " " + third + " " + amount  +" " + fourth
print(mpesa) 
