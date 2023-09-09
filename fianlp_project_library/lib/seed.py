from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import User, Student, Book, BookBorrower, Base


DATABASE_URL = "sqlite:///library.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()


for _ in range(100):
    user = User(
        user_name=fake.user_name(),
        email=fake.email(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        phone_number=fake.phone_number(),
        address=fake.address(),
    )
    session.add(user)



for _ in range(25):
    student = Student(
        name=fake.name(),
        address=fake.address(),
        school_name=fake.word(),
        user_id=fake.random_element(elements=session.query(User).all()).id,
    )
    session.add(student)


for _ in range(200):
    book = Book(
        title=fake.catch_phrase(),
        author=fake.name(),
        shelf_number=fake.random_int(min=1, max=10),
        description=fake.text(),
    )
    session.add(book)


for _ in range(80):
    borrower = BookBorrower(
        user_id=fake.random_element(elements=session.query(User).all()).id,
        book_id=fake.random_element(elements=session.query(Book).all()).id,
        borrowed_date=fake.date(),
        borrowed_time=fake.time(),
        return_date=fake.date(),
        return_time=fake.time(),
        borrower_address=fake.address(),
    )
    session.add(borrower)

session.commit()
