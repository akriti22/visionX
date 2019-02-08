from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

class TaskListButton(ListItemButton):
	pass


   
class TaskDB(BoxLayout):
	task_input: ObjectProperty()
	task_list: ObjectProperty()

	def submit_task(self):

		taskname = self.task_input.text 
		self.task_list.adapter.data.extend([taskname])
		self.task_list._trigger_reset_populate()

	def delete_task(self, *args):
		if self.task_list.adapter.selection:
			selection = self.task_list.adapter.selection[0].text
			self.task_list.adapter.data.remove(selection)
			self.task_list._trigger_reset_populate()

	
	def replace_task(self, *args):
		if self.task_list.adapter.selection:
			selection = self.task_list.adapter.selection[0].text
			self.task_list.adapter.data.remove(selection)
			taskname = self.task_input.text
			self.task_list.adapter.data.extend([taskname])
        	
        	
        	

class TaskDBApp(App):

	def build(self):
		return TaskDB()

TaskDBApp().run()




