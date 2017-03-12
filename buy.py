#!/usr/bin/env python3

import urwid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base, User, Product, Purchase

from ui import TextDialog

engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)

def key_input(key):
    if key in ['ctrl n']:
        new_product()
        focus_editor()

    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


def main():
    Base.metadata.create_all(engine)

    conn = Session()

#    for product in conn.query(Product):
#        table.add_item(product, list_edit_click)

    dialog = TextDialog('Scan Item', 'Scan an item to buy')
    product = []

    def get_product():
        upc = dialog.value()
        product = conn.query(Product).filter(Product.upc == upc).all()

    padding = urwid.Padding(dialog, 'center', 40)
    filler = urwid.Filler(padding, 'middle', 10)

    loop = urwid.MainLoop(filler, unhandled_input=key_input)
    loop.run()

    print(product[0].name)

main()
