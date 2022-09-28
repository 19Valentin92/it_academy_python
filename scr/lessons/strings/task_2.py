sentence = input()  # "This is a sentence"

max_len = 0
max_word = ""

words = sentence.split(" ")  # ["This", "is", "a", "sentence"]
for word in words:
    if len(word) > max_len:
        max_len = len(word)
        max_word = word

print(max_word)