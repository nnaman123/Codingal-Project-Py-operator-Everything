#Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 10 subcategories. To give the user better selection options
#take input from the user for the type of ride
ride_type = input("Enter the type of ride (Bike/Car): ")
#check if the ride type is Bike
if ride_type.lower() == 'bike':
    #take input from the user for the bike subcategory
    bike_subcategory = input("Enter the bike subcategory (Standard/Sports): ")
    #check if the bike subcategory is Standard
    if bike_subcategory.lower() == 'standard':
        print("You have selected a Standard Bike.")
    #check if the bike subcategory is Sports
    elif bike_subcategory.lower() == 'sports':
        print("You have selected a Sports Bike.")
    else:
        print("Invalid bike subcategory selected.")
#check if the ride type is Car
elif ride_type.lower() == 'car':
    #take input from the user for the car subcategory
    car_subcategory = input("Enter the car subcategory (Sedan/SUV): ")
    #check if the car subcategory is Sedan
    if car_subcategory.lower() == 'sedan':
        print("You have selected a Sedan Car.")
    #check if the car subcategory is SUV
    elif car_subcategory.lower() == 'suv':
        print("You have selected an SUV Car.")
    else:
        print("Invalid car subcategory selected.")
        print("Invalid ride type selected.")
        print("Please select a valid ride type (Bike/Car).")
