'''

Problem:


Annie goes to her hometown after a very long period outside the country.
When she gets home, she sees the grandmother's old library and she remembers her favorite book.
Help Annie to write a program, in which she enters the book she is looking for (text) and the capacity of the library
(integer). While Annie doesn't find the favorite book or don't check everyone in the library,
the program should read every time on new line the name of each subsequent book (text).

 If she does not find the book, print it in two lines:
o The book you search is not here!
o You checked {number} books.

 If she finds her book, print it in one order:
o You checked {number} books and found it.

Example Input:

Troy
8
Stronger
Life Style
Troy

Output:

You checked 2 books and found it.


Solution:



'''


books = input()
count = int(input())

counter = 0
book_found = False

while counter < count and not book_found:
    current_book = input()
    if current_book == books:
        print('You checked {} books and found it.'.format(counter))
        book_found = True

    counter += 1

if not book_found:
    print('The book you search is not here!')
    print('You checked {} books.'.format(count))
