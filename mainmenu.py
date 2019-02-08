from kivy import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import NavigationDrawer


class Drawer(NavigationDrawer):
	theme_cls = ThemeManager()

class MainMenuApp(App):

	def shaw_drawer(self):
		d = Drawer()
		d.toggle_state()


	def build(self):
		return Drawer()

if __name__ == '__main__':
	MainMenuApp().run()