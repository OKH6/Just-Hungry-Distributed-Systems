import Pyro4
FrontEnd = Pyro4.Proxy("PYRONAME:FrontEnd")


while True:
    print("Welcome to Just Hungry!")
    name = input("What is your name? ").strip()
    while True:
        ques="Hello "+name+" enter 0 to see past orders or enter 1 if you would like to start a new order: "
        ans = input(ques).strip()
        print("\n")
        if ans == "0":
            Corders = FrontEnd.GetPastOrders(name)
            if len(Corders)==0:
                print("You do not have any orders")
            for order in Corders:
                print(order)
            print("\n")
            break
        if ans == "1":
            Menus = FrontEnd.GetAllMenus(name)
            print("Here are all the restaurants in just Hungry! More will be added in the near future :).\n")
            for x, y in enumerate(Menus):
                print("{}: {}".format(x + 1, y[0]))
            print("\n")
            while True:
                try:
                    MenNum = int(input("Which restaurants menu do you want? ").strip())
                except:
                    print("please input an integer")
                    continue

                if MenNum <= len(Menus) and MenNum > 0:
                    break
                else:
                    print("Please choose a valid menu")
            ChosenMen = FrontEnd.GetMenu(MenNum - 1)
            print(">>>>>>>>>>>>>>>>{} Menu<<<<<<<<<<<<<<<<\n\n".format(ChosenMen[0]))
            for course, options in ChosenMen[1].items():
                print("\n {:^33}".format(course))
                print("-------------------------------------".format(course))
                for c,j in enumerate(options):
                    print('{}: {:^30} £{}'.format(c, j[0], j[1]))
            print("\n\n")
            while True:
                try:
                    starter = int(input("Please choose a starter?(number) ").strip())

                except:
                    print("please enter a number")
                    continue
                if starter <= len(ChosenMen[1]["starters"]) and starter >= 0:
                    break
                else:
                    print("please choose a valid starter number")

            while True:
                try:
                    main = int(input("Please choose a main? (number)").strip())

                except:
                    print("please enter a number")
                    continue

                if main <= len(ChosenMen[1]["mains"]) and main >= 0:
                    break
                else:
                    print("please choose a valid meal number")

            while True:
                try:
                    desert = int(input("Please choose a desert? (number)").strip())
                except:
                    print("please enter a number")
                    continue
                if desert <= len(ChosenMen[1]["desert"])  and desert >= 0:
                    break
                else:
                    print("please choose a valid desert number")

            FrontEnd.AddFoodChoice([starter, main, desert])

            while True:
                postcode = input("What is your Postcode? ").strip()
                checkPostCode=FrontEnd.CheckAddress(postcode)
                if len(checkPostCode)<7:

                    print("please enter a valid post code")
                else:

                    print("order will be posted to "+checkPostCode[5]+", "+checkPostCode[6]+" Post Code: "+postcode+", Total Cost: "+str(checkPostCode[3]))
                    break


            while True:
                cont = input("Do you wish to confirm(Confirm) the order or cancel it(Cancel)?").strip()
                if cont=="Confirm":
                    response=FrontEnd.ConfirmOrder(True)
                    print(response)
                    print("\n")
                    break

                elif cont=="Cancel":
                    response=FrontEnd.ConfirmOrder(False)
                    print(response)
                    print("\n")
                    break
            break
        else:
            print("Please choose a valid option")
