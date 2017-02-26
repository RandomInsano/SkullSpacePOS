from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

Base = declarative_base()
class ItemBase(Base):
    ''' Taken from http://stackoverflow.com/a/22947975/187769 '''
    __abstract__ = True
    def ensure_defaults(self):
        for column in self.__table__.c:
            if getattr(self, column.name) is None and column.default is not None and column.default.is_scalar:
                setattr(self, column.name, column.default.arg)

class User(ItemBase):
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

class Product(ItemBase):
    ''' Item for sale.'''
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('product.id'))
    # Barcode for the particular product
    upc = Column(String, default="")
    # Human readable name
    name = Column(String, default="")
    # How much this product is worth to customers. AKA suggested donation amount
    cost = Column(Float, default=0.00)
    # How many do we have in stock
    qty = Column(Integer, default=1)
    # Products can contain other products like a 24 can box of softy drinkums
    contains = relationship("Product", remote_side=[id])
    # How man child prodcts does this have?
    contains_qty = Column(Integer, default=1)

class Purchase(ItemBase):
    ''' Keeps track of who bought what '''
    __tablename__ = 'purchase'

    # Some unique indentifier doodle
    id = Column(Integer, primary_key=True)
    # How many items did they buy
    qty = Column(Integer)
    # Cost. Because we're a donation after all
    cost = Column(Float, default=1.00)
    # What was the thing?
    product = Column(Integer, ForeignKey('product.id'))
    transaction = Column(Integer, ForeignKey('transaction.id'))

class Transaction(ItemBase):
    ''' A collection of purchases to dedup some data '''
    __tablename__ = 'transaction'

    # Some unique indentifier
    id = Column(Integer, primary_key=True)
    # When did the transaction happen
    date = Column(DateTime)
    # Who bought the things
    user = Column(Integer, ForeignKey('user.id'))
