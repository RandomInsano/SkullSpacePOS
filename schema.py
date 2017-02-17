from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    # Users will be identified by barcode / swipe card
    id = Column(String, primary_key=True)
    # Friendly name of the User
    name = Column(String)
    # Contact address
    email = Column(String)

class Product(Base):
    ''' Item for sale.'''
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('product.id'))
    name = Column(String)
    cost = Column(Float)
    # Products can contain other products like a 24 can box of softy drinkums
    contains = relationship("Product", remote_side=[id])
    # How man child prodcts does this have?
    contains_qty = Column(Integer)
    pass

class Purchase(Base):
    ''' Keeps track of who bought what '''
    __tablename__ = 'purchase'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    pass
