from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout 
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import MDRectangleFlatButton
import tempfile
from PIL import Image as ImagePIL
from kivy.uix.button import Button
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.image import Image
from matplotlib.pyplot import text
from numpy import source

from app.Components.ButtonManager import FileManagerButton
from app.Components.FileManagerButton import DisplayerImage

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(*kwargs)
        Window.size = (300, 500)

    def build(self):

        # Crete the screen manager
        layout = BoxLayout(orientation="vertical")
        # Create The toolabar
        toolbar = MDTopAppBar(title='Welcome',
                            left_action_items=[["menu", lambda x: x]],
                            right_action_items=[["dots-vertical", lambda x: x]],
                            elevation=10,
                            md_bg_color=(0, 0, 0, 1),
                            )
        layout.add_widget(toolbar)
        layout.add_widget(MDLabel(text="Hello world", halign="center"))
        # self.path_image = None
        # self.image = Image(source='app/imgs/file_manager.jpg', size_hint=(1, 1), pos_hint={'center_x': .5, 'center_y': .5})
        # layout.add_widget(self.image)
        # button = FileManagerButton(text="Open image",source="app/imgs/file_manager.jpg")
        # layout.add_widget(button)
        display = DisplayerImage()
        layout.add_widget(display)
        # self.path_image = None
        label = MDLabel(text="Hello world", halign="center")
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    MainApp().run()