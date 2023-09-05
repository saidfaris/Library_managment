from database import session
from models import Restaurant, Review, Customer

if __name__ == '__main__':
    # sample restaurants
    restaurant1 = Restaurant(name="Restaurant A", price=30000)
    restaurant2 = Restaurant(name="Restaurant B", price=20000)
    restaurant3 = Restaurant(name="Restaurant C", price=40000)

    # sample customers
    customer1 = Customer(first_name="John", last_name="Doe")
    customer2 = Customer(first_name="Jane", last_name="Smith")
    customer3 = Customer(first_name="Alice", last_name="Johnson")

    # sample reviews
    review1 = Review(review = 'It was a good place',star_rating=5, restaurant=restaurant1, customer=customer1)
    review2 = Review(review = 'Good food!',star_rating=4, restaurant=restaurant2, customer=customer2)
    review3 = Review(review = 'Great place but bad food',star_rating=3, restaurant=restaurant3, customer=customer3)
    review4 = Review(review = 'Decent waiters',star_rating=4, restaurant=restaurant1, customer=customer2)
    review5 = Review(review = 'Loved it!',star_rating=5, restaurant=restaurant2, customer=customer3)

    # session.add_all([restaurant1, restaurant2, restaurant3, customer1, customer2, customer3, review1, review2, review3, review4, review5])
    # session.commit()

    # # Close the session
    # session.close()
    
    
    print(review1.full_review())
    print(restaurant1.all_reviews())
    Restaurant.fanciest()
    
    print(customer3.favorite_restaurant())
    print(customer3.full_name())
    
    # customer3.add_review(restaurant2, 5, review='This is a added review!')
    
    print(customer3.customer_reviews())
    print(customer3.customer_restaurants())
    
    print(restaurant1.restaurant_reviews())
    print(restaurant1.restaurant_customers())
    
    
    print(review1.full_review())