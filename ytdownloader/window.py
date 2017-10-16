#!/usr/bin/python3
import gi
import pafy
import requests

from datetime import datetime
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio, GdkPixbuf, GLib
import headerbar as hb
import welcome as wl
from video import Video


class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="YT Downloader")

        hbar = hb.Headerbar()
        self.set_titlebar(hbar)

        self.welcome = wl.Welcome()
        self.light = self.welcome.light
        self.light.get_button.connect("clicked", self.open_click)
        self.add(self.welcome)

    def next_screen(self, widget):
        self.remove(self.welcome)

    def open_click(self, widget):
        self.address = self.light.address_input.get_text()
        self.type = self.light.combobox.get_active()

        if self.type == 0:
            try:
                video = pafy.new(self.address)
                self.remove(self.welcome)
                self.light.hide()
                self.video_window = Video()
                self.video_window.video_title.set_text(video.title)
                self.video_window.video_description_label.set_text(video.description)
                self.video_window.video_author_label.set_text(video.author)
                for obj in video.audiostreams:
                    self.video_window.audio_store.append([str(obj)])

                for obj in video.videostreams:
                    self.video_window.video_store.append([str(obj)])

                self.add(self.video_window)

                response=requests.get(video.bigthumb)
                input_stream = Gio.MemoryInputStream.new_from_bytes(GLib.Bytes.new(response.content))             
                pixbuf = GdkPixbuf.Pixbuf.new_from_stream(input_stream, None) 
                self.video_window.image.set_from_pixbuf(pixbuf)
            except:
         	    message = Gtk.MessageDialog(type=Gtk.MESSAGE_ERROR, buttons=Gtk.BUTTONS_OK)
         	    message.set_markup("An example error popup.")
         	    message.run()

        
