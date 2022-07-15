N = int(input())
books = {}
for i in range(N):
    a = input()
    if books.get(a, 0):
        books[a] += 1
    else:
        books[a] = 1

books_sorted = sorted(books.items(), key=lambda x: x[1], reverse=True)

li = []
for i in books_sorted:
    if i[1] == books_sorted[0][1]:
        li.append(i[0])

li.sort()
print(li[0])