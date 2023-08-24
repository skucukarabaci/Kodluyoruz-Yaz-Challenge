def find_animal_count(total_animals, total_legs):
    for num_of_chickens in range(total_animals + 1):
        num_of_sheeps = total_animals - num_of_chickens
        if(2 * num_of_chickens + 4 * num_of_sheeps) == total_legs:
            return num_of_chickens, num_of_sheeps
    return None, None
    
total_animals = 36
total_legs = 100
num_of_chickens, num_of_sheeps = find_animal_count(total_animals, total_legs)
if(num_of_chickens is not None, num_of_sheeps is not None):
    print("Num of Chicken is: ", num_of_chickens)
    print("Num of Sheep is: ", num_of_sheeps)
else:
    print("Error...")