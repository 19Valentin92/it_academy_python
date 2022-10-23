teams_inp=input("Введите названия команд через пробел без запятых: ")
teams=teams_inp.split()
scores_inp=input("Введите результаты матчей через пробел без запятых: ")
a=scores_inp.split(" ")
x=[]
win_list_1=[]
win_list_2=[]
win_list_3=[]

for i in a:
    s=i.split(":")
    x.append(int(s[0]))
    x.append(int(s[1]))
while len(win_list_1)!=8:
    y=x[0]+x[2]
    z=x[1]+x[3]
    del x[0:4]
    if y>z :
        win_list_1.append(teams[0])
        del teams[0::(len(teams))-1]

    else:
        win_list_1.append(teams[(len(teams))-1])
        del teams[0::(len(teams))-1]

while len(win_list_2) != 4:
    y = x[0] + x[2]
    z = x[1] + x[3]
    del x[0:4]
    if y > z:
        win_list_2.append(win_list_1[0])
        del win_list_1[0::(len(win_list_1)) - 1]

    else:
        win_list_2.append(win_list_1[(len(win_list_1))-1])
        del win_list_1[0::(len(win_list_1)) - 1]

while len(win_list_3) != 2:
    y = x[0] + x[2]
    z = x[1] + x[3]
    del x[0:4]
    if y > z:
        win_list_3.append(win_list_2[0])
        del win_list_2[0::(len(win_list_2)) - 1]

    else:
        win_list_3.append(win_list_2[(len(win_list_2))-1])
        del win_list_2[0::(len(win_list_2)) - 1]

if x[0]>x[1]:
    print(f"Выиграла команда: {win_list_3[0]}")
else:
    print(f"Выиграла команда: {win_list_3[1]}")