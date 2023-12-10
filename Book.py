import database
from datetime import datetime

class Book:
    def __init__(self,isbn,title,format,subject,rental_price,no_of_copies,current_stock):
        self.isbn = isbn
        self.title = title
        self.format = format
        self.subject = subject
        self.rental_price = rental_price
        self.no_of_copies = no_of_copies
        self.current_stock = current_stock


    def insert_book(book):
        con = database.db_connect()
        with con:
            try:
                con.execute("INSERT INTO book(isbn,title,format,sub_id,rental_price,no_of_copies,current_stock) VALUES"
                            "(?,?,?,?,?,?,?);",(book.isbn,book.title,book.format,book.subject,
                                              book.rental_price,book.no_of_copies,book.current_stock)
                )
                return True
            except:
                return False

        con.close()


    def delete_book_by_isbn(isbn):
        con = database.db_connect()
        with con:
            try:
                con.execute("DELETE FROM book WHERE isbn=?;", (isbn,))
                return True
            except:
                return False
        con.close()


    def lend_book(isbn):
        con = database.db_connect()
        with con:
            try:
                con.execute("UPDATE book SET current_stock = current_stock-1 WHERE isbn=?;",(isbn,))
                return True
            except:
                return False


    def received_book(isbn):
        con = database.db_connect()
        with con:
            try:
                con.execute("UPDATE book SET current_stock = current_stock+1 WHERE isbn=?;",(isbn,))
                return True
            except:
                return False



    def getAllBooks(self):
        con = database.db_connect()
        return con.execute("SELECT * FROM book").fetchall()
        con.close
