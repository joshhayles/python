
# you can use a tuple to check if a user input is lowercase or uppercase:
number = 7
user_input = input("Enter 'y' if you would like to play..." )
# you can also turn the users input into lowercase using .lower()

if user_input in ("y", "Y"): # if the users input is in this tuple...
    user_number = int(input("Guess what number I'm thinking ..."))
    if user_number == number:
        print("Wow! That's right!")
    elif abs(number - user_number) == 1:
        print("You are soooo close")
    else:
        print("Not even close.")