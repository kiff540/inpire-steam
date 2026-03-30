# Mwenje kiff
# 18/02/2026
# PROGRAM TO SHOW DICTIONARIES IN PYTHON

car = {"Model" : "rs7" ,
      "Make" : "Audi" ,
      "Color" : "white"}
print (car)

print (car["Model"])

students = {"Kiff" : 24 ,
        "Mark" : 13,
        "Tessie" : 14,
        "Tracy":12 ,
        "John" :23}
for key in students :
    print(key)

    for val in students.values():
        print(val)