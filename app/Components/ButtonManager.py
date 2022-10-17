from kivymd.uix.filemanager import MDFileManager
import os
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.image import Image


@staticmethod
class FileManagerButton(MDRectangleFlatButton):
    """ This class represents a file manager button """
    def __init__(self, **kwargs):
        # Initialize the button
        super().__init__(**kwargs)
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )
        
        self.background_normal = ''
        self.background_color = (243/255, 148/255, 48/255, 255/255)
        self.pos_hint = {'center_x': .5, 'center_y': .5}

        self.icon = 'folder'
        self.on_release = self.open_file_manager

    def open_file_manager(self):
        self.file_manager.show(os.getcwd())

    def select_path(self, path):
        print(path)
        self.path_image = path
        self.exit_manager()
    def exit_manager(self, *args):
        self.file_manager.close()
        
