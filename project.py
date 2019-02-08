import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
#from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout

class Todo(BoxLayout):
	pass



	# def show(self, tasktodo):
		
	#     #self.add_widget(str(tasktodo))
	#     self.add_widget("\n ")
	
		


class TodoApp(App):
	def build(self):
		return Todo()


TodoApp().run()