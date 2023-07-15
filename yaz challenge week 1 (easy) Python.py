from datetime import date 
def age_calculation(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.year:
        age -= 1
    elif today.month < birth_date.month:
        age -= 1
    return age
day = int(input("Please enter your birth day:"))
month = int(input("Please enter your birh month:"))
year = int(input("ĞPlease enter your birth year:"))
birth_date = date(year, month, day)
age = age_calculation(birth_date)
print("Your age is:", age)