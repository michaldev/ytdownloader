from gi.repository import Gtk

class LightWindow(Gtk.Dialog):
    def __init__(self):
        super(LightWindow, self).__init__()
        self.set_default_size(400, 200)
        #self.set_title(title)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_size_request(400, 200)
        self.set_resizable(False)
        self.connect("destroy", self.close)
             
        type_store = Gtk.ListStore(str)
        type_store.append(["Video"])
        self.combobox = Gtk.ComboBox.new_with_model(type_store)
        self.combobox.set_active(0)

        renderer_text = Gtk.CellRendererText()
        self.combobox.pack_start(renderer_text, True)
        self.combobox.add_attribute(renderer_text, "text", 0)

        self.address_input = Gtk.Entry()

        combobox_label = Gtk.Label("Choose type")

        address_label = Gtk.Label("Entry address:")

        self.get_button = Gtk.Button("Get info")

        self.vbox.pack_start(combobox_label, False, False, 10)
        self.vbox.pack_start(self.combobox, False, False, 0)
        self.vbox.pack_start(address_label, False, False, 10)
        self.vbox.pack_start(self.address_input, False, False, 0)
        self.vbox.pack_start(self.get_button, False, False, 50)
        self.vbox.show_all()

    def close(self, widget):
        print("TEST")
        widget.destroy()




