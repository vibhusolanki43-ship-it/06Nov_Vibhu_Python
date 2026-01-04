try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is {result}")

except:
    print("Error: Cannot divide by zero.")