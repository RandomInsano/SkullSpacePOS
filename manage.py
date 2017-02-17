#!/usr/bin/env python3
'''
    This will act as a staging area for working with the data and grow outward
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base, User, Product, Purchase

engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)

def main():
    Base.metadata.create_all(engine)

    conn = Session()

    print("Products:")
    for product in conn.query(Product):
        print("{0:3} | {1:32} | ${2:,.2f}".format(product.id, product.name, product.cost))

main()
