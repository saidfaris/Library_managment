Phase 3 Code Challenge: Restaurants
This code challenge will help you practice your SQLAlchemy skills by building a restaurant review domain.

The challenge includes the following tasks:

Create migrations for the reviews table.
Write object relationship methods for the Review, Restaurant, and Customer classes.
Write aggregate and relationship methods for the Customer and Restaurant classes.
Instructions
Clone the repository and create a virtual environment.
Install the dependencies using pip install -r requirements.txt.
Run the migrations using flask db migrate.
Seed the database using flask db seed.
Run the tests using pytest.
Deliverables
The following deliverables are required for this challenge:

Review.customer()
Review.restaurant()
Restaurant.reviews()
Restaurant.customers()
Customer.reviews()
Customer.restaurants()
Customer.full_name()
Customer.favorite_restaurant()
Customer.add_review()
Customer.delete_reviews()
Review.full_review()
Restaurant.fanciest()
Restaurant.all_reviews()
Tips
Use the seeds.py file to create sample data to test your models and relationships.
Write error-free code is more important than completing all of the deliverables listed - prioritize writing methods that work over writing more methods that don't work.
You should test your code in the console as you write.
Submission
Once you have completed the challenge, submit your code to GitHub.

Resources
SQLAlchemy documentation: https://docs.sqlalchemy.org/en/14/
Flask documentation: https://flask.palletsprojects.com/en/2.1.x/
pytest documentation: https://docs.pytest.org/en/6.2.x/
