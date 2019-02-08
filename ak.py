from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class CaloriesScreen(Screen):
    pass

class categoriesScreen(Screen):
    pass

class loginScreen(Screen):
    pass

class registerScreen(Screen):
    pass

class shoppingListScreen(Screen):
    pass

class theScreenManager(ScreenManager):
    pass

root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition

theScreenManager:
    transition: FadeTransition()
    CaloriesScreen:

<CaloriesScreen>:
    name: 'calories'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: '<'
                font_size: 75
                background_normal: ""
                background_color: 0.18, .5, .92, 1
                size_hint: .1, .3
                on_release: app.root.current = 'main' 
                
            Label:
                text: 'Calories'
                size_hint: .9, .3
                font_size: 50
                canvas.before:
                    Color:
                        rgb: 0.18, .5, .92
                    Rectangle:
                        pos: self.pos
                        size: self.size
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'Recipes'
                font_size: 30
                color: 0.18, .5, .92, 1
                canvas.before:
                    Color:
                        rgb: 0.8, 0.8, 0.8
                    Rectangle:
                        pos: self.pos
                        size: self.size

            Button:
                id: btn
                text: 'Recipes'
                on_release: dropdown.open(self)
                size_hint_y: None
                height: '48dp'

            DropDown:

                id: dropdown
                on_parent: self.dismiss()
                on_select: btn.text = '{}'.format(args[1]) 

                Button:
                    text: 'First recipe'
                    size_hint_y: None
                    height: '48dp'
                    on_release: dropdown.select('First Item')

                Label:
                    text: 'Second recipe'
                    size_hint_y: None
                    height: '48dp'

                Button:
                    text: 'Third recipe'
                    size_hint_y: None
                    height: '48dp'
                    on_release: dropdown.select('Third Item')
            
         
''')

class RecipeApp(App):
    def build(self):
        return root_widget

if __name__ == "__main__":
    RecipeApp().run()