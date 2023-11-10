check = True

while check:
    age = int(input("Enter your age : "))
    if age < 1:
        print("Chota baccha he ky")
    elif age < 10:
        print("primary Age")
    elif age < 20:
        print("Secondary Age")
    elif age < 50:
        print("Working Age")
    else:
        print("Retirement Age")

