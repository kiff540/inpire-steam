# Mwenje kiff
# 18/02/2026
# PROGRAM TO SHOW LISTS IN PYTHON

#******************************************
friends = ["sophie" , "mia" ,"violet" ,"crystal"]
print (friends)
#******************************************
#SORT()
friends.sort()
print(friends)
#******************************************
#REVERSE
friends.reverse()
print(friends)
#******************************************
#APPEND
friends.append("willow")
print (friends)
#*****************************************
#ADDING A NEW LIST
new_friends = ["kiff" , "violet"]
print(len(new_friends))
students = new_friends + friends
print (students)
#***************************************
#POP
students.pop()
print (students)
#**************************************
#INSERT
students.insert( 4 , "jane")
print (students)
students.insert(7 ,"bob")
print (students)
#**************************************
#REMOVE
students.remove("violet")
print (students)
#************************************
#COPY
new_students = students.copy()
print (new_students)
#************************************
