from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton, MDRoundFlatButton
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.gridlayout import GridLayout
from  kivy.uix.image import Image
import cv2

path_image = "app/imgs/event_camera.jpeg"

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
        self.minimum_width = 250        # Create a camera object
        self.image = Image(source=path_image, allow_stretch= True, texture_size= (200,300) )
        
        # Create the Button for take control to camaera event 
        self.add_widget(self.image,  )
        self.button_open_close = MDRaisedButton(text="Open Camera", pos_hint={'center_x':0.5, "center_y": 0.5}, size_hint=(None, None))
        self.button_open_close.on_release = self.open_close_camera

        self.add_widget(self.button_open_close)

        self.buttons_components = GridLayout(cols=2, spacing=10, rows=1, )

        # Create the Button for capture the actual frame
        self.button_take_photo = MDRaisedButton(text="Take a photo", )#pos_hint={'center_x':0.5, "center_y": 0.5}, size_hint=(None, None))
        self.button_take_photo.on_release = self.capture_image
        self.button_take_photo.disabled = True

        self.buttons_components.add_widget(self.button_take_photo)

        self.button_save_photo = MDRoundFlatButton(text="Save photo", )#pos_hint={'center_x':0.5, "center_y": 0.5}, size_hint=(None, None))
        self.button_save_photo.on_release = self.save_image
        self.button_save_photo.disabled = True

        self.buttons_components.add_widget(self.button_save_photo)

        self.add_widget(self.buttons_components, )

        self.image_frame = self.capture = None
        
        self.__clock__ = Clock


    def open_close_camera(self, *args):       
        """
            This method allows you to open and close the camera.        
        """ 

        if self.button_open_close.text == "Open Camera":
            self.open_camera()
        elif self.button_open_close.text == "Close Camera":
            print("Apagar camara")
            self.close_camera()


    def open_camera(self):
        """
            This method allow take the video from the First camera allowed.
        """
        self.capture = cv2.VideoCapture(0)
        self.button_open_close.text = "Close Camera"
        print("Encender camara")
        self.__clock__.schedule_interval(self.load_video, 1.0/30.0)
        self.button_take_photo.disabled = False

    def close_camera(self):
        """
            This method close the camera socket video
        """
        self.image.source = path_image
        self.__clock__.unschedule(self.load_video)
        self.capture.release()
        self.image.reload()
        self.button_open_close.text = "Open Camera"
        self.button_take_photo.disabled = True


    def load_video(self, *args):
        """
            This method load the camera video.
        """
        ret, frame = self.capture.read()
        self.image_frame = frame
        buffer = cv2.flip(frame, 0).tobytes()
    
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture
        pass

    def capture_image(self, *args):
        """
            This method Stop the live Streaming video capture from the camera.
        """
        self.__clock__.unschedule(self.load_video)
        if self.button_save_photo.disabled:
            self.button_save_photo.disabled = False
        
        else:
            self.button_save_photo.disabled = True
        print("Take a photo")
    
    def save_image(self, *args, **kwargs):
        """
            This method save the image
        """
        if self.image_frame is not None:
            cv2.imwrite("app/imgs/test.jpeg", self.image_frame)
            print("Save photo")

    def capture_video(self, *args):
        pass
