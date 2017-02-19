from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    ''' Person doing the buying '''
    __tablename__ = 'user'

    # Users will be identified by barcode / swipe card
    id = Column(String, primary_key=True)
    # Friendly name of the User
    name = Column(String)
    # Contact address
    email = Column(String)
    # Are they an admin
    is_admin = Column(Boolean)

class Product(Base):
    ''' Item for sale.'''
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('product.id'))
    # Barcode for the particular product
    upc = Column(String)
    # Human readable name
    name = Column(String)
    # How much this product is worth to customers. AKA suggested donation amount
    cost = Column(Float)
    # How many do we have in stock
    qty = Column(Integer)
    # Products can contain other products like a 24 can box of softy drinkums
    contains = relationship("Product", remote_side=[id])
    # How man child prodcts does this have?
    contains_qty = Column(Integer)
    pass

class Purchase(Base):
    ''' Keeps track of who bought what '''
    __tablename__ = 'purchase'

    # Some unique indentifier doodle
    id = Column(Integer, primary_key=True)
    # When did the purchase happen
    date = Column(DateTime)
    # How many items did they buy this purchase
    qty = Column(Integer)
    # Cost. Because we're a donation after all
    cost = Column(Float)
    # Who bought the thing
    user = Column(Integer, ForeignKey('user.id'))
    # What was the thing?
    product = Column(Integer, ForeignKey('product.id'))

    pass
