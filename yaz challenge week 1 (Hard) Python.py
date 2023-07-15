def find_combinations(number, target):
    result = []
    current_combination = []
    def backtrack(remaining, start):
        if remaining == 0:
            result.append(list(current_combination))
        elif remaining < 0:
            return
        else:
            for i in range(start, len (numbers)):
                current_combination.append(numbers[i])
                backtrack(remaining - numbers[i], i)
                current_combination.pop()
    backtrack(target, 0)
    return result
numbers = input("enter integer with using comma:").split(",")
numbers = [int(num.strip()) for num in numbers]
target = int(input("enter your target numnber: "))
combinations = find_combinations(numbers, target)
print(f"Different combinations for target number ({target})")
for combination in combinations:
    print(combination)