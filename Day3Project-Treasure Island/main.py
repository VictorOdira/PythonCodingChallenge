print("Welcome to the Treasure Island")
print("Your Mission to find the Treasure.")

chosen_direction = input("Enter your choice. 'Left' or 'Right': ").lower()

if chosen_direction == "left":
    print("Bingo. Your choice is perfect.")
    crossing_mode = input("Will you 'Swim' or 'Wait for the Boat? Enter either 'Swim' or 'Wait': ").lower()
    if crossing_mode == "wait":
        print("Bingo. Your choice is accurate")
        door = input("Enter the color of the door you have settled on: ").lower()
        if door == "yellow":
            print("You Win. The Treasure is Here")
        elif door == "blue":
            print("Game Over. Here there is a Monster")
        else:
            print("Game Over. Here we kill Humankind.")
    else:
        print("Game Over. Crocodiles Everywhere.")
else:
    print("Game Over")

