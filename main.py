from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from app.Components.FileManagerButton import DisplayerImage

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(*kwargs)
        Window.size = (300, 500)

    def build(self):

        # Crete the screen manager
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
        layout.add_widget(MDLabel(text="Hello world", halign="center"))

        display = DisplayerImage()
        layout.add_widget(display)

        return layout

if __name__ == '__main__':
    MainApp().run()