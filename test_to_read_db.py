from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, CategoryItem

engine = create_engine('sqlite:///database.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Tests to verify data is properly populating tables

#Test to return all users in our database
read_user = session.query(User).all()
for i in read_user:
    print(i.id)
    print(i.name)
    print(i.email)

#Test to return all categories in our database
read_category = session.query(Category).all()
for i in read_category:
    print(i.name)

#Test to return all category items in our database
read_item = session.query(CategoryItem).all()
for i in read_item:
    # print(i.id)
    print(i.name)
    # print(i.category_id)

#Test for verify the last 5 recent item entries in our database
last_five = session.query(CategoryItem).order_by(CategoryItem.id.desc()).limit(
    5)
for i in last_five:
    print(i.name)
