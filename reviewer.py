#inputs
age = int(input("Enter your Age-->"))
rev = int(input("Enter Monthly Revenue-->"))
cc = int(input("Enter Credit score-->"))
yrs_b =  int(input("Years Bussines"))
has_defaults = bool(input("Default History"))
collateral = input("Collateral Name")
c_value = float(input("collateral Vaule"))

max_limit = 0.0
base_fee = 0.0

#baseline
if age >= 21 and yrs_b >=2 and has_defaults == False:
    print("baseline passed")
    #tier 1 condition
    if cc >=720:
        max_limit = rev * 3
        print("maxloan for high credit is",max_limit)
        print("High Credit Score of 720")
        if rev >= 720:
            base_fee = max_limit * 0.015
            print("Base Fee rate is",base_fee)
        else:
            base_fee = max_limit *0.025
            print("base fee rate is",base_fee)
        if c_value >= max_limit:#collateral
            print("Collateral", collateral, "--Accepted")
        else:
            print("Collateral not Accepted!!")
        #sercharge
        surcharge = max_limit * base_fee
        if c_value % 500 !=0:
            surcharge +=250
    
    #tier 2

    elif cc <= 620 and cc < 720:
        max_limit = rev * 1.5
        print("max laon is set",max_limit)
        if yrs_b >= 5:
            base_fee = max_limit * 0.02
            print("Base fee rate is",base_fee)
        else:
            base_fee = max_limit *0.035
            print("Base fee rate is",base_fee)
        if c_value >= max_limit:
            print("Collateral", collateral, "-->Accepted")
        else:
            print("Collateralnot accepted!")
        #sercharge
        surcharge = max_limit * base_fee
        if c_value % 500 !=0:
            surcharge +=250
    #tier 3
    elif cc < 620:
        print("Credit Score too low to low")
    else:
        print("not Tier 1")
else:
    print("Baseline Failed!!")