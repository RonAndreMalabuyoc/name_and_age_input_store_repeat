while True:
    while True:
        try:
            Age = int(input ("Please put your name here: "))
            Retry = input("Will you give us your information again? Put yes if yes, put no if no: ")
            if Retry == "no":
                break
        except:
            print(" hehehe")

    if Retry == "no":
        break
    elif Retry != "no":
        print("Good job Buddy!")
