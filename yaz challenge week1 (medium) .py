from collections import Counter

def find_most_common_letter(text):
    text = text.lower()  # Convert the text to lowercase to remove case sensitivity
    letters = [letter for letter in text if letter.isalpha()]  # Create a list containing only letters
    letter_counts = Counter(letters)  # Count the occurrences of each letter

    most_common = letter_counts.most_common(1)[0]  # Get the most common letter and its count

    return most_common

# Get input from the user
text = input("Enter a text: ")

# Find the most common letter
most_common_letter, count = find_most_common_letter(text)

# Print the result
print("Most common letter:", most_common_letter)
print("Count:", count)
