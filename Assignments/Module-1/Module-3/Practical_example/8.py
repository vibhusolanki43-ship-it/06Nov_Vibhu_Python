try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))

    c=a/b
    print("The result is:",c)   

except:
    print("Division by zero is not allowed.")

else:
    print("Error! Please enter valid numbers.")

finally:
    print("Thank you for using the program.")