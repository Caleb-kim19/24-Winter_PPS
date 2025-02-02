from collections import Counter

N = int(input())
books = [input().strip() for _ in range(N)]

book_count = Counter(books)
max_count = max(book_count.values())

max_books = [book for book, count in book_count.items() if count == max_count]
print(min(max_books))