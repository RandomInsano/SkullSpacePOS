#!/usr/bin/env python3
'''
    This will act as a staging area for working with the data and grow outward
'''

import urwid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base, User, Product, Purchase

from ui import ProductTable

engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)

def main():
    Base.metadata.create_all(engine)

    conn = Session()

    table = ProductTable(conn.query(Product))

    loop = urwid.MainLoop(table)
    loop.run()

main()
