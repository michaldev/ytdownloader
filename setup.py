#!/usr/bin/python3

import glob, os 
from distutils.core import setup

install_data = [('share/applications', ['data/com.github.michaldev.ytdownloader.desktop']),
                ('share/metainfo', ['data/com.github.michaldev.ytdownloader.appdata.xml']),
                ('share/icons/hicolor/128x128/apps',['data/com.github.michaldev.ytdownloader.svg']),
                ('bin/elementarypython',['ytdownloader/headerbar.py']),
                ('bin/elementarypython',['ytdownloader/main.py']),
                ('bin/elementarypython',['ytdownloader/welcome.py']),
                ('bin/elementarypython',['ytdownloader/window.py']),
                ('bin/elementarypython',['ytdownloader/__init__.py'])]

setup(  name='YT Downloader',
        version='0.0.1',
        author='Michał Rosiak',
        description='Youtube Downloader for Elementary OS',
        url='https://github.com/michaldev/ytdownloader',
        license='GNU GPL3',
        scripts=['com.github.michaldev.ytdownloader'],
        packages=['ytdownloader'],
        data_files=install_data)
