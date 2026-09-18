#Exercise 1. Arithmetic Product and Conditional Logic
#Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
while True:
    first_integer=input("Enter the first integer:\n")
    second_integer=input("Enter the second integer:\n")
    try:
        first_integer1=int(first_integer)
        second_integer1=int(second_integer)
    except:
        print("Invalid input")
        continue
    if first_integer1*second_integer1<=1000:
        print("Product:",first_integer1*second_integer1)
    elif first_integer1*second_integer1>1000:
        print("Sum:",first_integer1+second_integer1)
    while True:
        user_choice=input("Do you want to continue ? (y/n):\n")
        try:
            if user_choice.strip().lower() not in ("y","n"):
                raise ValueError
            else:
                break
        except:
            print("invalid input")
            continue
    if user_choice.strip().lower()=="y":
        continue
    elif user_choice.strip().lower()=="n":
        print("quitting...")
        quit()
    
