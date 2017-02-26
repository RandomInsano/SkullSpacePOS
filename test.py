#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base, User, Product, Purchase, ContainsProduct, Transaction

from ui import ProductTable, ProductRow, ProductEditor

engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)

def main():
    Base.metadata.create_all(engine)

    conn = Session()

    products = conn.query(Product)
    for product in products:
        print("Product: {0}".format(product.name))
        if len(product.children) > 0:
            for contains in product.children:
                print("\t{1}x {0}".format(contains.child.name, contains.qty))

main()
