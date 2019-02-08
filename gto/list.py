from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ListProperty
from kivy.uix.listview import ListItemButton


class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    def add_genre(self, lang):
        app = App.get_running_app()
        app.MY_LANG = lang

class ScreenThree(Screen):
    def add_genre(self, *argv):
        app = App.get_running_app()
        for n in argv:
            app.MY_DATA.append(n)

class ScreenFour(Screen):
    def add_genre(self, gen):
        app = App.get_running_app()
        app.MY_DATA.append(gen)

class ScreenFive(Screen):
    def press_readLang(self):
        app = App.get_running_app()
        self.ids.lbl1.text = "SharedVar is " + app.MY_LANG

    def press_read(self):
        app = App.get_running_app()
        self.ids.lbl1.text = "SharedVar is " + ', '.join(app.MY_DATA)

class ScreenSix(Screen):
    pass

class ScreenSeven(Screen):
    pass

class ImageButton(ButtonBehavior, Image, BoxLayout):
    pass



class Filmy(ScreenManager):
    screen_one = ObjectProperty(None) # You don't need those ObjectProperty variables
    screen_two = ObjectProperty(None) # so you can delete all those
    screen_three = ObjectProperty(None)
    screen_four = ObjectProperty(None)
    screen_five = ObjectProperty(None)

    choices = {}

    @staticmethod
    def addChoice(key, value):
        choices[key] = value

class FilmyApp(App):
    MY_DATA = []
    MY_LANG = ''
    MY_DATE = ''

    def build(self):
        return Filmy()



filmy = FilmyApp()
filmy.run()