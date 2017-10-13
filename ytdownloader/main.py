#!/usr/bin/python3
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite
import window as wn

class Application(Granite.Application):

    def do_activate(self):
        win = wn.Window()
        win.set_default_size(600, 600) 
        win.connect("delete-event", Gtk.main_quit)
        win.show_all()
        Gtk.main()
        

app = Application()

stylesheet = """
    @define-color colorPrimary #FF0000;
    @define-color textColorPrimary #EEEDEC;
    @define-color textColorPrimaryShadow #53433F;
""";

style_provider = Gtk.CssProvider()
style_provider.load_from_data(bytes(stylesheet.encode()))
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(), style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

app.run("", 1)
