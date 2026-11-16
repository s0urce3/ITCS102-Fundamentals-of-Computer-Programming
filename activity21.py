#jeepney simulator
route = ["Lucena", "Tayabas", "Sariaya"]
passengers = []
seats = 6
fare = 13
total = 0

while True:
    print()
    print("SAKAY : ", passengers)
    print(len(passengers), "of", seats, "seats")
    print("1 Sakay 2 Priority 3 Para po!")
    print("4 Baba sa pinto 5 baba sa harap")
    print("6 Seat cheack 7 Balikan 8 Exit")
    choice = input("Choice: ")

    if choice == "1":
        if len(passengers) == seats:
            print("PUNO NA!!!")
        else:
            name = input("Name: ")
            passengers.append(name)
            total = total + fare
            print(name, "boarded at the back.")

    elif choice == "2":
        if len(passengers) == seats:
            print("PUNO NA!!!")
        else:
            name = input("Name: ")
            passengers.append(name)
            total = total + fare
            print(name, "Took the priority seat.")

    elif choice == "3":
        name = input("Who is getting off?")
        if name in passengers:
            passengers.remove(name)
            print(name, "Got off. Ingat po")
        else:
            print(name, "Is not on this jeep")

    elif choice == "4":
        if len(passengers) == 0:
            print("The jeepney is empty")
        else:
            left = passengers.pop(0)
            print(left, "Got off at the door.")

    elif choice == "5":
        if len(passengers) == 0:
            print("The jeepney is empty")
        else:
            front = passengers.pop(0)
            print(front, "Got off at the door.")

    elif choice == "6":
        for i in range(len(passengers)):
            print("Seat", i + 1, passengers[i])

    elif choice == "7":
        route.reverse()
        print("Route: ", route)

    elif choice == "8":
        print("Total fare today: ", fare)
        break

    else:
        print("Invalid Choice.")
