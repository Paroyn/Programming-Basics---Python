book_count = 0
the_book = input()

while True:
    book_name = input()
    book_count += 1
    if book_name == the_book:
        book_count = book_count -  1
        print(f'You checked {book_count} books and found it.')
        break
    elif book_name == 'No More Books':
        book_count = book_count - 1
        print('The book you search is not here!')
        print(f'You checked {book_count} books.')
        break
