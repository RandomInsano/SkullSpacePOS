#!/usr/bin/env python3
'''
    This will act as a staging area for working with the data and grow outward
'''

import urwid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base, User, Product, Purchase

from ui import ProductTable, ProductRow, ProductEditor

engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)

def main():
    Base.metadata.create_all(engine)

    conn = Session()

    editor = ProductEditor()
    table = ProductTable()

    header = urwid.Text("Product Editor")
    body = urwid.Pile([
        urwid.LineBox(table),
        (8, urwid.LineBox(urwid.Filler(editor, 'top'))),
    ])
    document = urwid.Frame(body, header)

    def new_product():
        product = Product()
        product.ensure_defaults()
        conn.add(product)
        editor.set(product)

        # Go to editor
        body.focus_position = 1

    def key_input(key):
        if key in ['ctrl n']:
            new_product()

        if key in ['enter']:
            body.focus_position = 1

    def list_edit_click(product):
        editor.set(product)

    def new_product_click(button):
        new_product()

    def commit_editor_click(button):
        editor.commit()
        conn.commit()
        editor.refresh()
        table.update()

        # Go to product list
        body.focus_position = 0

    # Open to suggestions on how ugly this is...
    urwid.connect_signal(editor._save_button, 'click', commit_editor_click)
    urwid.connect_signal(editor._new_button, 'click', new_product_click)

    # Fill product table
    for product in conn.query(Product):
        table.add_item(product, list_edit_click)

    loop = urwid.MainLoop(document, unhandled_input=key_input)

    # Set editor to have some product by default
    new_product()

    loop.run()

main()
