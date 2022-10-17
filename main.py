from turtle import bgcolor
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

import os

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (300, 500)
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )

    def build(self):
        # Create the screen manager
        layout = BoxLayout(orientation='vertical')
        # Create The toolabar
        toolbar = MDTopAppBar(title='Welcome',
                            left_action_items=[["menu", lambda x: x]],
                            right_action_items=[["dots-vertical", lambda x: x]],
                            elevation=10,
                            md_bg_color=(0, 0, 0, 1),
                              )
        layout.add_widget(toolbar)

        layout.add_widget(MDLabel(text="Hello world", halign="center"))
        layout.add_widget(MDRectangleFlatButton(text='Prender la camara', pos_hint={'center_x': 0.5, 'center_y': 0.4}))

        btn_select_file = Button(text='Seleccione una imagen',)
        # set size

        btn_select_file.size_hint = (0.5, 0.5)
        # set position
        btn_select_file.pos_hint = {'center_x': .5, 'center_y': .5}
        # put border radius
        btn_select_file.background_normal = ''
        btn_select_file.background_color = (0, 0, 0, 1)
        self.path_image = None
        self.image = Image(source='src/images.jpeg', size_hint=(1, 1), pos_hint={'center_x': .5, 'center_y': .5})
        btn_select_file.on_release = self.open_file_manager

        layout.add_widget(btn_select_file)
        return layout


    def open_file_manager(self):
        self.file_manager.show(os.getcwd())

    def select_path(self, path):
        print(path)
        self.path_image = path
        self.exit_manager()

    def exit_manager(self, *args):
        self.file_manager.close()
        # img = analize_image(self.path_image)
        img = ImagePIL.fromarray(img)
        # put the image in the layout
        with tempfile.NamedTemporaryFile(suffix='.png', prefix="image", delete=False, mode="w+b") as temp:
            img.save(temp.name)
            self.image.source = temp.name

        print('exit manager')


if __name__ == '__main__':
    MainApp().run()
