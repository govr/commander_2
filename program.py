import kivy

import os

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.listview import ListItemButton, ListView
from kivy.adapters.listadapter import ListAdapter
import psutil

from kivy.uix.button import Button

class Folder(GridLayout):
    elements = 0
    folder = "c:\\"

    def __init__(self, **kwargs):
        kwargs['cols'] = 2
        super(Folder, self).__init__(**kwargs)

        self.show_list()

    def callback(self, obj):
        if obj.selection[0].text == '[..]':
            folder = ''

            i = 0
            for element in self.elements[0:-1]:
                if(i==0):
                    folder = folder + element
                else:
                    folder = folder + '/' + element
                i = i+1

            self.folder = folder

        else:
            self.folder = self.folder + '/' + obj.selection[0].text

        self.show_list()
    def changeDisk(self,obj):
        self.folder = obj.text
        self.show_list()

    def show_list(self):
        self.ids.folder_list.clear_widgets()
        self.ids.disk.clear_widgets()

        self.elements = self.folder.split("/")

        if len(self.elements)<=1:
            list = []
        else:
            list = ['[..]']

        list = list + os.listdir(self.folder)

        listA = ListAdapter(
            data=list,
            selection_mode='single',
            allow_empty_selection=False,
            cls=ListItemButton)

        lista = ListView(adapter=listA, size_hint=(.2, 1.0))

        listA.bind(on_selection_change=self.callback)

        dps = psutil.disk_partitions()
        for dp in dps:
            button = Button(text = dp.device)
            button.bind(on_press=self.changeDisk)

            self.ids.disk.add_widget(button)

        self.ids.folder_list.add_widget(lista)
class Program(App):
    title = 'Folder list'
    icon = 'icon.png'

    def build(self):
        return Folder()


Config.set('graphics', 'fullscreen', '0')

Program().run()