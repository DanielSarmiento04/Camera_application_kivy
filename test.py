from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout 
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import MDRectangleFlatButton
import cv2

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

        button = MDRectangleFlatButton(text='Open Camera', pos_hint={'center_x': 0.5, 'center_y': 0.4})
        button.on_release = self.open_camera
        layout.add_widget(button)
        return layout

    def open_camera(self):
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        print("Open Camera")

if __name__ == '__main__':
    MainApp().run()