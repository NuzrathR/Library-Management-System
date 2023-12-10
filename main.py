

import database
from Book import Book
from Magazine import Magazine
from Dvd import Dvd
from Cd import Cd
from LendBook import LendBook
from LendMagazine import LendMagazine
from LendDvd import LendDvd
from LendCd import LendCd
from datetime import datetime

MAIN_MENU = "********************* Library Management System *********************" \
            "\nPlease choose option" \
            "\n1. Add new resources" \
            "\n2. Remove resources" \
            "\n3. Available resources" \
            "\n4. Unavailable resources" \
            "\n5. Search by subject" \
            "\n6. Lend resources" \
            "\n7. Receive resources" \
            "\n8. Exit"

SUB_MENU_ADD_RESOURCE = "********** Add new resources **********" \
                        "\n1. Add book" \
                        "\n2. Add Magazine" \
                        "\n3. Add Educational DVD" \
                        "\n4. Add Lecture CD" \
                        "\n5. Back"

SUB_MENU_REMOVE_RESOURCE = "********** Remove resources **********" \
                        "\n1. Remove book" \
                        "\n2. Remove Magazine" \
                        "\n3. Remove Educational DVD" \
                        "\n4. Remove Lecture CD" \
                        "\n5. Back"

SUB_MENU_LEND_RESOURCE = "********** Lend resources **********" \
                        "\n1. Lend book" \
                        "\n2. Lend Magazine" \
                        "\n3. Lend Educational DVD" \
                        "\n4. Lend Lecture CD" \
                        "\n5. Back"

SUB_MENU_RECEIVE_RESOURCE = "********** Receive resources **********" \
                        "\n1. Receive book" \
                        "\n2. Receive Magazine" \
                        "\n3. Receive Educational DVD" \
                        "\n4. Receive Lecture CD" \
                        "\n5. Back"

