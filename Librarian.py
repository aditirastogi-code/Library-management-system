def authorization(number:int):
    authorization_no = 8624357
    attempt = 0
    while attempt <=3:
        x = int(input("Enter the authorisation no.:"))
            
        if authorization_no == x:
            return True
        
        else:
            if attempt == 3:
                print("Trial limit reached")
                print("Access denied")
                return False
            print(f"Access denied \nTry again\n You have {3-attempt} left")
            attempt+=1

def enter_the_name_of_books(book_list:list):
    book_name = input("Enter book name:")
    book_id = input("Enter book ID:")
    author_name = input("Enter the author name:")
    category = input("Enter category of the book:")
    no_of_books = int(input("Enter the number of books:"))
    my_dictionary = {"Book name":book_name.lower(), "Id" : book_id ,"author name" :author_name ,"category":category , "available" : no_of_books 
                     , "reg_no":[], "waiting_list":[]}
    book_list.append(my_dictionary)
    return book_list
    
def check_status(book_list:list):
    print("This is the status of the books")
    for item in book_list:
        for key,value in item.items():
            print(f"{key}:{value}")     

    
