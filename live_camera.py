from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.window import Window
from kivymd.app import MDApp
from app.Components.LiveCamera import LiveCamera

class TestCamera(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (300, 500)

    def build(self):
        # Cr~ete the screen manager
        layout = BoxLayout(orientation="vertical")
        layout.spacing = 10
        # Create The toolabar
        toolbar = MDTopAppBar(title='Welcome',
                            left_action_items=[["menu", lambda x: x]],
                            right_action_items=[["dots-vertical", lambda x: x]],
                            elevation=10,
                            md_bg_color=(0, 0, 0, 1),
                            )
        layout.add_widget(toolbar)
        
        label = Label(text="Hello world")
        layout.add_widget(label)
        live_camera = LiveCamera()
        layout.add_widget(live_camera,)
        
        return layout
    def open_camera(self, *args):
        self.camera.play = True
        print("Open Camera")

TestCamera().run()