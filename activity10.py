#Basic if else program

username = "Venn"
password = "Marc"

u = input("Input USERNAME -->  ")
p = input("Input PASSWORD -->  ")
# Erase which one is not using" 
#2 "and"
 if  u == username and p == password :
	print("username and password corect")
else:
	print("acess denied")
#3 "or"
 if  u == username or p == password :
	print("username and password corect")
else:
	print("acess denied")
