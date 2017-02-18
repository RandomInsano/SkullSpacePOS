'''
    There's the UI tests to find something good
'''

import urwid

def grid_view(data):
    pass

COL_WIDTH_ID = 4
COL_WIDTH_NAME = 32
COL_WIDTH_COST = 5
COL_WIDTH_QTY = 3
COL_WIDTH_BARCODE = 15

"ID", "Name", "Cost ", "Qty", "Barcode"

headers = [
    (COL_WIDTH_ID, urwid.Text("ID")),
    (COL_WIDTH_NAME, urwid.Text("Name")),
    (COL_WIDTH_COST, urwid.Text("Cost")),
    (COL_WIDTH_QTY, urwid.Text("Qty")),
    (COL_WIDTH_BARCODE, urwid.Text("Barcode")),
]

items = []
items.append(urwid.Columns(headers, dividechars=1))

list_box = urwid.ListBox(urwid.SimpleListWalker(items))

#fill = urwid.Filler(list_box, 'top')

loop = urwid.MainLoop(list_box)
loop.run()
