#!/usr/bin/python3
import gi
from datetime import datetime
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import headerbar as hb
import welcome as wl

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="YT Downloader")

        hbar = hb.Headerbar()
        self.set_titlebar(hbar)

        self.welcome = wl.Welcome()

        self.add(self.welcome)

