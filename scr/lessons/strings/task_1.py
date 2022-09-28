sentence=input()
alphabet="abcdefghijklmnopqrstuvwxyz"
ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_letter=0
big_letter=0
for letter in sentence:
    if letter in alphabet:
        small_letter+=1
    elif letter in ALPHABET:
        big_letter+=1
number_of_small_letters=small_letter
number_of_big_letters=big_letter
print ("- Количество маленьких букв:",  number_of_small_letters)
print ("- Количество больших букв:", number_of_big_letters)