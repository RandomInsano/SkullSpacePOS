import urwid

COL_WIDTH_ID = 4
COL_WIDTH_NAME = 32
COL_WIDTH_COST = 7
COL_WIDTH_QTY = 3
COL_WIDTH_BARCODE = 15
COL_WIDTH_EDITBUTTON = 10
COL_DIVIDER_WIDTH = 2

class ProductEditor(urwid.WidgetWrap):
    def __init__(self):
        self._product = None

        self._id = urwid.Text("ID:        ")
        self._name = urwid.Edit("Name:     ")
        self._cost = urwid.Edit("Cost:     ")
        self._qty = urwid.IntEdit("Quantity: ")
        self._barcode = urwid.Edit("Barcode:  ")
        self._save_button = urwid.Button("save")
        self._new_button = urwid.Button("new")
        self._delete_button = urwid.Button("delete")

        button_flow = urwid.GridFlow([
            self._save_button,
            self._new_button,
            self._delete_button
        ], 10, 1, 0, 'left')

        display_widget = urwid.Pile([
            self._id,
            self._name,
            self._barcode,
            self._cost,
            self._qty,
            button_flow
        ])

        urwid.WidgetWrap.__init__(self, display_widget)

    def commit(self):
        product = self._product

        product.name = self._name.edit_text
        product.cost = float(self._cost.edit_text)
        product.qty = int(self._qty.edit_text)
        product.upc = self._barcode.edit_text

    def refresh(self):
        if not hasattr(self, '_product'):
            return

        product = self._product

        self._id.set_text("ID:       {0}".format(product.id if product.id is not None else "[new]"))
        self._name.edit_text = product.name if product.name is not None else ""
        self._cost.edit_text = str(product.cost if product.cost is not None else "0.00?")
        self._qty.edit_text = str(product.qty if product.qty is not None else "1?")
        self._barcode.edit_text = product.upc if product.upc is not None else ""

    def set(self, product):
        self._product = product
        self.refresh()

    def get(self):
        return self._product


class ProductRow(urwid.Columns):
    def __init__(self, product, edit_event):
        self._product = product

        self._id = urwid.Text("")
        self._name = urwid.Text("")
        self._cost = urwid.Text("")
        self._qty = urwid.Text("")
        self._upc = urwid.Text("")

        edit_button = urwid.Button("edit")

        def on_edit_click(button):
            edit_event(self._product)

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

        urwid.Columns.__init__(self, widget_list=values, dividechars=COL_DIVIDER_WIDTH)

    def update(self):
        product = self._product

        self._id.set_text(str(product.id))
        self._name.set_text(product.name)
        self._cost.set_text("${0:3,.2f}".format(product.cost))
        self._qty.set_text(str(product.qty))
        self._upc.set_text(product.upc)

    def contains(self, product):
        return self._product is product

class ProductTable(urwid.WidgetWrap):
    def __init__(self):
        self._sizing = 'fixed'

        self._items = urwid.SimpleFocusListWalker([])

        display_widget = urwid.Frame(
            header=urwid.Text("ID    Name                              Cost   Qty  Barcode"),
            body=urwid.ListBox(self._items)
        )

        urwid.WidgetWrap.__init__(self, display_widget)

    def update(self):
        for product_row in self._items:
            if hasattr(product_row, 'update'):
                product_row.update()

    def remove_item(self, product):
        # Ugh... Linear search :'(
        for item in self._items:
            if item.contains(product):
                self._items.remove(item)

    def add_item(self, product, edit_event):
        row = ProductRow(product, edit_event)

        self._items.append(row)
