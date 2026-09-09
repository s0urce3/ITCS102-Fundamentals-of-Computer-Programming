#multiple if and else conditions

#create a python programming that would capture age group

name = input("Please state your name--> ",)
age = int(input("please state your age----> "))

if age >=0 and age <=5 :
    print("The age is considered as INFANT")

elif age >=0 and age <=5 :
   print("that age is considered as INFANT")

if age >=6  and age <=12:
    print("The age is considered as KID")

elif age >=6 and age <=12:
   print("that age is considered as KID")

if age >=13 and age <=15:
   print("The age is considered as PRE-TEEN")

elif age >=13 and age <=15:
   print("that age is considered as PRE-TEEN")

if age >=16 and age <=19:
 print("The age is considered as TEENAGER")

elif age >=16 and age <=19:
   print("that age is considered as TEENAGER")

if age >=20 and age <=29 :
 print("The age is considered as EARLY ADULTHOOD")

elif age >=20 and age <=29:
  print("that age is considered as EARLY ADULTHOOD")


else :
    print("age INVALID")