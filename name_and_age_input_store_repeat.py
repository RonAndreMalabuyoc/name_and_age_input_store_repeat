user_info = {}

while True:
    while True:
        try:
            Name = input("Please put your name here: ")
            Age = int(input ("Please put your age here: "))
            user_info['name'] = Name
            user_info['age'] = Age

            user_info[Name] = Age

            Retry = input("Will you give us your information again? Put yes if yes, put no if no: ")
            if Retry == "no":
                break
        except:
            print("Invalid input, please try again")
            

    if Retry == "no":
        break
    elif Retry != "no":
        print("Good job Buddy!")

print("\nUsers Information: ")
for name, age in user_info.items():
    print(f"{name}: {age}")
