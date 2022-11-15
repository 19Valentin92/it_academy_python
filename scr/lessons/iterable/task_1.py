brackets_string = input()
brackets = []
bool_value = True
for i in brackets_string:
    if i in '({[':
        brackets.append(i)
    elif i in ')}]':
        if not brackets:
            bool_value = False
            break
        cloud_storage = brackets.pop()
        if cloud_storage == '(' and i == ')':
            continue
        if cloud_storage == '[' and i == ']':
            continue
        if cloud_storage == '{' and i == '}':
            continue
        bool_value = False
        break
if bool_value and len(brackets) == 0:
    print("Верно")
else:
    print('Неверно')