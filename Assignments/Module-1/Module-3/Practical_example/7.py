try:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    print("Select the operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    opreation = input("Enter operation (1/2/3/4): ")

    if opreation == '1':
        print(f"The addition of {n1} and {n2} is {n1 + n2}")

    elif opreation == '2':
        print(f"The subtraction of {n1} and {n2} is {n1 - n2}") 

    elif opreation == '3':
        print(f"The multiplication of {n1} and {n2} is {n1 * n2}")

    elif opreation == '4':
        print(f"The division of {n1} and {n2} is {n1 / n2}")

    else:
        print("Invalid operation selected!")

except:
        print("Division by zero is not allowed.")

finally:
    print("Thank you for using the calculator.")