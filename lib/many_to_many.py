class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        """Return a list of contracts for this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return a list of authors who have contracts for this book."""
        return list({contract.author for contract in self.contracts()})  # Unique authors


class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        """Return a list of contracts for this author."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return a list of books the author has contracts for."""
        return list({contract.book for contract in self.contracts()})  # Unique books

    def sign_contract(self, book, date, royalties):
        """Create a contract for this author with a book."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return the total royalties earned by this author."""
        return sum(contract.royalties for contract in self.contracts())

class Contract:
    all = []  # Store all contract instances

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return a list of contracts sorted by date."""
        return [contract for contract in cls.all if contract.date == date]

