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

    def focus_editor():
        ''' Focus cursor on the editor '''
        body.focus_position = 1

    def focus_list():
        ''' Focus cursor on the list of products '''
        body.focus_position = 0

    def new_product():
        if editor._product is not None and editor._product.id is None:
            return

        product = Product()
        product.ensure_defaults()
        editor.set(product)

    def key_input(key):
        if key in ['ctrl n']:
            new_product()
            focus_editor()

    def list_edit_click(product):
        editor.set(product)
        focus_editor()

    def new_product_click(button):
        new_product()
        focus_editor()

    def commit_editor_click(button):
        editor.commit()
        conn.add(product)
        conn.commit()
        editor.refresh()
        table.update()

        focus_list()

    def delete_editor_click(button):
        table.remove_item(editor._product)
        conn.delete(editor._product)
        conn.commit()
        new_product()

    # Open to suggestions on how ugly this is...
    urwid.connect_signal(editor._save_button, 'click', commit_editor_click)
    urwid.connect_signal(editor._new_button, 'click', new_product_click)
    urwid.connect_signal(editor._delete_button, 'click', delete_editor_click)

    # Fill product table
    for product in conn.query(Product):
        table.add_item(product, list_edit_click)

    loop = urwid.MainLoop(document, unhandled_input=key_input)

    # Set editor to have some product by default
    new_product()

    loop.run()

main()
