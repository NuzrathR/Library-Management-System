import database

class LendMagazine:
    def __init__(self,lend_id,magazine_no,stu_id,lend_date,received_date):
        self.lend_id = lend_id
        self.magazine_no = magazine_no
        self.stu_id = stu_id
        self.lend_date = lend_date
        self.received_date = received_date


    def insert_lend_magazine_record(magazine):
        con = database.db_connect()
        with con:
            try:
                con.execute("INSERT INTO lend_magazine(magazine_no,stu_id,lend_date,received_date) VALUES"
                            "(?,?,?,?);",(magazine.magazine_no,magazine.stu_id,magazine.lend_date,magazine.received_date)
                )
                return True
            except:
                return False

        con.close()


    def update_lend_magazine_record(magazine):
        con = database.db_connect()
        with con:
            ''''try:
                con.execute("UPDATE lend_magazine SET received_date =? WHERE magazine_no=?;", (magazine.received_date,magazine.lend_id,))
                return True
            except:
                return False'''
            print(magazine.received_date)
            con.execute("UPDATE lend_magazine SET received_date=? WHERE lend_id=?;", (magazine.received_date, magazine.lend_id))
            return True
        con.close()


    def get_lend_magazine_records_by_stu_id(stu_id):
        con = database.db_connect()
        try:
            return con.execute("SELECT * FROM lend_magazine  WHERE stu_id=? "
                               "AND received_date = 'still not';",(stu_id,)).fetchall()
        except:
            return False
        con.close


    def get_magazine_no_by_lend_id(lend_id):
        con = database.db_connect()
        return con.execute("SELECT magazine_no FROM lend_magazine WHERE lend_id=?;",(lend_id,)).fetchall()
        con.close


    def get_all_lend_records(self):
        con = database.db_connect()
        return con.execute("SELECT * FROM lend_magazine").fetchall()
        con.close