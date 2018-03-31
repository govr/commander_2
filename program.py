#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
import psutil

kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.lang import Builder

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '300')
Config.set('graphics', 'fullscreen', '0')

#Builder.load_file('myapp.kv')

class LoginScreen (GridLayout):
    def __init__(self, **kwargs):
        kwargs['cols'] = 2
        super(LoginScreen, self).__init__(**kwargs)

        button = Button(text='My first button')
        self.add_widget(button)

    def click(self):
        button = Button(text='My first button')
        self.add_widget(button)

        self.BoxLayout.add_widget(button)
    def build(self):

        dps = psutil.disk_partitions()
        print(dps)
        fmt_str = "{:<8} {:<7} {:<7}"
        print(fmt_str.format("Drive", "Type", "Opts"))
        # Only show a couple of different types of devices, for brevity.
        for dp in dps:
            print(fmt_str.format(dp.device, dp.fstype, dp.opts))

class MyApp(App):
    def build(self):
        return LoginScreen()

MyApp().run()