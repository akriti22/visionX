import kivy
#kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.button import Button


class HelloKivy(App):

    def build(self):
        return Button(text = "Hello Kivy", background_color = (0,0,1,1),
        	font_size=150)

helloKivy = HelloKivy()

helloKivy.run()
