
class Book:
    def __init__(self,title,author,genre,availability_status=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.availability_status =availability_status
        
    def is_available(self):
        if self.availability_status:
            return "Book is Available"
        else:
            return "Book not available"
        
    def borrowed_boosk(self):
        if self.availability_status:
            self.availability_status=False
            return f"{self.title} has been borrowed."
        else:
            return f"Sorry, {self.title} is not Available for borrowing."
            
    def returned_books(self):
        if not self.availability_status:
            self.availability_statuse = True
            return f"Thank you for returning {self.title}."
        else:
           return f"{self.title} was not borrowed, so it cannot be returned."
    
class Patron:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.borrowed_books=[]
        
        
    def borrow_book(self,book):
        if book.availability_status:
            self.borrowed_books.append(book)
            book.borrow()
            return f"{self.name} has borrowed {book.title}."

        else:
            return f"Sorry, {book.title} is not Available for borrowing."

            
            
    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.returned_book()
            return f"{self.name} has returned {book.title}."

        else:
            return f"{self.name} did not borrow {book.title}, so it cannot be returned."

            
            
    def display_borrowed_books(self,book):
        if len(self.borrowed_books)==0:
            return f"{self.name} has not borrowed any book so far"
        else:
            for book in self.borrowed_books:
                print(book.title)
    
class Library:
    def __init__(self, name,books,patron):
        self.name = name
        self.books = []
        self.patrons = []
        
    def add_book(self,book):
        self.books.append(book)
        return f"Book '{book.title}' has been added to the library."
    
    def register_patron(self,patron):
        if self.patrons.count(patron)>=1:
            return f"{patron} already exist, Register another patron"
        else:
            self.patrons.append(patron)
            return f"Patron '{patron.name}' has been registered."
    
    def display_borrowed_books(self,patron):
        patron.display_borrowed_books()
        
    def display_available_books(self):
        for book in self.books:
            if book.is_available():
                print(book.title)
                
                
    def display_registered_patron(self):
        for patron in self.patrons:
            print(patron.name)
   
   
   
class ReferenceBook:
    def __init__(self,title,author,genre,reference_id):
        super().__init__(title,author,genre)
        self.reference_id=reference_id
    
    def display_reference_id(self):
        print( f" Reference ID:",{self.reference_id})    