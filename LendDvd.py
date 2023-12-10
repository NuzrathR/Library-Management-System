import database

class LendDvd:
    def __init__(self,lend_id,dvd_no,stu_id,lend_date,received_date):
        self.lend_id = lend_id
        self.dvd_no = dvd_no
        self.stu_id = stu_id
        self.lend_date = lend_date
        self.received_date = received_date



    def insert_lend_dvd_record(dvd):
        con = database.db_connect()
        with con:
            try:
                con.execute("INSERT INTO lend_dvd(dvd_no,stu_id,lend_date,received_date) VALUES"
                            "(?,?,?,?);",(dvd.dvd_no,dvd.stu_id,dvd.lend_date,dvd.received_date)
                )
                return True
            except:
                return False

        con.close()


    def update_lend_dvd_record(dvd):
        con = database.db_connect()
        with con:
            ''''try:
                con.execute("UPDATE lend_dvd SET received_date =? WHERE dvd_no=?;", (dvd.received_date,dvd.lend_id,))
                return True
            except:
                return False'''
            print(dvd.received_date)
            con.execute("UPDATE lend_dvd SET received_date=? WHERE lend_id=?;", (dvd.received_date, dvd.lend_id))
            return True
        con.close()


    def get_lend_dvd_records_by_stu_id(stu_id):
        con = database.db_connect()
        try:
            return con.execute("SELECT * FROM lend_dvd WHERE stu_id=? "
                               "AND received_date = 'still not';",(stu_id,)).fetchall()
        except:
            return False
        con.close


    def get_dvd_no_by_lend_id(lend_id):
        con = database.db_connect()
        return con.execute("SELECT dvd_no FROM lend_dvd WHERE lend_id=?;",(lend_id,)).fetchall()
        con.close


    def get_all_lend_records(self):
        con = database.db_connect()
        return con.execute("SELECT * FROM lend_dvd").fetchall()
        con.close