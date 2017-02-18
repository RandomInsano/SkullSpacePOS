import urwid

COL_WIDTH_ID = 4
COL_WIDTH_NAME = 32
COL_WIDTH_COST = 5
COL_WIDTH_QTY = 3
COL_WIDTH_BARCODE = 15
COL_WIDTH_EDITBUTTON = 10
COL_DIVIDER_WIDTH = 2

class ProductEditor(urwid.Pile):
    def __init__(self):
        self.row = None

        self._id = urwid.Text("ID:        ")
        self._name = urwid.Edit("Name:     ")
        self._cost = urwid.Edit("Cost:     ")
        self._qty = urwid.IntEdit("Quantity: ")
        self._barcode = urwid.Edit("Barcode:  ")
        self._save_button = urwid.Button("save")

        controls = [
            self._id,
            self._name,
            self._cost,
            self._qty,
            self._barcode,
            self._save_button,
        ]

        super(ProductEditor, self).__init__(controls)

    def _commit(self):
        product = self._row._product

        product.name = self._name.edit_text
        product.cost = float(self._cost.edit_text)
        product.qty = int(self._qty.edit_text)
        product.upc = self._barcode.edit_text
        self._row.update()

    def set(self, row):
        self._row = row
        product = row._product

        def on_save_click(button):
            self._commit()

        urwid.connect_signal(self._save_button, 'click', on_save_click)

        self._id.set_text("ID:{0:8}".format(product.id))
        self._name.edit_text = product.name
        self._cost.edit_text = str(product.cost)
        self._qty.edit_text = str(product.qty)
        self._barcode.edit_text = product.upc

class ProductRow(urwid.Columns):
    def __init__(self, product, editor):
        self._product = product
        self._editor = editor

        self._id = urwid.Text("")
        self._name = urwid.Text("")
        self._cost = urwid.Text("")
        self._qty = urwid.Text("")
        self._upc = urwid.Text("")

        edit_button = urwid.Button("edit")

        def on_edit_click(button):
            self._editor.set(self)

        urwid.connect_signal(edit_button, 'click', on_edit_click)

        values = [
            (COL_WIDTH_ID, self._id),
            (COL_WIDTH_NAME, self._name),
            (COL_WIDTH_COST, self._cost),
            (COL_WIDTH_QTY, self._qty),
            (COL_WIDTH_BARCODE, self._upc),
            (COL_WIDTH_EDITBUTTON, edit_button)
        ]

        self.update()

        super(ProductRow, self).__init__(values, dividechars=COL_DIVIDER_WIDTH)

    def update(self):
        product = self._product

        self._id.set_text(str(product.id))
        self._name.set_text(product.name)
        self._cost.set_text("${0:3,.2f}".format(product.cost))
        self._qty.set_text(str(product.qty))
        self._upc.set_text(product.upc)

class ProductTable(urwid.ListBox):
    def __init__(self, products, editor):
        self._editor = editor
        self._items = []

        headers = [
            (COL_WIDTH_ID, urwid.Text("ID")),
            (COL_WIDTH_NAME, urwid.Text("Name")),
            (COL_WIDTH_COST, urwid.Text("Cost")),
            (COL_WIDTH_QTY, urwid.Text("Qty")),
            (COL_WIDTH_BARCODE, urwid.Text("Barcode")),
        ]

        # Headers here
        self._items.append(urwid.Columns(headers, dividechars=COL_DIVIDER_WIDTH))

        # New item button
        new_button = urwid.Button("new")
        temp_column = urwid.Columns([(7, new_button)])
        self._items.append(temp_column)

        for product in products:
            self.add_item(product)

        super(ProductTable, self).__init__(urwid.SimpleListWalker(self._items))

    def add_item(self, product):
        row = ProductRow(product, self._editor)

        self._items.insert(-1, row)
