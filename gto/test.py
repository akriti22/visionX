import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class kivyentrywidget(BoxLayout):
    orientation= "vertical"

    def __init__(self, **kwargs):
        super(kivyentrywidget, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='What do you want to print?'))
        self.text_input = TextInput(multiline=False)
        self.add_widget(self.text_input)

        self.printbutton1 = Button(text='Print')
        self.printbutton1.bind(on_press=self.callback)
        #self.printbutton2 = Button(text='Delete')
        #self.printbutton2.bind(on_press=self.call)
       

        self.add_widget(self.printbutton1)
        #self.add_widget(self.printbutton2)


        
        

    def callback(self, evt=None): 
        return self.add_widget(Label(text=self.text_input.text))
    # def call(self, evt=None):
    #     return self.add_widget(textinput(text=self.text_input.text))



class Firstapp(App):
    def build(self):
        return kivyentrywidget()

if __name__ == '__main__':
    Firstapp().run()