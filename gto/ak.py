from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class GameScreen(Screen):
    def __init__(self, **args):
        Screen.__init__(self, **args)
        self.money = 0
        self.label = Label(text=str(self.money), color=(1,0,0,1), font_size=(45),size_hint=(0.2,0.1), pos_hint={"center_x":0.5, "center_y":0.9})
        self.add_widget(self.label)

    def add_money(self):
        self.money += 1
        self.label.text = str(self.money)

Builder.load_string('''
<GameScreen>:
    name: "GameScreen"
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Button:
        size: self.texture_size
        on_release: root.add_money()
        text: "Press"
        font_size: 50
        color: 1,1,1,1
        background_color: (0,0,0,1)
        background_normal: ""
        background_down: ""
        size_hint: None, None
        pos_hint: {"center_x":0.5, "center_y":0.6}
        width: self.texture_size[0] + dp(10)
        height: self.texture_size[1] + dp(10)
    ''')

class TestApp(App):
    def build(self):
        return GameScreen()

if __name__ == '__main__':
    TestApp().run()