list_of_books = []
from Librarian import(check_status,enter_the_name_of_books,authorization)
from Student_acess import(issue_a_book,return_a_book)
print("8624357 is the authorization number")
while True:
    print("Welcome to the library\n Enter (1):To add a book \n Enter (2):To check book status \n Enter (3):To issue a book \n Enter (4):To return a book \n Enter (5):To exit")
    command = int(input("Enter the command:"))
    if command == 5:
        print("Ok! terminating")
        break
    elif command == 1:
        
        authorised = authorization(0)# 8624357 is the authorization number
        if authorised == True:
            enter_the_name_of_books(list_of_books)
    elif command == 2:
            authorised = authorization(0)# 8624357 is the authorization number
            if authorised == True:
                check_status(list_of_books)
    elif command == 3:
        issue_a_book(list_of_books)
    elif command == 4:
        return_a_book(list_of_books)
    else:
         print("Invalid command")
    