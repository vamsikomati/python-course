string = input("Enter a string: ")
words = string.split()
max_length = 0
for word in words:
    if len(word) > max_length:
        max_length = len(word)
print("Length of the longest word:", max_length)
