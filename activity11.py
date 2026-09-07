#import demo

import getpass

username = "Venn"
password = "Marc"

u = input("Input USERNAME -->  ")
p = getpass.getpass("Input PASSWORD -->  ")

if  u == username and p == password :
	print("username and password corect")
else:
	print("acess denied")
