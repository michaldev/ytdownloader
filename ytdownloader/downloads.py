#!/usr/bin/python3
import os
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite


class Downloads(Gtk.VBox):
        
    # Define variable for GTK global theme
    settings = Gtk.Settings.get_default()

    def __init__(self):
        Gtk.Box.__init__(self, False, 0)
        
        self.open_folder_button = Gtk.Button("Open download folder")
        self.pack_end(self.open_folder_button, False, False, 0)
        

        

        
        

