list= input('Введите список тем и количество книг, через запятую:' ).split(',')
num,list_theme=int(list[-1]),set(list[:-1])
import csv
books=[]
with open('library.csv') as f:
    csvfile = csv.DictReader(f, delimiter=' ', quotechar='|', fieldnames=['names', 'novels', 'years', 'topics'])
    for row in csvfile:
        match=len(set((row.get('topics')).split(',')) & list_theme)
        row['match']=match
        if match>0:
            books.append(row)
z=(sorted(books, key=lambda row:row['match'], reverse=True ))
result=z[0:num]
for d in result:
    print(d.setdefault('names'), d.setdefault('novels'), d.setdefault('years'), d.setdefault('topics'))