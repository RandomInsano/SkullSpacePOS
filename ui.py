'''
    There's the UI tests to find something good
'''

import urwid


COL_WIDTH_ID = 4
COL_WIDTH_NAME = 32
COL_WIDTH_COST = 5
COL_WIDTH_QTY = 3
COL_WIDTH_BARCODE = 15
COL_DIVIDER_WIDTH = 2


class ProductTable(urwid.ListBox):
    _items = []

    def __init__(self, products):

        headers = [
            (COL_WIDTH_ID, urwid.Text("ID")),
            (COL_WIDTH_NAME, urwid.Text("Name")),
            (COL_WIDTH_COST, urwid.Text("Cost")),
            (COL_WIDTH_QTY, urwid.Text("Qty")),
            (COL_WIDTH_BARCODE, urwid.Text("Barcode")),
        ]

        self._items.append(urwid.Columns(headers, dividechars=COL_DIVIDER_WIDTH))

        for product in products:
            self.add_item(product)

        super(ProductTable, self).__init__(urwid.SimpleListWalker(self._items))

    def add_item(self, product):
        values = [
            (COL_WIDTH_ID, urwid.Text(str(product.id))),
            (COL_WIDTH_NAME, urwid.Text(product.name)),
            (COL_WIDTH_COST, urwid.Text("${0:3,.2f}".format(product.cost))),
            (COL_WIDTH_QTY, urwid.Text(str(product.qty))),
            (COL_WIDTH_BARCODE, urwid.Text(product.upc)),
        ]

        self._items.append(urwid.Columns(values, dividechars=COL_DIVIDER_WIDTH))
