from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from kivy.uix.button import Button

default_path_image = "app/imgs/event_camera.jpeg"

class LiveCamera(BoxLayout):
    """
        LiveCamera
        ==========
        This is a class that allows you to display the camera x1on the screen.
        Take a photo and save it to the device.

    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Configure the Boc Layout
        self.spacing = 10
        self.orientation = "vertical"
        # Create a camera object
        self.camera = Camera(play=False, resolution=(720, 480))
        self.camera.source = default_path_image
        self.add_widget(self.camera)
        
        # Create a button to open the camere
        self.button_open_close_camera = Button(text='OpenCamera', )
        self.button_open_close_camera.bind(on_press=self.open_camera)
        self.add_widget(self.button_open_close_camera)
    
    def open_camera(self, *args):
        # Event open camera
        if self.camera.play:
            self.camera.play = False
            self.button_open_close_camera.text = "Open Camera"
            self.camera.source = default_path_image
        else:
            self.camera.play = True
            self.button_open_close_camera.text = "Close Camera"
