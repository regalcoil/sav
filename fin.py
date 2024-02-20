def sav():
        t = 0
        a = 0
        print("")
        x = float(input("How many dollars will your initial investment be? "))
        print("")
        i = float(input("What is the expected interest rate? "))
        print("")
        n = float(input("How frequently will the investment compound per year? "))
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("The investment will multiply over the following years ")
        while a < 2*x:
                t = t + 1
                a = x*((1+(i/n))**(t*n))
        print("")
        print("double:     " + str(t))
        while a < 3*x:
                t = t + 1
                a = x*((1+(i/n))**(t*n))
        print("")
        print("triple:     " + str(t))
        while a < 4*x:
                t = t + 1
                a = x*((1+(i/n))**(t*n))
        print("")
        print("quadruple:  " + str(t))
        while a < 5*x:
                t = t + 1
                a = x*((1+(i/n))**(t*n))
        print("")
        print("quintet:    " + str(t))
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        choice = input("Enter 'y' to restart and anything else to exit this program: ")
        choice = choice.lower()
        if choice == "y":
                sav()
        else:
                exit()
        

sav()