def terminal():

    database.create_tables()
    database.insert_subject()

    print(Book.getAllBooks(0))
    while(True):

        print(MAIN_MENU)
        main_option = input("Your option: ")

        if main_option == '1': # add new resources
            while(True):
                print(SUB_MENU_ADD_RESOURCE)
                sub_option = input("Your option: ")

                if sub_option == '1': #add new book
                    print("************ Add new book ************")
                    isbn = title = format = subject = rental_price = no_of_copies = current_stock = None

                    while(True):
                        isbn = input('ISBN: ')
                        if len(isbn) != 0:
                            break
                        else:
                            print('Invalid ISBN...')

                    while(True):
                        title = input('Title: ')
                        if len(title) != 0:
                            break
                        else:
                            print('Invalid Title...')

                    while(True):
                        format = input('Format [1. Hardcover | 2. Paperback]: ')
                        if format in ('1','2'):
                            if format == '1':
                                format = 'Hardcover'
                            else:
                                format = 'Paperback'
                            break
                        else:
                            print('Invalid Format...')

                    while(True):
                        subject = input('Subject [1. Science | 2. History | 3. Literature]: ')
                        if subject in ('1','2','3'):
                            break
                        else:
                            print('Invalid Subject...')

                    while(True):
                        rental_price = input('Rental price: ')
                        if rental_price.isnumeric() and rental_price != '0':
                            break
                        else:
                            print('Invalid Rental pric...')

                    while(True):
                        no_of_copies =input('No of Copies: ')
                        if no_of_copies.isnumeric():
                            current_stock = no_of_copies
                            break
                        else:
                            print('Invalid No of Copies...')

                    book = Book(isbn,title,format,subject,rental_price,no_of_copies,current_stock)
                    if Book.insert_book(book):
                        print('Succeefully saved a book...')
                    else:
                        print('Already saved this book...')
                    print(book.getAllBooks())

                elif sub_option == '2':  #add new magazine
                    print("************ Add new magazine ************")
                    magazine_no = title = print_type = subject = rental_price = no_of_copies = current_stock = None

                    while (True):
                        magazine_no = input('Magazine No: ')
                        if len(magazine_no) != 0:
                            break
                        else:
                            print('Invalid Magazine No...')

                    while (True):
                        title = input('Title: ')
                        if len(title) != 0:
                            break
                        else:
                            print('Invalid Title...')

                    while (True):
                        print_type = input('Print [1. color | 2. black&white]: ')
                        if print_type in ('1', '2'):
                            if print_type == '1':
                                print_type = 'color'
                            else:
                                print_type = 'black&white'
                            break
                        else:
                            print('Invalid Print...')

                    while (True):
                        subject = input('Subject [1. Science | 4. Technology | 5. Sport]: ')
                        if subject in ('1', '4', '5'):
                            break
                        else:
                            print('Invalid Subject...')

                    while (True):
                        rental_price = input('Rental price: ')
                        if rental_price.isnumeric() and rental_price != '0':
                            break
                        else:
                            print('Invalid Rental price...')

                    while (True):
                        no_of_copies = input('No of Copies: ')
                        if no_of_copies.isnumeric():
                            current_stock = no_of_copies
                            break
                        else:
                            print('Invalid No of Copies...')

                    magazine = Magazine(magazine_no, title, print_type, subject, rental_price, no_of_copies,current_stock)
                    if Magazine.insert_magazine(magazine):
                        print('Succeefully saved a magazine...')
                    else:
                        print('Already saved this magazine...')

                elif sub_option == '3': # add new dvd
                    print("************ Add new Educational DVD ************")
                    dvd_no = title =  subject = rental_price = no_of_copies = current_stock = None

                    while (True):
                        dvd_no = input('DVD No: ')
                        if len(dvd_no) != 0:
                            break
                        else:
                            print('Invalid DVD No...')

                    while (True):
                        title = input('Title: ')
                        if len(title) != 0:
                            break
                        else:
                            print('Invalid Title...')

                    while (True):
                        subject = input('Subject [4. Technology | 6. Astronomy | 7. Math]: ')
                        if subject in ('4', '6', '7'):
                            break
                        else:
                            print('Invalid Subject...')

                    while (True):
                        rental_price = input('Rental price: ')
                        if rental_price.isnumeric() and rental_price != '0':
                            break
                        else:
                            print('Invalid Rental pric...')

                    while (True):
                        no_of_copies = input('No of Copies: ')
                        if no_of_copies.isnumeric():
                            current_stock = no_of_copies
                            break
                        else:
                            print('Invalid No of Copies...')

                    dvd = Dvd(dvd_no, title, subject, rental_price, no_of_copies,current_stock)
                    if Dvd.insert_dvd(dvd):
                        print('Succeefully saved a magazine...')
                    else:
                        print('Already saved this magazine...')

                elif sub_option == '4': # add new cd
                    print("************ Add new Lecture CD ************")
                    cd_no = title = subject = rental_price = no_of_copies = current_stock = None

                    while (True):
                        cd_no = input('CD No: ')
                        if len(cd_no) != 0:
                            break
                        else:
                            print('Invalid CD No...')

                    while (True):
                        title = input('Title: ')
                        if len(title) != 0:
                            break
                        else:
                            print('Invalid Title...')

                    while (True):
                        subject = input('Subject [7. Math | 8. Music | 9. Foreign Language]: ')
                        if subject in ('7', '8', '9'):
                            break
                        else:
                            print('Invalid Subject...')

                    while (True):
                        rental_price = input('Rental price: ')
                        if rental_price.isnumeric() and rental_price != '0':
                            break
                        else:
                            print('Invalid Rental pric...')

                    while (True):
                        no_of_copies = input('No of Copies: ')
                        if no_of_copies.isnumeric():
                            current_stock = no_of_copies
                            break
                        else:
                            print('Invalid No of Copies...')

                    cd = Cd(cd_no, title, subject, rental_price, no_of_copies,current_stock)
                    if Cd.insert_cd(cd):
                        print('Succeefully saved a magazine...')
                    else:
                        print('Already saved this magazine...')
                    print(cd.getAllCds())

                elif sub_option == '5':
                    break
                else:
                  print('Invalid option...')

        elif main_option == '2': # remove resources
           while(True):
                print(SUB_MENU_REMOVE_RESOURCE)
                sub_option = input('Your option: ')

                if sub_option == '1': # remove book
                    print("************ Remove  book ************")
                    isbn = None
                    while(True):
                        isbn = input('ISBN: ')
                        if len(isbn) != 0:
                            break
                        else:
                            print('Invalid ISBN...')

                    if Book.delete_book_by_isbn(isbn):
                        print('Successfully deleted...')
                    else:
                        print('Error...')

                elif sub_option == '2': # remove magazine
                    print("************ Remove  magazine ************")
                    magazine_no = None
                    while (True):
                        magazine_no = input('Magazine No: ')
                        if len(magazine_no) != 0:
                            break
                        else:
                            print('Invalid Magazine No...')

                    if Magazine.delete_magazine_by_no(magazine_no):
                        print('Successfully deleted...')
                    else:
                        print('Error...')

                elif sub_option == '3': # remove dvd
                    print("************ Remove DVD ************")
                    dvd_no = None
                    while (True):
                        dvd_no = input('DVD No: ')
                        if len(dvd_no) != 0:
                            break
                        else:
                            print('Invalid DVD No...')

                    if Dvd.delete_dvd_by_no(dvd_no):
                        print('Successfully deleted...')
                    else:
                        print('Error...')

                elif sub_option == '4': # remove cd
                    print("************ Remove CD ************")
                    cd_no = None
                    while (True):
                        cd_no = input('CD No: ')
                        if len(cd_no) != 0:
                            break
                        else:
                            print('Invalid CD No...')

                    if Cd.delete_cd_by_no(cd_no):
                        print('Successfully deleted...')
                    else:
                        print('Error...')

                elif sub_option == '5':
                    break

        elif main_option == '6': # lend resources

            while (True):
                print(SUB_MENU_LEND_RESOURCE)
                sub_option = input('Your option: ')

                if sub_option == '1':  # lend book
                    print("************ Lend  book ************")
                    isbn = stu_id = None
                    while (True):
                        isbn = input('ISBN: ')
                        if len(isbn) != 0:
                            break
                        else:
                            print('Invalid ISBN...')

                    while (True):
                        stu_id = input('Student ID: ')
                        if len(stu_id) != 0:
                            break
                        else:
                            print('Invalid Student ID...')

                    lend_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    received_date = 'still not'

                    lend_book = LendBook(0,isbn,stu_id,lend_date,received_date)

                    if LendBook.insert_lend_book_record(lend_book):
                        if Book.lend_book(isbn):
                            print('Successfully Lend..')
                    else:
                        print('Error...')

                    print(Book.getAllBooks(0))
                    print(lend_book.get_all_lend_records())

                elif sub_option == '2':  # lend magazine
                    print("************ Lend  Magazine ************")
                    magazine_no = stu_id = None
                    while (True):
                        magazine_no = input('Magazine No: ')
                        if len(magazine_no) != 0:
                            break
                        else:
                            print('Invalid Magazine No...')

                    while (True):
                        stu_id = input('Student ID: ')
                        if len(stu_id) != 0:
                            break
                        else:
                            print('Invalid Student ID...')

                    lend_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    received_date = 'still not'

                    lend_magazine = LendMagazine(0, magazine_no, stu_id, lend_date, received_date)

                    if LendMagazine.insert_lend_magazine_record(lend_magazine):
                        if Magazine.lend_magazine(magazine_no):
                            print('Successfully Lend..')
                    else:
                        print('Error...')

                    print(Magazine.getAllMagazines(0))
                    print(lend_magazine.get_all_lend_records())
                elif sub_option == '3':  # lend dvd
                    print("************ Lend  DVD ************")
                    dvd_no = stu_id = None
                    while (True):
                        dvd_no = input('DVD No: ')
                        if len(dvd_no) != 0:
                            break
                        else:
                            print('Invalid DVD No...')
                    while (True):
                        stu_id = input('Student ID: ')
                        if len(stu_id) != 0:
                            break
                        else:
                            print('Invalid Student ID...')

                    lend_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    received_date = 'still not'

                    lend_dvd = LendDvd(0, dvd_no, stu_id, lend_date, received_date)

                    if LendDvd.insert_lend_dvd_record(lend_dvd):
                        if Dvd. lend_dvd(dvd_no):
                            print('Successfully Lend..')
                    else:
                        print('Error...')

                    print(Dvd.getAllDvds(0))
                    print(lend_dvd.get_all_lend_records())

                elif sub_option == '4':  # lend cd
                    print("************ Lend  CD ************")
                    cd_no = stu_id = None
                    while (True):
                        cd_no = input('CD No: ')
                        if len(cd_no) != 0:
                            break
                        else:
                            print('Invalid CD No...')

                    while (True):
                        stu_id = input('Student ID: ')
                        if len(stu_id) != 0:
                            break
                        else:
                            print('Invalid Student ID...')

                    lend_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    received_date = 'still not'

                    lend_cd = LendCd(0, cd_no, stu_id, lend_date, received_date)

                    if LendCd.insert_lend_cd_record(lend_cd):
                        if Cd.lend_cd(cd_no):
                            print('Successfully Lend..')
                    else:
                        print('Error...')

                    print(Cd.getAllCds(0))
                    print(lend_cd.get_all_lend_records())

                elif sub_option == '5':
                    break
        elif main_option == '7': # receive resources
            while (True):
                print(SUB_MENU_RECEIVE_RESOURCE)
                sub_option = input('Your option: ')

                if sub_option == '1':  # receive book
                    print("************ Receive  book ************")
                    while (True):
                        stu_id = input('Student ID: ')
                        if len(stu_id) != 0:
                            break
                        else:
                            print('Invalid Student ID...')

                    book_records = LendBook.get_lend_book_records_by_stu_id(stu_id)

                    print('########################### Lend Books ###############################'
                          '\n\t Lend Id |\tISBN\t|\t\t\t\tLendDate\t|\tReceived Date ')
                    for rec in book_records:
                        print('\t\t', rec[0], '\t|\t', rec[1], '\t|\t', rec[3], '\t|\t', rec[4])

                    magazine_records = LendMagazine.get_lend_magazine_records_by_stu_id(stu_id)

                    print('########################### Lend Magazines ###############################'

                          '\n\t Lend Id |\tmagazine_no\t|\t\t\t\tLendDate\t|\tReceived Date ')
                    for rec in magazine_records:
                        print('\t\t', rec[0], '\t|\t', rec[1], '\t|\t', rec[3], '\t|\t', rec[4])

                    dvd_records = LendDvd.get_lend_dvd_records_by_stu_id(stu_id)

                    print('########################### Lend DVDs ###############################'

                          '\n\t Lend Id |\tdvd_no\t|\t\t\t\tLendDate\t|\tReceived Date ')
                    for rec in dvd_records:
                        print('\t\t', rec[0], '\t|\t', rec[1], '\t|\t', rec[3], '\t|\t', rec[4])

                    cd_records = LendCd.get_lend_cd_records_by_stu_id(stu_id)

                    print('########################### Lend CDs ###############################'

                          '\n\t Lend Id |\tcd_no\t|\t\t\t\tLendDate\t|\tReceived Date ')
                    for rec in cd_records:
                        print('\t\t', rec[0], '\t|\t', rec[1], '\t|\t', rec[3], '\t|\t', rec[4])



                    while (True):
                        lend_id = input('Lend ID: ')
                        if len(lend_id) != 0:
                            break
                        else:
                            print('Invalid Lend ID...')

                    received_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    lend_book = LendBook(lend_id, 0, 0, 0, received_date)
                    # isbn = LendBook.get_isbn_by_lend_id(lend_id)
                    # print(isbn[0][0])
                    if LendBook.update_lend_book_record(lend_book):
                        isbn = LendBook.get_isbn_by_lend_id(lend_id)
                        if Book.received_book(isbn[0][0]):
                            print('Successfully reveived...')
                    else:
                        print('Error...')

                    print(Book.getAllBooks(0))
                    print(LendBook.get_all_lend_records(0))

                elif sub_option == '2':  # receive magazine

                    print("************ Receive  magazine ************")
                    while (True):
                        lend_id = input('Lend ID: ')
                        if len(lend_id) != 0:
                            break
                        else:
                            print('Invalid Lend ID...')


                    received_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    lend_magazine = LendMagazine(lend_id, 0, 0, 0, received_date)
                    # isbn = LendBook.get_isbn_by_lend_id(lend_id)
                    # print(isbn[0][0])
                    if LendMagazine.update_lend_magazine_record(lend_magazine):
                      magazine_no = LendMagazine.get_magazine_no_by_lend_id(lend_id)
                    if Magazine.received_magazine(magazine_no[0][0]):
                        print('Successfully received...')
                    else:
                        print('Error...')

                        print(Magazine.getAllMagazines(0))
                        print(LendMagazine.get_all_lend_records(0))


                elif sub_option == '3':  # receive dvd
                        print("************ Receive  DVD ************")


                while (True):
                         lend_id = input('Lend ID: ')
                if len(lend_id) != 0:
                         break
                else:
                    print('Invalid Lend ID...')

                    received_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    lend_dvd = LendDvd(lend_id, 0, 0, 0, received_date)
                    # isbn = LendBook.get_isbn_by_lend_id(lend_id)
                    # print(isbn[0][0])
                    if LendDvd.update_lend_dvd_record(lend_dvd):
                       dvd_no = LendDvd.get_dvd_no_by_lend_id(lend_id)
                    if Dvd.received_dvd(dvd_no[0][0]):
                        print('Successfully received...')
                    else:
                       print('Error...')

                       print(Dvd.getAllDvds(0))
                       print(LendDvd.get_all_lend_records(0))





        elif sub_option == '4':  # receive cd

                 print("************ Receive  CD ************")


                 while (True):
                          lend_id = input('Lend ID: ')
                 if len(lend_id) != 0:
                          break
                 else:
                      print('Invalid Lend ID...')

                 received_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                 lend_cd = LendCd(lend_id, 0, 0, 0, received_date)
                 # isbn = LendBook.get_isbn_by_lend_id(lend_id)
                 # print(isbn[0][0])
                 if LendCd.update_lend_cd_record(lend_cd):
                  cd_no = LendCd.get_cd_no_by_lend_id(lend_id)
                 if Cd.received_cd(cd_no[0][0]):
                    print('Successfully received...')
                 else:
                   print('Error...')

                   print(Cd.getAllCds(0))
                   print(LendCd.get_all_lend_records(0))


        elif sub_option == '5':

                    break


        else:

            print('Invalid option...')


terminal()