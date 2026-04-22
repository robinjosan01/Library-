books=[]
issued_books=[]

# ^ ADD BOOKS
def add_books():
    name=input("Enter the name of the books:")
    books.append(name)
    print("Books added")
    
    
# ^ SHOW BOOKS
def show_books():
    if len(books) == 0:
        print("No books available")
    else:
        print("Books available")
        for b in books:
            print(b)
            
# ^ ISSUE BOOKS
def issue_books():
    show_books()
    name=input("The books name:")
    if name in books:
        books.remove(name)
        issued_books.append(name)
        print("Books issued")
    else:
        print("There is no book to issue")
        
# ^ RETURN BOOKS
def return_books():
    name=input("The books name:")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print("Books returned")
    else:
        print("No books returned")
        
        
        
        
# ! MAIN BODY
def library ():
    while True:
        print("\n1.Add Books")
        print("2.Show Books")
        print("3.Issue Books")
        print("4.Return Books")
        print("5.Exit")
        
        choice = int(input("Enter your choice:"))
        
        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_books()
        elif choice == 5:
            print("Thank you")
            break
        else:
            print("Invalid choice")
            break
        
#! RUN
library()
