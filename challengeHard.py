def pool():
    first_one_speed = 1 / 10
    second_one_speed = 1 / 15
    #third_one_speed = 1 / 30 
    total_speed = first_one_speed + second_one_speed 
    total_time = 1 / total_speed
    return total_time
total_time = pool()
print("Total full of pool time: ", total_time)