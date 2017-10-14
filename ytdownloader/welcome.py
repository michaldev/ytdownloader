#!/usr/bin/python3
import os
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite

from open import LightWindow


class Welcome(Gtk.Box):
        
    # Define variable for GTK global theme
    settings = Gtk.Settings.get_default()

    def __init__(self):
        Gtk.Box.__init__(self, False, 0)
        self.light = LightWindow()

        self.settings.set_property("gtk-application-prefer-dark-theme", True)

        # Create welcome widget
        self.welcome = Granite.WidgetsWelcome()
        self.welcome = self.welcome.new("Welcome", "What do you want to do?")

        # Welcome voices
        self.welcome.append("folder-videos", "Open", "Open Video or Playlist")

        self.welcome.connect("activated", self.on_welcome_activated)

        self.add(self.welcome)

    def on_welcome_activated(self, widget, index):
        if index == 0:
            self.light.run()
            
