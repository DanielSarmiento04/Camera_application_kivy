from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from  kivy.uix.image import Image
from kivy.clock import Clock
from kivymd.app import MDApp
import cv2
from functools import partial

path_image = "app/imgs/event_camera.jpeg"
class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(*kwargs)
        Window.size = (300, 500)

    def build(self):
        self.layout = MDBoxLayout(orientation="vertical")
        self.image = Image(source=path_image)
        
        self.layout.add_widget(self.image)
        self.button_open_close = MDRaisedButton(text="Open Camera", pos_hint={'center_x':0.5, "center_y": 0.5}, size_hint=(None, None))
        self.button_open_close.on_release = self.open_close_camera
        self.button_take_photo = MDRaisedButton(text="Take a photo", pos_hint={'center_x':0.5, "center_y": 0.5}, size_hint=(None, None))
        self.button_take_photo.on_release = self.capture_image
        
        self.button_take_photo.disabled = True
        self.layout.add_widget(self.button_take_photo)

        self.layout.add_widget(self.button_open_close)

        self.capture = None
        # Clock.schedule_interval(self.load_video, 1.0/30.0)
        return self.layout

    def open_close_camera(self, *args):        
        if self.button_open_close.text == "Open Camera":
            self.capture = cv2.VideoCapture(0)
            self.button_open_close.text = "Close Camera"
            print("Encender camara")
            Clock.schedule_interval(self.load_video, 1.0/30.0)
            self.button_take_photo.disabled = False
        else:
            print("Apagar camara")
            self.image.source = path_image
            Clock.unschedule(self.load_video)
            self.capture.release()
            self.image.reload()
            self.button_open_close.text = "Open Camera"
            self.button_take_photo.disabled = True

    def load_video(self, capture):
        
        ret, frame = self.capture.read()
        self.image_frame = frame
        buffer = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture
        pass

    def capture_image(self, *args):
        cv2.imwrite("app/imgs/test.png", self.image_frame)
        print("Take a photo")


if __name__ == '__main__':
    MainApp().run()