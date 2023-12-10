import database

class LendCd:
    def __init__(self,lend_id,cd_no,stu_id,lend_date,received_date):
        self.lend_id = lend_id
        self.cd_no = cd_no
        self.stu_id = stu_id
        self.lend_date = lend_date
        self.received_date = received_date



    def insert_lend_cd_record(cd):
        con = database.db_connect()
        with con:
            try:
                con.execute("INSERT INTO lend_cd(cd_no,stu_id,lend_date,received_date) VALUES"
                            "(?,?,?,?);",(cd.cd_no,cd.stu_id,cd.lend_date,cd.received_date)
                )
                return True
            except:
                return False

        con.close()


    def update_lend_cd_record(cd):
        con = database.db_connect()
        with con:
            ''''try:
                con.execute("UPDATE lend_cd SET received_date =? WHERE cd_no=?;", (cd.received_date,cd.lend_id,))
                return True
            except:
                return False'''
            print(cd.received_date)
            con.execute("UPDATE lend_cd SET received_date=? WHERE lend_id=?;", (cd.received_date, cd.lend_id))
            return True
        con.close()


    def get_lend_cd_records_by_stu_id(stu_id):
        con = database.db_connect()
        try:
            return con.execute("SELECT * FROM lend_cd WHERE stu_id=? "
                               "AND received_date = 'still not';",(stu_id,)).fetchall()
        except:
            return False
        con.close


    def get_cd_no_by_lend_id(lend_id):
        con = database.db_connect()
        return con.execute("SELECT cd_no FROM lend_cd WHERE lend_id=?;",(lend_id,)).fetchall()
        con.close


    def get_all_lend_records(self):
        con = database.db_connect()
        return con.execute("SELECT * FROM lend_cd").fetchall()
        con.close