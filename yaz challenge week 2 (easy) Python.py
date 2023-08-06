def prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(num**0.5) +1 ):
            if num % i == 0:
                return False
            return True
try:
    num = int(input("Please enter a number: "))
    if prime(num):
        print(num, "is a prime number! ")
    else:
        print(num, "is not a prime number! ")
except ValueError:
    print("Please enter a valid number")