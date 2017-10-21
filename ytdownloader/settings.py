import os
import json

from gi.repository import Gtk


home_directory = os.path.expanduser("~")
path = os.path.join(home_directory, ".ytdownloader.json")


class SettingsPopup(Gtk.Dialog):
    def __init__(self):
        super(SettingsPopup, self).__init__()

        self.path = None

        self.set_default_size(400, 200)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_size_request(400, 200)
        self.set_resizable(False)
        self.connect("destroy", self.close)

        self.location_label = Gtk.Label("Choose download location")
        self.file = Gtk.Button("Choose Folder")
        self.file.connect("clicked", self.on_folder_clicked)
        self.save_button = Gtk.Button("Save")
        self.save_button.connect("clicked", self.save)

        self.vbox.pack_start(self.location_label, False, False, 10)
        self.vbox.pack_start(self.file, False, False, 10)
        self.vbox.pack_start(self.save_button, False, False, 10)
        self.vbox.show_all()

    def load_config(self):
        if os.path.isfile(path):
            with open(path) as data_file:    
                self.data = json.load(data_file)
        return self.data

    def save_config(self, data):
        with open(path, 'w') as outfile:
            json.dump(data, outfile)

    def close(self, widget):
        print("TEST")
        widget.destroy()

    def save(self, widget):
        if self.path is not None:
            data = self.load_config()
            data['download_path'] = self.path
            self.save_config(data)
            self.destroy()

    def on_folder_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
            self.path = dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()
