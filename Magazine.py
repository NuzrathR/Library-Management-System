import database

class Magazine:

    def __init__(self,magazine_no,title,print_type,subject,rental_price,no_of_copies,current_stock):
        self.magazine_no = magazine_no
        self.title = title
        self.print_type = print_type
        self.subject = subject
        self.rental_price = rental_price
        self.no_of_copies = no_of_copies
        self.current_stock = current_stock

    def insert_magazine(magazine):
        con = database.db_connect()
        with con:
            try:
                con.execute("INSERT INTO magazine(magazine_no,title,print_type,sub_id,rental_price,no_of_copies,current_stock) VALUES"
                            "(?,?,?,?,?,?,?);",(magazine.magazine_no,magazine.title,magazine.print_type,magazine.subject,
                                              magazine.rental_price,magazine.no_of_copies,magazine.current_stock)
                )
                return True
            except:
                return False


        con.close()


    def delete_magazine_by_no(magazine_no):
        con = database.db_connect()
        with con:
            try:
                con.execute("DELETE FROM magazine WHERE magazine_no=?;", (magazine_no,))
                return True
            except:
                return False
        con.close()


    def lend_magazine(magazine_no):
        con = database.db_connect()
        with con:
            try:
                con.execute("UPDATE book SET current_stock = current_stock-1 WHERE magazine_no=?;", (magazine_no,))
                return True
            except:
                return False

    def received_book(magazine_no):
        con = database.db_connect()
        with con:
            try:
                con.execute("UPDATE book SET current_stock = current_stock+1 WHERE magazine_no=?;", (magazine_no,))
                return True
            except:
                return False


    def getAllMagazines(self):
        con = database.db_connect()
        return con.execute("SELECT * FROM magazine").fetchall()
        con.close