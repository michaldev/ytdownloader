#!/usr/bin/python3
import os
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite


class Video(Gtk.HBox):
        
    # Define variable for GTK global theme
    settings = Gtk.Settings.get_default()

    def __init__(self):
        Gtk.Box.__init__(self, False, 0)
        self.vbox = Gtk.VBox()
        self.image = Gtk.Image()
        self.video_title = Gtk.Label("Video Title")
        self.video_title.set_line_wrap(True)
        self.video_description = Gtk.Label("Video description")
        self.video_description.set_line_wrap(True)
        self.vbox.pack_start(self.video_title, False, False, 10)
        self.vbox.pack_start(self.image, False, False, 10)
        self.vbox.pack_start(self.video_description, False, False, 20)
        self.pack_start(self.vbox, False, False, 5)

        self.options_vbox = Gtk.VBox()
        self.options_vbox.set_size_request(600, 400)
        self.download_button = Gtk.Button("Download")
        self.options_vbox.pack_start(self.download_button, False, False, 10)
        self.pack_start(self.options_vbox, False, False, 5)
        self.show_all()

            
