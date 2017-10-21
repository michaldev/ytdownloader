#!/usr/bin/python3
import gi
import pafy
import requests
import threading
import json
import os

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
        self.data = self.load_config()

        self.download_screen = Downloads()
        self.download_screen.open_folder_button.connect("clicked", self.open_folder)

        self.hbar = hb.Headerbar()
        self.hbar.hbar_download.connect("clicked", self.open_download_screen)
        self.hbar.hbar_settings.connect("clicked", self.open_settings_popup)

        self.set_titlebar(self.hbar)
        
        self.video_window = Video()
        self.video_window.download_video_button.connect("clicked", self.add_to_download_section, "video")
        self.video_window.download_audio_button.connect("clicked", self.add_to_download_section, "audio")       

        self.welcome = wl.Welcome()
        self.open_popup = self.welcome.light
        self.open_popup.get_button.connect("clicked", self.open_click)

        self.add(self.welcome)

    def open_folder(self, widget):
        os.system("pantheon-files "+self.data['download_path'])

    def load_config(self):
        home_directory = os.path.expanduser("~")
        path = os.path.join(home_directory, ".ytdownloader.json")

        if os.path.isfile(path):
            with open(path) as data_file:    
                self.data = json.load(data_file)
        else:
            temp_download_dir = os.path.join(home_directory, "ytdownloader")
            if os.path.isdir(temp_download_dir) is False:
                os.makedirs(temp_download_dir)
            self.data = {"download_path": temp_download_dir}
            with open(path, 'w') as outfile:
                json.dump(self.data, outfile)
        return self.data

    def open_settings_popup(self, widget):
        from settings import SettingsPopup
        settings_popup = SettingsPopup()
        settings_popup.show()

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
        #import threading
        #th = threading.Thread(target=self.get_video)
        #th.start()
        self.get_video()

    def mycb(self, total, recvd, ratio, rate, eta):
        self.download_progressbar.set_fraction(ratio)

    def download_video(self):
        if self.media_type == "video":
            self.video_window.video.videostreams[self.video_window.video_combobox.get_active()].download(filepath=self.data['download_path'], quiet=True, callback=self.mycb)
        elif self.media_type == "audio":
            self.video_window.video.audiostreams[self.video_window.audio_combobox.get_active()].download(filepath=self.data['download_path'], quiet=True, callback=self.mycb)

    def add_to_download_section(self, widget, media_type):
        self.media_type = media_type
        self.download_hbox = Gtk.HBox()
 
        if self.media_type == "audio":
            self.media_type_name = "Audio"
        elif self.media_type == "video":
            self.media_type_name = "Video"

        self.image = Gtk.Image()
        
        self.download_label = Gtk.Label(self.video_window.video.title+" | "+self.media_type_name)
        self.download_progressbar = Gtk.ProgressBar()

        response=requests.get(self.video_window.video.thumb)
        input_stream = Gio.MemoryInputStream.new_from_bytes(GLib.Bytes.new(response.content))             
        pixbuf = GdkPixbuf.Pixbuf.new_from_stream(input_stream, None) 
        self.image.set_from_pixbuf(pixbuf)

        self.download_hbox.pack_start(self.image, False, False, 5)
        self.download_vbox = Gtk.VBox()
        self.download_vbox.pack_start(self.download_label, False, False, 5)
        self.download_vbox.pack_start(self.download_progressbar, False, False, 5)

        self.download_hbox.pack_start(self.download_vbox, True, True, 10)

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


        
