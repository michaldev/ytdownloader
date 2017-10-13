#!/usr/bin/python3
import os
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite

from dialog import LightWindow


class Welcome(Gtk.Box):
        
    # Define variable for GTK global theme
    settings = Gtk.Settings.get_default()

    def __init__(self):
        Gtk.Box.__init__(self, False, 0)

        self.settings.set_property("gtk-application-prefer-dark-theme", True)

        # Create welcome widget
        welcome = Granite.WidgetsWelcome()
        welcome = welcome.new("Welcome", "What do you want to do?")

        # Welcome voices
        welcome.append("folder-videos", "Open", "Open Video or Playlist")

        welcome.connect("activated", self.on_welcome_activated)

        self.add(welcome)

    def on_welcome_activated(self, widget, index):
        if index == 0:
            light = LightWindow(title="abc")
            light.show()
            
