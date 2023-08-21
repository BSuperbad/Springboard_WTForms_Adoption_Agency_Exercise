"""Seed file to make sample data for adoption_db"""

from models import Pet, db
from app import app

with app.app_context():
    # Create all tables
    db.drop_all()
    db.create_all()

    jack = Pet(name='Jack', species='dog',
               photo_url="https://www.southernliving.com/thmb/ZuS1MlY7N7G67Lyvl2zDIoktRDU=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/gettyimages-837898820-1-4deae142d4d0403dbb6cb542bfc56934.jpg")
    test1 = Pet(name='Jack', species='dog',
                photo_url="https://www.southernliving.com/thmb/ZuS1MlY7N7G67Lyvl2zDIoktRDU=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/gettyimages-837898820-1-4deae142d4d0403dbb6cb542bfc56934.jpg")
    test2 = Pet(name='Jack', species='dog',
                photo_url="https://www.southernliving.com/thmb/ZuS1MlY7N7G67Lyvl2zDIoktRDU=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/gettyimages-837898820-1-4deae142d4d0403dbb6cb542bfc56934.jpg")
    test3 = Pet(name='Jack', species='dog',
                photo_url="https://www.southernliving.com/thmb/ZuS1MlY7N7G67Lyvl2zDIoktRDU=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/gettyimages-837898820-1-4deae142d4d0403dbb6cb542bfc56934.jpg")
    test4 = Pet(name='Jack', species='dog',
                photo_url="https://www.southernliving.com/thmb/ZuS1MlY7N7G67Lyvl2zDIoktRDU=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/gettyimages-837898820-1-4deae142d4d0403dbb6cb542bfc56934.jpg")
    test5 = Pet(name='Jack', species='dog',
                photo_url="https://www.southernliving.com/thmb/ZuS1MlY7N7G67Lyvl2zDIoktRDU=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/gettyimages-837898820-1-4deae142d4d0403dbb6cb542bfc56934.jpg")

    db.session.add_all([jack, test1, test2, test3, test4, test5])

    db.session.commit()
