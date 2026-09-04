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

print("Your Current Balance Money is --->",Balance)
print ("Money to Withdraw--->",Balance)

Thousand = Balance // 1000
Balance = Balance % 19
print("Withdraw Balance is --->",Thousand)

Five Hundred = Balance // 500
Balance = Balance % 1
print("Withdraw Balance--->",Five Hundred)
