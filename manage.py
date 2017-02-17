#!/usr/bin/env python3
'''
    This will act as a staging area for working with the data and grow outward
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base, User, Product, Purchase

engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)

def print_products(conn):
    print("Products:")
    print("{0:3} | {1:32} | {2:4} | {3:2} | {4}".format("ID", "Name", "Cost ", "Qty", "Barcode"))
    print("-" * 70)
    for product in conn.query(Product):
        print("{0:3} | {1:32} | ${2:3,.2f} | {3:3} | {4}".format(product.id, product.name, product.cost, product.qty, product.upc))
    print()

def main():
    Base.metadata.create_all(engine)

    conn = Session()

    print_products(conn)

    p = Product()
    p.name = input('Product ("n" to commit and exit): ')
    while(p.name.lower() != 'n'):
        p.upc = input("UPC:      ")
        p.cost = float(input("Cost:     "))
        p.qty = int(input("Quantity: "))
        conn.add(p)

        print()
        print("Added. Will commit on exit")
        print()

        print_products(conn)
        p = Product()
        p.name = input('Product ("n" to quit): ')

    conn.commit()

main()
