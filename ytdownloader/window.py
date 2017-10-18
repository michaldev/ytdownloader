#!/usr/bin/python3
import gi
import pafy
import requests
import threading

from datetime import datetime
from gi.repository import Gtk, Gdk, Gio, GdkPixbuf, GLib

gi.require_version('Gtk', '3.0')

import headerbar as hb
import welcome as wl
from downloads import Downloads
from video import Video


class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="YT Downloader")
        self.current = None

        self.download_screen = Downloads()

        self.hbar = hb.Headerbar()
        self.hbar.hbar_download.connect("clicked", self.open_download_screen)

        self.set_titlebar(self.hbar)
        
        self.video_window = Video()
        self.video_window.download_video_button.connect("clicked", self.add_to_download_section)

        self.welcome = wl.Welcome()
        self.open_popup = self.welcome.light
        self.open_popup.get_button.connect("clicked", self.open_click)

        self.add(self.welcome)

    def open_download_screen(self, widget=None):
        if self.get_child() == self.download_screen:
            self.remove(self.get_child())
            self.add(self.current)
            self.hbar.hbar_download.set_icon_name("folder-download")
        else:
            self.current = self.get_child()
            self.remove(self.get_child())
            self.add(self.download_screen)
            self.hbar.hbar_download.set_icon_name("edit-undo")

    def open_click(self, widget):
        self.address = self.open_popup.address_input.get_text()
        self.type = self.open_popup.combobox.get_active()

        self.open_popup.vbox.hide()
        self.progressbar = Gtk.Spinner()

        self.progressbar.show()
        self.open_popup.vbox.pack_start(self.progressbar, True, True, 10)
        self.open_popup.vbox.show()
        self.progressbar.start()

        self.get_video()

    def mycb(self, total, recvd, ratio, rate, eta):
        self.download_progressbar.set_fraction(ratio)

    def download_video(self):
        self.video_window.video.videostreams[self.video_window.video_combobox.get_active()].download(quiet=True, callback=self.mycb)

    def add_to_download_section(self, widget):
        self.download_hbox = Gtk.HBox()

        self.image = Gtk.Image()
        
        self.download_label = Gtk.Label(self.video_window.video.title)
        self.download_progressbar = Gtk.ProgressBar()

        response=requests.get(self.video_window.video.thumb)
        input_stream = Gio.MemoryInputStream.new_from_bytes(GLib.Bytes.new(response.content))             
        pixbuf = GdkPixbuf.Pixbuf.new_from_stream(input_stream, None) 
        self.image.set_from_pixbuf(pixbuf)

        self.download_hbox.pack_start(self.image, False, False, 5)
        self.download_vbox = Gtk.VBox()
        self.download_vbox.pack_start(self.download_label, False, False, 5)
        self.download_vbox.pack_start(self.download_progressbar, False, False, 5)

        self.download_hbox.pack_start(self.download_vbox, False, False, 5)

        self.download_screen.pack_start(self.download_hbox, False, False, 5)
        self.download_screen.show_all()

        self.open_download_screen()

        self.work_thread = threading.Thread(target=self.download_video)
        self.work_thread.start()

    def get_video(self):
        if self.type == 0:
            video = pafy.new(self.address)
      
            self.remove(self.get_child())
            self.open_popup.hide()

            self.video_window.video = video
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


        
