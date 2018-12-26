import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, CategoryItem

# Tell application which database engine we want to use. We will use SQLite3
# Create sqlite3 database file
engine = create_engine('sqlite:///database.db')

# Bind engine to Base class, creating connection between our class definitions
# and their corrisponding tables
Base.metadata.bind = engine

# Create a sessionmaker object which is a line of communication between our
# code and the database engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


# Create dummy data to populate our app with starter data

# Baseball Category and Items:
category = Category(
    name = 'Baseball',
    user_id = 1
)

session.add(category)
session.commit()

item = CategoryItem(
    name = 'Baseball Glove',
    description = 'A leather mitt for shagging fly balls!',
    creation_date = datetime.datetime.now(),
    category = category,
)

session.add(item)
session.commit()

item = CategoryItem(
    name = 'Baseball Cleats',
    description = 'Metal spikes for extra traction',
    creation_date = datetime.datetime.now(),
    category = category
)

session.add(item)
session.commit()

item = CategoryItem(
    name = 'Baseball Bat',
    description = 'Louisville Slugger for smashing home runs',
    creation_date = datetime.datetime.now(),
    category = category
)

session.add(item)
session.commit()

# Surfing Category and Items
category = Category(
    name = 'Surfing',
    user_id = 1
)

session.add(category)
session.commit()

item = CategoryItem(
    name = 'Surfboard',
    description = 'The lateste technology for the best performance!',
    creation_date = datetime.datetime.now(),
    category = category
)

session.add(item)
session.commit()

item = CategoryItem(
    name = 'Wetsuit',
    description = 'The lateste technology for the best performance!',
    creation_date = datetime.datetime.now(),
    category = category
)

session.add(item)
session.commit()


# Camping Category and Items
category = Category(
    name = 'Camping',
    user_id = 1
)

session.add(category)
session.commit()
