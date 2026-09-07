#BANK CHALLENGE

Balance = 19863
#Thousand = 19
#Five Hundred = 1
#Two Hundred = 1
#One Hundred = 1
#Fifty = 1
#Twenty = 0
#Ten = 1
#Five= 0
#one = 3

print ("Money to deposit --->",Balance)

p1000 = Balance // 1000
Balance %= 1000

p500 = Balance // 500
Balance %= 500

p200 = Balance // 200
Balance %= 200

p100 = Balance // 100
Balance %= 100

p50 = Balance // 50
Balance %= 50

p20 = Balance // 20
Balance %= 20

p10 = Balance // 10
Balance %= 10

p5 = Balance // 5
Balance %= 5

p1 = Balance // 1

print("My deposit ---> -", p1000)
print("My deposit --->  -", p500)
print("My deposit --->  -", p200)
print("My deposit --->  -", p100)
print("My deposit --->   -", p50)
print("My deposit --->   -", p20)
print("My deposit --->   -", p10)
print("My deposit --->    -", p5)
print("My deposit --->    -", p1)



#revised Bank deposit Activity

money = eval(input("Money to deposit --->"))

dot = money // 1000
dofh = money % 1000 // 500
doth = money % 1000 % 500 // 209
donh = money % 1000 % 500 % 200 // 100
doft = money % 1000 % 500 % 200 % 100 // 50
dotw = money % 1000 % 500 % 200 % 100 % 50 // 20
dotn = money % 1000 % 500 % 200 % 100 % 50 % 20 // 10
dofv = money % 1000 % 500 % 200 % 100 % 50 % 20 % 10 // 5
done = money % 1000 % 500 % 200 % 100 % 50 % 20 % 10 % 5 // 1

print("1000 -", dot)
print("500 -", dofh)
print("200 -", doth)
print("100 -", donh)
print("50 -", doft)
print("20 -", dotw)
print("10 -", dotn)
print("5 -", dofv)
print("1 -", done)
