#!/usr/bin/python3
import gi
import webbrowser
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Headerbar(Gtk.HeaderBar):

    def __init__(self):

        Gtk.HeaderBar.__init__(self)

        self.set_show_close_button(True)
        self.props.title = "YT Downloader"

        self.hbar_download = Gtk.ToolButton()
        self.hbar_download.set_icon_name("folder-download")
        self.pack_end(self.hbar_download)

