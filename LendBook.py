import database

class LendBook:
    def __init__(self,lend_id,isbn,stu_id,lend_date,received_date):
        self.lend_id = lend_id
        self.isbn = isbn
        self.stu_id = stu_id
        self.lend_date = lend_date
        self.received_date = received_date



    def insert_lend_book_record(book):
        con = database.db_connect()
        with con:
            try:
                con.execute("INSERT INTO lend_book(isbn,stu_id,lend_date,received_date) VALUES"
                            "(?,?,?,?);",(book.isbn,book.stu_id,book.lend_date,book.received_date)
                )
                return True
            except:
                return False

        con.close()

    def update_lend_book_record(book):
        con = database.db_connect()
        with con:
            ''''try:
                con.execute("UPDATE lend_book SET received_date =? WHERE isbn=?;", (book.received_date,book.lend_id,))
                return True
            except:
                return False'''
            print(book.received_date)
            con.execute("UPDATE lend_book SET received_date=? WHERE lend_id=?;", (book.received_date, book.lend_id))
            return True
        con.close()

    def get_lend_book_records_by_stu_id(stu_id):
        con = database.db_connect()
        try:
            return con.execute("SELECT * FROM lend_book WHERE stu_id=? "
                               "AND received_date = 'still not';",(stu_id,)).fetchall()
        except:
            return False
        con.close

    def get_isbn_by_lend_id(lend_id):
        con = database.db_connect()
        return con.execute("SELECT isbn FROM lend_book WHERE lend_id=?;",(lend_id,)).fetchall()
        con.close

    def get_all_lend_records(self):
        con = database.db_connect()
        return con.execute("SELECT * FROM lend_book").fetchall()
        con.close