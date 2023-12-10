import database


class Cd:
    def __init__(self, cd_no, title, subject, rental_price, no_of_copies,current_stock):
        self.cd_no = cd_no
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.no_of_copies = no_of_copies
        self.current_stock = current_stock



    def insert_cd(cd):
        con = database.db_connect()

        with con:
            try:
                con.execute("INSERT INTO cd(cd_no,title,sub_id,rental_price,no_of_copies,current_stock) VALUES"
                            "(?,?,?,?,?,?);", (cd.cd_no, cd.title, cd.subject, cd.rental_price,
                                               cd.no_of_copies,cd.current_stock)
                            )
                return True
            except:
                return False

        con.close()



    def delete_cd_by_no(cd_no):
        con = database.db_connect()
        with con:
            try:
                con.execute("DELETE FROM cd WHERE cd_no=?;", (cd_no,))
                return True
            except:
                return False
        con.close()

    def lend_cd(cd_no):
        con = database.db_connect()
        with con:
            try:
                con.execute("UPDATE book SET current_stock = current_stock-1 WHERE cd_no=?;", (cd_no,))
                return True
            except:
                return False
    def received_cd(cd_no):
        con = database.db_connect()
        with con:
            try:
                con.execute("UPDATE book SET current_stock = current_stock+1 WHERE cd_no=?;", (cd_no,))
                return True
            except:
                return False

    def getAllCds(self):
        con = database.db_connect()
        return con.execute("SELECT * FROM cd").fetchall()
        con.close
