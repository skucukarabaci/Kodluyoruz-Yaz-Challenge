import math
try:
    number = int(input("Please enter an integer: "))
    if(number < 0):
        print("Negative numbers have not a factorial")
    else:
        result = math.factorial(number)
        print(f"{number} 's factorial is: {result}")

except ValueError:
    print("Invalied value entered")