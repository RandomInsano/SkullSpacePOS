#!/usr/bin/env python3
'''
    This will act as a staging area for working with the data and grow outward
'''

import urwid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base, User, Product, Purchase

from ui import ProductTable, ProductEditor

engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)

def main():
    Base.metadata.create_all(engine)

    conn = Session()

    editor = ProductEditor()
    table = ProductTable(conn.query(Product), editor)

    header = urwid.Text("Product Editor")
    body = urwid.Pile([
        urwid.LineBox(table),
        (10, urwid.LineBox(urwid.Filler(editor, 'top'))),
    ])
    document = urwid.Frame(body, header)

    loop = urwid.MainLoop(document)
    loop.run()

main()
