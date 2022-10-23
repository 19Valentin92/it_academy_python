last_name, parametr = input("введите фамилию автора и (название книги или дату выпуска или First или Last) :").split(' ',1)
import csv
books=[]
x=0
with open('library.csv') as f:
    fieldnames = ['names', 'novels', 'years', 'topics']
    csvfile = csv.DictReader(f, delimiter=' ', quotechar='|', fieldnames=fieldnames)

    for row in csvfile:
        if last_name in row.setdefault('names') and parametr in row.setdefault('years'):
            x+=1
            print(row.setdefault('names'), row.setdefault('novels'), row.setdefault('years'), row.setdefault('topics'))
        if last_name in row.setdefault('names') and parametr in row.setdefault('novels'):
            x+=1
            print(row.setdefault('names'), row.setdefault('novels'), row.setdefault('years'), row.setdefault('topics'))

        if (row['names'].split(', ')[0])==last_name:
            books.append(row)

if parametr =="First":
    x += 1
    book = None
    for i in books:
        if book is None:
            book=i
        else:
            if i['years'] < book ['years']:
                book=i
    print(book.setdefault('names'), book.setdefault('novels'), book.setdefault('years'), book.setdefault('topics'))

if parametr == "Last":
    x += 1
    book = None
    for i in books:
        if book is None:
            book = i
        else:
            if i['years'] > book['years']:
                book = i
    print(book.setdefault('names'), book.setdefault('novels'), book.setdefault('years'), book.setdefault('topics'))
if x==0:
    print("Ничего не найдено")