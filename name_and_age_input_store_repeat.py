while True:
    while True:
        try:
            Name = input("Please put your name here: ")
            Age = int(input ("Please put your age here: "))
            Retry = input("Will you give us your information again? Put yes if yes, put no if no: ")
            if Retry == "no":
                print("name:", Name)
                print("Age:", Age)
                break
        except:
            print("Invalid input, please try again")
            

    if Retry == "no":
        break
    elif Retry != "no":
        print("Good job Buddy!")
