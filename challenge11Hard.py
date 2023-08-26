import numpy as np
array = np.random.randint(0, 100, size = 10)
array.sort()
print(array)
target_number = int(input("Please enter your target number: "))
repeat_count = np.count_nonzero(array == target_number)
print(f"The number {target_number} repeats {repeat_count} times.")