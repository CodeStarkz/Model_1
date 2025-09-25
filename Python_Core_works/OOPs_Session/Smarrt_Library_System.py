# Smart Library System

class Library():
    Library_Name= "City Central Library"

    def __init__(self,book_name,author_name,available_copies):
        self.book_name=book_name
        self.author_name=author_name
        self.available_copies=available_copies

    def book_info(self):
        print(f"Library_name:{Library.Library_Name},"
              f"Book_name:  {self.book_name},"
              f"Author_name: {self.author_name},"
              f"Available_Copies: {self.available_copies}")


    def borrow_book(self):
        if self.available_copies >0:
            self.available_copies -=1
            return(self.available_copies )
        else:
            return("Not avilable")


    def return_book(self):
        self.available_copies +=1
        return("Book returned successfully")

    @classmethod
    def change_library_name(cls,new_name):
        cls.Library_Name=new_name
        return(cls.Library_Name)

    @staticmethod
    def is_valid_book_name(book_name):
        if len(str(book_name)) >= 3:
            return(True)

        else:
            return(False)


#  ----------- Test Cases--------------------------
# Create objects
book1 = Library("Python Basics", "Guido", 2)
book2 = Library("Data Science 101", "Andrew", 1)

# Show info
book1.book_info()
book2.book_info()

# Borrow books
print(book1.borrow_book())  # should reduce available copies from 2 → 1
print(book1.borrow_book())  # should reduce available copies from 1 → 0
print(book1.borrow_book())  # should show "Not available"

# Return a book
print(book1.return_book())  # should increase copies from 0 → 1

# Change library name
print(Library.change_library_name("National Digital Library"))
book1.book_info()  # new library name reflect hoga

# Check valid book names
print(Library.is_valid_book_name("AI"))     # False (length < 3)
print(Library.is_valid_book_name("ML101"))  # True


