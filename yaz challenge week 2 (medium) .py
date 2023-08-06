def upper(x):
    return x.upper()
try:
    x = input("please enter a word: ")
    converted_word = upper(x)
    print("Converted version: ", converted_word)
except Exception as e:
    print("Upps Something goes wrong!", e)
