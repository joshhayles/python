
# used to easily identify keyword arguments
def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("you fool")

divide(dividend=15, divisor=0) # => you fool