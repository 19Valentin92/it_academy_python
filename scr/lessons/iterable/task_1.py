my_list_1=input()
my_list_2=('()[]{}')
d=[]
for i in my_list_1:
    if i in my_list_2:
        d+=i
    else:
        ...
counter_1=0
if d.count("(")==d.count(")") and d.count("[")==d.count("]") and d.count("{")==d.count("}"):

    for i in d:
        if i==("("):
            counter_1+=1
        elif i==(")"):
            counter_1-=1
            if counter_1<0:
                break
    for i in d:
        if i==("["):
            counter_1+=1
        elif i==("]"):
            counter_1-=1
            if counter_1 < 0:
                break
    for i in d:
        if i==("{"):
            counter_1+=1
        elif i==("}"):
            counter_1-=1
            if counter_1 < 0:
                break
    if counter_1==0:

        for index, value in enumerate(d):
            y=d[index+1:]
            if (index + 1) != len(d):
                x=y[0]
            if value=="(" and x!="]" and x!="}":
                counter_1+=1
            if value=="[" and x!=")" and x!="}":
                counter_1+=1
            if value=="{" and x!="]" and x!=")":
                counter_1+=1
        if counter_1==(len(d)/2):
            print("Верно")

        else:
            print('Неверно')
    else:
        print('Неверно')
else:
    print('Неверно')
