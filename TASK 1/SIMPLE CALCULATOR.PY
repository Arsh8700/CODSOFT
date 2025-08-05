try: 
    a = int(input("Enter the first number: "))

    b = int(input("Enter the second number: "))

    print("what kind of operation do you want to perform. Press + for addition\nPress - for subtraction\nPress / for division\npress * for multiplication")

    o = input("Enter Operation: ")
    if o == "+":
        print(f"The result is: {a + b}")
    elif o == "-":
        print(f"The result is: {a - b}")
    elif o == "*":
        print(f"The result is: {a * b}")
    elif o == "/":
        print(f"The result is: {a / b}")
    else:
        print("There was an error")

except Exception as e:
    print("Enter a valid value of a and b")