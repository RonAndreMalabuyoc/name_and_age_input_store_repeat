user_info = {}

while True:
    while True:
        try:
            Name = input("Please put your name here: ")
            Age = int(input ("Please put your age here: "))
            user_info['name'] = Name
            user_info['age'] = Age

            user_info[Name] = Age

            Retry = input("Will you give us your information again? (yes/no): ")
            if Retry == "no":
                break
        except:
            print("Invalid input, please try again")
            

    if Retry == "no":
        break
    elif Retry != "no":
        print("Good job Buddy!")

oldest_person = None
highest_age = -1

for name, age in user_info.items():
    if age > highest_age:
        highest_age = age
        oldest_person = name

if oldest_person:
    print(f"\nThe Oldest person here is {oldest_person}: {highest_age}")