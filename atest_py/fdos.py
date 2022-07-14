import json
import os
import collections


USERS_DATA_FILE_PATH = "books.json"


def load_json(USERS_DATA_FILE_PATH):

    with open(USERS_DATA_FILE_PATH) as fd:
        books = json.load(fd)
    return books


def popular_genre(books):
	c=collections.Counter()
	for book in books:
		c[book['genre']] += 1
	max_count = None
	for key, value in c.items():
		if max_count is None or value > max_count:
			max_count = value
			popular_genre = key
	return popular_genre

def find_revenue(books, genre):
	revenue=0
	for book in books:
		if genre==book['genre']:
			revenue+=int(book['total_revenue'])
	return revenue

	
def main():
	books = load_json(USERS_DATA_FILE_PATH)
	genre = popular_genre(books)
	print('Самый популярный жанр книг - {}'.format(genre))
	total_revenue = find_revenue(books, genre)
	print('Было получено {} денежных единиц от продажи книг в жанре {}'.format(total_revenue, genre))

if __name__ == "__main__":
    main()