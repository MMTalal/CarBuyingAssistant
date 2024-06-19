# Prompt the user to enter the type of car they need (new or used)
car_type = input("What type of car do you need? New or Used? ").capitalize().strip()

# Check if the user requested a new car
if car_type == "New":
    print(f"We have {car_type} cars available.")
    
    # Prompt the user to select a color for the new car
    color = input("What color would you like? ").capitalize().strip()
    colors = ['White', 'Yellow', 'Red', 'Pink', 'Blue', 'Gray', 'Black', 'Orange', 'Green', 'Violet', 'Purple', 'Brown', 'Indigo', 'Silver', 'Golden']
    
    # Handle the user's color selection for a new car
    if color in colors:
        print(f"We have a {color} {car_type} car available.")
    else:
        print("Sorry, we don't have that color in stock.")
        color = input("What color would you like? ").capitalize().strip()
        print(f"Okay, we'll prepare a {color} car for you in five days.")
    
    # Prompt the user to enter the maximum mileage they're looking for
    distance = int(input("What is the maximum mileage you're looking for? "))
    
    # Handle the user's mileage requirement for a new car
    if distance > 200:
        print(f"Sorry, we don't have any cars with less than {distance} km.")
    else:
        print("Okay, great.")
        
        # Prompt the user to enter their maximum budget
        price = int(input("What is your maximum budget? "))
        
        # Handle the user's budget for a new car
        if price < 15000:
            print("Sorry, the car isn't ready for sale.")
        else:
            print("The car is ready for sale.")
            print(f"Review your order:\nYou're buying a {car_type} car in {color}, with a maximum mileage of {distance} km, for ${price}.")

# Check if the user requested a used car
elif car_type == "Used":
    print(f"We have {car_type} cars available.")
    
    # Prompt the user to select a color for the used car
    color = input("What color would you like? ").capitalize().strip()
    colors = ['White', 'Yellow', 'Red', 'Pink', 'Blue', 'Gray', 'Black', 'Orange', 'Green', 'Violet', 'Purple', 'Brown', 'Indigo', 'Silver', 'Golden']

    # Handle the user's color selection for a used car
    if color in colors:
        print(f"We have a {color} {car_type} car available.")
    else:
        print("Sorry, we don't have that color in stock.")
        color = input("What color would you like? ").capitalize().strip()
        print(f"Okay, we'll prepare a {color} car for you in five days.")
    
    # Prompt the user to enter the maximum mileage for the used car
    distance = int(input("What is the maximum mileage for the used car? "))
    
    # Handle the user's mileage requirement for a used car
    if distance > 200:
        print(f"Sorry, we don't have any used cars with less than {distance} km.")
    else:
        print("Okay, great.")
        
        # Prompt the user to enter their maximum budget
        price = int(input("What is your maximum budget? "))
        
        # Handle the user's budget for a used car
        if price < 15000:
            print("Sorry, the car isn't ready for sale.")
        else:
            print("The car is ready for sale.")
            print(f"Review your order:\nYou're buying a {car_type} car in {color}, with a maximum mileage of {distance} km, for ${price}.")

# Handle the case where the user enters an invalid car type
else:
    print("Error: Please choose either 'New' or 'Used'.")
