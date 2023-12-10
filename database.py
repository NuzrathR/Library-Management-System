import sqlite3

def db_connect():
    return sqlite3.connect('library.db')

def create_tables():
    con = db_connect()
    with con:
        con.execute(
            "CREATE TABLE IF NOT EXISTS subject("
                    "sub_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "name TEXT); "
            )

        con.execute(
            "CREATE TABLE IF NOT EXISTS book("
                "isbn VARCHAR PRIMARY KEY,"
                "title TEXT,"
                "format TEXT,"
                "sub_id INTEGER,"
                "rental_price REAL,"
                "no_of_copies INTEGER,"
                "current_stock INTEGER DEFAULT 0,"
                "FOREIGN KEY(sub_id) REFERENCES subject(sub_id) );"
        )

        con.execute(
            "CREATE TABLE IF NOT EXISTS magazine("
            "magazine_no VARCHAR PRIMARY KEY,"
            "title TEXT,"
            "print_type TEXT,"
            "sub_id INTEGER,"
            "rental_price REAL,"
            "no_of_copies INTEGER,"
            "current_stock INTEGER,"
            "FOREIGN KEY(sub_id) REFERENCES subject(sub_id) );"
        )

        con.execute(
            "CREATE TABLE IF NOT EXISTS dvd("
            "dvd_no VARCHAR PRIMARY KEY,"
            "title TEXT,"            
            "sub_id INTEGER,"
            "rental_price REAL,"
            "no_of_copies INTEGER,"
            "current_stock INTEGER,"
            "FOREIGN KEY(sub_id) REFERENCES subject(sub_id) );"
        )

        con.execute(
            "CREATE TABLE IF NOT EXISTS cd("
            "cd_no VARCHAR PRIMARY KEY,"
            "title TEXT,"
            "sub_id INTEGER,"
            "rental_price REAL,"
            "no_of_copies INTEGER,"
            "current_stock INTEGER,"
            "FOREIGN KEY(sub_id) REFERENCES subject(sub_id) );"
        )

        con.execute(
            "CREATE TABLE IF NOT EXISTS lend_book("
            "lend_id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "isbn VARCHAR,"
            "stu_id VARCHAR,"
            "lend_date TEXT,"
            "received_date TEXT,"            
            "FOREIGN KEY(isbn) REFERENCES book(isbn) );"
        )

        con.execute(
            "CREATE TABLE IF NOT EXISTS lend_magazine("
            "lend_id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "magazine_no VARCHAR,"
            "stu_id VARCHAR,"
            "lend_date TEXT,"
            "received_date TEXT,"
            "FOREIGN KEY(magazine_no) REFERENCES magazine(magazine_no) );"
        )

        con.execute(
            "CREATE TABLE IF NOT EXISTS lend_dvd("
            "lend_id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "dvd_no VARCHAR,"
            "stu_id VARCHAR,"
            "lend_date TEXT,"
            "received_date TEXT,"
            "FOREIGN KEY(dvd_no) REFERENCES dvd(dvd_no) );"
        )

        con.execute(
            "CREATE TABLE IF NOT EXISTS lend_cd("
            "lend_id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "cd_no VARCHAR,"
            "stu_id VARCHAR,"
            "lend_date TEXT,"
            "received_date TEXT,"
            "FOREIGN KEY(cd_no) REFERENCES cd(cd_no) );"
        )

    con.close()


def insert_subject():
    con = db_connect()
    with con:
        if len(getAllSubject()) == 0:
            con.execute("INSERT INTO subject(name) VALUES ('Science');")
            con.execute("INSERT INTO subject(name) VALUES ('History');")
            con.execute("INSERT INTO subject(name) VALUES ('Literature');")
            con.execute("INSERT INTO subject(name) VALUES ('Technology');")
            con.execute("INSERT INTO subject(name) VALUES ('Sport');")
            con.execute("INSERT INTO subject(name) VALUES ('Astronomy');")
            con.execute("INSERT INTO subject(name) VALUES ('Math');")
            con.execute("INSERT INTO subject(name) VALUES ('Music');")
            con.execute("INSERT INTO subject(name) VALUES ('Foreign Language');")
    con.close()


def getAllSubject():
    con = db_connect()
    with con:
        #print(con.execute("SELECT * FROM subject").fetchall())
        return con.execute("SELECT * FROM subject").fetchall()
    con.close()




