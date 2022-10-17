from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from app.Components.ButtonManager import FileManagerButton
from kivymd.uix.filemanager import MDFileManager
import os
import tempfile

class DisplayerImage(BoxLayout):
    def __init__(self, **kwargs):
        super(DisplayerImage, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10
        # initialize the file browser instance
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )

        # Create the image source
        self.image = Image(source='app/imgs/file_manager.jpg', size_hint=(1, 1), pos_hint={'center_x': .5, 'center_y': .5})
        # Add the image to the layout
        self.add_widget(self.image)
        # Create the button manager
        self.button = FileManagerButton(text="Open image",)

        self.button.on_release = self.open_file_manager
        self.button.icon = 'folder'
        self.button.background_color = (243/255, 148/255, 48/255, 255/255)
        self.button.background_normal = ''
        self.button.pos_hint = {'center_x': .5, 'center_y': .5}
        # Add the button to the center of the screen
        self.add_widget(self.button, )    
        
    def open_file_manager(self):
        self.file_manager.show(os.getcwd())

    def select_path(self, path):
        print(path)
        self.path_image = path
        self.exit_manager()

    def exit_manager(self, *args):
        self.file_manager.close()
        self.image.source = self.path_image
        
    # TODO:
    # Implement Tempfile