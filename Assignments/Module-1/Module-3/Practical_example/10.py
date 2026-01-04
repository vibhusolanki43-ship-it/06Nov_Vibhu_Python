try:
    car_price = int(input("Enter car price: "))
    buyer_age = int(input("Enter buyer age: "))
    buyer_name = input("Enter buyer name: ")
    car_brand = input("Enter car brand: ")

    # Custom exception conditions
    if car_price <= 0:
        raise Exception("Custom Exception: Car price must be greater than 0")

    if buyer_age < 18:
        raise Exception("Custom Exception: Buyer must be 18 years or older to purchase a car")

    print("Car sale approved!")
    print("Car Price:", car_price)
    print("Buyer Age:", buyer_age)
    print("Buyer Name:", buyer_name)
    print("Car Brand:", car_brand)

except Exception as e:
    print(e)

finally:
    print("Car selling process completed.")
