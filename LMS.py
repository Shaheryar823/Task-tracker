class Item:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.__available = True  # private attribute

    def displayinfo(self) -> None:
        print(f"Title: {self.title}, Author: {self.author}")

    def borrow(self) -> None:
        if self.__available:
            self.__available = False
            print(f"Borrowed -> {self.title}")
        else:
            print(f"{self.title} is already borrowed")

    def returned(self) -> None:
        self.__available = True
        print(f"Returned -> {self.title}")


class Book(Item):
    def displayinfo(self) -> None:
        print(f"Book: {self.title}, by {self.author}, 250 pages")


class Magazine(Item):
    def displayinfo(self) -> None:
        print(f"Magazine: {self.title}, by {self.author}, Issue #25")


# Data
books_data = [
    ("Python 101", "Mark"),
    ("Learning Python", "Mark Lutz"),
    ("Fluent Python", "Luciano Ramalho"),
    ("Python Crash Course", "Eric Matthes"),
    ("Effective Python", "Brett Slatkin"),
    ("Automate the Boring Stuff with Python", "Al Sweigart"),
    ("Think Python", "Allen B. Downey"),
    ("Head First Python", "Paul Barry"),
    ("Python Cookbook", "David Beazley"),
    ("Programming Python", "Mark Lutz")
]

magazines_data = [
    ("TechWorld", "Alice"),
    ("Python Monthly", "Bob"),
    ("AI Today", "Carol"),
    ("Data Science Digest", "David"),
    ("Coding Weekly", "Eve"),
    ("Machine Learning Times", "Frank"),
    ("Programming Insights", "Grace"),
    ("Software Today", "Hannah"),
    ("Cyber Security Review", "Ian"),
    ("Developer's Journal", "Jack")
]

# Create objects
book_objects = [Book(title, author) for title, author in books_data]
magazine_objects = [Magazine(title, author) for title, author in magazines_data]

# Display books
print("📚 Books:")
for b in book_objects:
    b.displayinfo()

# Display magazines
print("\n📰 Magazines:")
for m in magazine_objects:
    m.displayinfo()

# Borrow/Return demo
print("\n💡 Borrow/Return Demo:")
book_demo = book_objects[-1]  # Last book "Programming Python"
book_demo.borrow()
book_demo.borrow()
book_demo.returned()
book_demo.borrow()
