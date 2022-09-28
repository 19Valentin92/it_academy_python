sentence=input()
new_sentence=("")
for symbol in sentence:
    if new_sentence.count(symbol) <1 and  symbol!=(" ") :
        new_sentence+=symbol
print(new_sentence)