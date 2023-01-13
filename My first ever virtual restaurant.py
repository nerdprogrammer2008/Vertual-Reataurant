print("Hello")
name = input("What is your name? ")
if name == "Sara" or name == "Salma":
    answer = input("Do you like physics? ")
    answer3 = int(input("How many physics problems did you solve yesterday? "))
    if answer == "No" and answer3 < 10:
        print("Get out!! idiot")
        exit()
    else:
        print("Welcome,come in")
        menu = "Mashed potatos\n" + "Beef burger"
        print("Here is the menu\n" + menu)
        order = input("What would you like to order? ")
        if order == "Beef burger":
            answer2 = input("Would you like some extra chease in it? ")
            if answer2 == "Yes":
                price = 9
            else:
                price = 8
        elif order == "Mashed potatos":
            price = 5
        else:
            print("Sorry!we dont have that")
            exit()
        Num = input("How many meals do you want? ")
        Total = int(Num)*price
        print(name + " your " + Num + " " + order + " will be ready in a few moments and your total is $" + str(Total))
else:
    print("Welcome,come in")
    menu = "Mashed potatos\n" + "Beef burger"
    print("Here is the menu\n" + menu)
    order = input("What would you like to order? ")
    if order == "Beef burger":
        answer2 = input("Would you like some extra chease in it? ")
        if answer2 == "Yes":
            price = 9
        else:
            price = 8
    elif order == "Mashed potatos":
        price = 5
    else:
        print("Sorry!we dont have this")
        exit()
    Num = input("How many meals do you want? ")
    Total = int(Num)*price
    print(name + " your " + Num + " " + order + " will be ready in a few moments and your total is $" + str(Total))
    
    
    
    
    
    
    
    

   









