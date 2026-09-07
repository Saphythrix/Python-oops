class Book:
    def __init__(self,title,author,isbn,pages):
        self.__title=title
        self.__author=author
        self.isbn=isbn
        self.pages=pages
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self,value):
        self.__author=value



class Author:
    def __init__(self,name,birth_year,books):
        self.__name=name
        self.birth_year=birth_year
        self.books=books

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name=value

class Library:
    def __init__(self,name, books):
        self.name=name
        self.books=books

    def add_book(self,book):
        self.books.append(book)
        print(f"{book.title} added successfully")

    def search_by_title(self,title):
        for obj in self.books:
            if obj.title==title:
                print("Book exist")
                print(f"Book Details:- {obj.title}\n {obj.author.name}\n {obj.isbn} \n{obj.pages}")
                return
            else:
                print("Book doesn't exist")

    def search_by_author(self,author_name):
        for obj in self.books:
            if obj.author.name==author_name:
                print("Author exist")
                print(f"Author Details:- {obj.author.name} \n {obj.author.birth_year}\n{[book.title for book in obj.author.books]}")
                return 
            else:
                print("Author not found")

    def get_total_pages(self,book):
        for obj in self.books:
            if obj==book:
                return obj.pages

        else:
            print("Book not found")

def main():
    
    author1 = Author("George Orwell", 1903, [])
    author2 = Author("J.K. Rowling", 1965, [])
    author3 = Author("J.R.R. Tolkien", 1892, [])

    book1 = Book("1984", author1, "9780451524935", 328)
    book2 = Book("Harry Potter", author2, "9780747532743", 309)
    book3 = Book("The Hobbit", author3, "9780547928227", 310)
    book4 = Book("Harry Potter PAKB", author2, "9780747532744", 350)
    book5 = Book("Rich dad,Poor dad", author1, "9780747532754", 360)

    author1.books.append(book1)
    author1.books.append(book5)

    author2.books.append(book2)
    author2.books.append(book4)

    author3.books.append(book3)

    l1=Library("Royal Book Corner",[book2,book4])
    l2=Library("Book House",[book1,book3])

    l2.add_book(book5)
    l1.search_by_title("Harry Potter")
    l1.search_by_author("J.K. Rowling")
    l2.get_total_pages(book5)

if __name__ == "__main__":
    main()