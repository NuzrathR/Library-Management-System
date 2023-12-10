import database

class Dvd:
    def __init__(self,dvd_no,title,subject,rental_price,no_of_copies,current_stock):
        self.dvd_no = dvd_no
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.no_of_copies = no_of_copies
        self.current_stock = current_stock



    def insert_dvd(dvd):
        con = database.db_connect()
        with con:
            try:
                con.execute("INSERT INTO dvd(dvd_no,title,sub_id,rental_price,no_of_copies,current_stock) VALUES"
                            "(?,?,?,?,?,?);",(dvd.dvd_no,dvd.title,dvd.subject,dvd.rental_price,
                                              dvd.no_of_copies,dvd.current_stock)
                )
                return True
            except:
                return False

        con.close()



    def delete_dvd_by_no(dvd_no):
        con = database.db_connect()
        with con:
            try:
                con.execute("DELETE FROM dvd WHERE dvd_no=?;", (dvd_no,))
                return True
            except:
                return False
        con.close()

    def lend_dvd(dvd_no):
        con = database.db_connect()
        with con:
            try:
                con.execute("UPDATE book SET current_stock = current_stock-1 WHERE dvd_no=?;", (dvd_no,))
                return True
            except:
                return False

    def received_dvd(dvd_no):
        con = database.db_connect()
        with con:
            try:
                con.execute("UPDATE book SET current_stock = current_stock+1 WHERE dvd_no=?;", (dvd_no,))
                return True
            except:
                return False

    def getAllDvds(self):
        con = database.db_connect()
        return con.execute("SELECT * FROM dvd").fetchall()
        con.close
