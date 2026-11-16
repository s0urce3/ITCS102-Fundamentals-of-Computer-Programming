anime = []

isContinue = True

while isContinue  == True:
    ans = input("do you know any anime?? (Yes/No) ").lower()

    if ans == "Yes":
        title = input(" What is the title of the anime --->")
        anime.append(title)
        ans = input("Do you Wish to continue (yes/no)").lower()
        if ans == "yes":
            print("continue")
            continue
    else:
        print(anime)
        break