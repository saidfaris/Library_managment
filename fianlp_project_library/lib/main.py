import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Student, Book, BookBorrower



DATABASE_URL = "sqlite:///library.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def main():
    pass

@main.command()
@click.option('--title', prompt='Enter the book title')
@click.option('--author', prompt='Enter the author')
@click.option('--shelf_number', prompt='Enter the shelf number')
@click.option('--description', prompt='Enter the book description')
def add_book(title, author, shelf_number, description):
    book = Book(
        title=title,
        author=author,
        shelf_number=shelf_number,
        description=description
    )
    session.add(book)
    session.commit()
    click.echo("Book added successfully.")

@main.command()
@click.argument('book_id', type=int)
def delete_book(book_id):
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        click.echo("Book deleted successfully.")
    else:
        click.echo("Book not found.")

@main.command()
@click.option('--user_id', prompt='Enter user ID')
@click.option('--book_id', prompt='Enter book ID')
def borrow_book(user_id, book_id):
    user = session.query(User).get(user_id)
    book = session.query(Book).get(book_id)

    if user and book:
        if not any(borrower.user_id == user_id and borrower.book_id == book_id for borrower in book.borrowers):
            borrower = BookBorrower(
                user_id=user_id,
                book_id=book_id,
                borrowed_date="2023-09-09",  
                borrowed_time="10:00 AM",     
                return_date="",               
                return_time="",               
                borrower_address=user.address  
            )
            session.add(borrower)
            session.commit()
            click.echo("Book borrowed successfully.")
        else:
            click.echo("This book has already been borrowed by the user.")
    else:
        click.echo("User or book not found.")

@main.command()
@click.option('--user_id', prompt='Enter user ID')
@click.option('--book_id', prompt='Enter book ID')
def return_book(user_id, book_id):
    borrower = session.query(BookBorrower).filter_by(user_id=user_id, book_id=book_id).first()

    if borrower:
        borrower.return_date = "2023-09-16"  
        borrower.return_time = "02:00 PM"     
        session.commit()
        click.echo("Book returned successfully.")
    else:
        click.echo("Borrower not found.")

@main.command()
@click.option('--user_id', prompt='Enter user ID')
def delete_user(user_id):
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        click.echo("User deleted successfully.")
    else:
        click.echo("User not found.")

if __name__ == '__main__':
    main()
