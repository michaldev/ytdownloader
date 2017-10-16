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

        self.right_vbox = Gtk.VBox()
        self.right_vbox.set_size_request(600, 400)
        self.formats_hbox = Gtk.HBox()

        self.download_audio_button = Gtk.Button("Download audio")
        self.audio_vbox = Gtk.VBox()
        self.audio_store = Gtk.ListStore(str)
        self.audio_combobox = Gtk.ComboBox.new_with_model(self.audio_store)
        self.audio_combobox.set_active(0)
        renderer_text = Gtk.CellRendererText()
        self.audio_combobox.pack_start(renderer_text, True)
        self.audio_combobox.add_attribute(renderer_text, "text", 0)
        self.audio_vbox.pack_start(self.audio_combobox, False, False, 10)
        self.audio_vbox.pack_start(self.download_audio_button, False, False, 10)

        self.download_video_button = Gtk.Button("Download video")
        self.video_store = Gtk.ListStore(str)
        self.video_combobox = Gtk.ComboBox.new_with_model(self.video_store)
        self.video_combobox.set_active(0)
        renderer_text = Gtk.CellRendererText()
        self.video_combobox.pack_start(renderer_text, True)
        self.video_combobox.add_attribute(renderer_text, "text", 0)
        self.video_vbox = Gtk.VBox()
        self.video_vbox.pack_start(self.video_combobox, False, False, 10)
        self.video_vbox.pack_start(self.download_video_button, False, False, 10)

        self.formats_hbox.pack_start(self.audio_vbox, True, False, 10)
        self.formats_hbox.pack_start(self.video_vbox, True, False, 10)

        self.right_vbox.pack_start(self.formats_hbox, False, False, 10)
        self.pack_start(self.right_vbox, True, True, 5)
        self.show_all()

