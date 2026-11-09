# Boolean variable

tuloy = True

while tuloy == True:

    ask = input("Do you want to continue? (yes/no) ")

    if ask.lower() == "yes":
        print("continuing")
        continue
    else:
        print("stopping")
        break