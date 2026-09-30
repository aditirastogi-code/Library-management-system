def issue_a_book(book_list:list):
    book_name = input("Enter the book name:")
    book_name = book_name.lower()
    reg_no =input("Enter your registration number:")
    reg_no = reg_no.lower()
    found = False
    for book in book_list:
        if book["Book name"] == book_name and book["available"]>0:
            found = True
            print("The book is available")
            print("Here remember to return the book")
            book["reg_no"].append(reg_no)
            book["available"] = book["available"]-1
            break
        elif book["Book name"] == book_name and book["available"]==0:
            found = True
            print("The book is not available")
            waitlist = input("But do you want to be in waitlist ?")
            if (waitlist).lower() == "yes":
                book["waiting_list"].append(reg_no)
                print(f"Okay you are on {len(book['waiting_list'])} in the waiting list.\n We will notify you once the book is ready to be issued")
            else:
                print("Ok thanks,\n Do you want to borrow any other book?")
            break
    if found == False:
        print("There is no such book in our library")
def return_a_book(book_list:list):
    book_name = input("Enter the book name")
    book_name = book_name.lower()
    reg_no = input("Enter your registration number")
    reg_no = reg_no.lower()
    days = int(input("Enter the number of days the book was borrowed for:"))
    for book in book_list:
        if book["Book name"]==book_name and reg_no not in book["reg_no"]:
                print("No record of this student borrowing this book.")
                return
        if book["Book name"]==book_name and reg_no in book["reg_no"]:
            book["reg_no"].remove(reg_no)
            book["available"] +=1
            if days > 7 :
                    basic_fine = 250
                    no_of_weeks = ((days-8)//7)
                    fine  = basic_fine + no_of_weeks*10
                    print("The amount of fine is",fine)
                    print("Return the book on time next time!!")
