from gi.repository import Gtk


class SettingsPopup(Gtk.Dialog):
    def __init__(self):
        super(SettingsPopup, self).__init__()
        self.set_default_size(400, 200)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_size_request(400, 200)
        self.set_resizable(False)
        self.connect("destroy", self.close)

        self.save_button = Gtk.Button("Save")

        self.vbox.pack_start(self.save_button, False, False, 10)
        self.vbox.show_all()

    def close(self, widget):
        print("TEST")
        widget.destroy()

