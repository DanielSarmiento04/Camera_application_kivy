from turtle import bgcolor
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout 
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.toolbar import MDTopAppBar


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (300, 500)

    def build(self):
        # Create the screen manager
        layout = BoxLayout(orientation='vertical')
        # Create The toolabar
        toolbar = MDTopAppBar(title='Camera controller',
                            left_action_items=[["menu", lambda x: x]],
                            right_action_items=[["dots-vertical", lambda x: x]],
                            elevation=10,
                            md_bg_color=(0, 0, 0, 1),
                            
                              )

                              

        layout.add_widget(toolbar)

        layout.add_widget(MDLabel(text="Hello World", halign="center"))
        return layout

  

   

if __name__ == '__main__':
    MainApp().run()
