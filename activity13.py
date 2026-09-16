#nesting 
print("Welcome to the Bank!")
age = int(input("Enter you age ---->"))
IsEmployed = bool(input("Are you currently Employed?--->"))
credit_score = eval(input("Credit score history--->"))
AnnualIncome = eval(input("How much is your annual income---->?"))
HasCollateral = bool(input("Do you have any collateral--->?"))

base_interest = 0.0
#1.
if age >= 21 and IsEmployed == True:
    print("you may now proceed to the next step")


    if credit_score >= 750:
        if AnnualIncome >= 1000:
           base_rate = 4.5
           print("hi,your interest rate is",base_interest)
        else:
          base_rate = 5.0
          print("hi,your interest rate is",base_interest) 
    elif credit_score >= 600 and credit_score >750:
        if HasCollateral == True:
            base_rate = 7,0
            print("hi,your interest rate is",base_interest)
        elif AnnualIncome > 40000:
             base_rate = 9.5
             print("hi,your interest rate is",base_interest)
        else:
             base_rate=8.0
             print("hi,your interest rate is",base_interest)
    if credit_score < 600:
        print("rejected credit score too low!")


else:
    print("Baseline crietria Failed!")