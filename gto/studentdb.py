from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
 
 
class CameraListButton(ListItemButton):
    pass
 
 
class CameraDB(BoxLayout):
 
    # Connects the value in the TextInput widget to these
    # fields
    text_input = ObjectProperty()
    
    student_list = ObjectProperty()
 
    def submit_camera(self):
 
        
        taskname = self.text_input.text
 
        # Add the student to the ListView
        self.camera_list.adapter.data.extend([taskname])
 
        # Reset the ListView
        self.cameralist._trigger_reset_populate()
 
    def delete_camera(self, *args):
 
        # If a list item is selected
        if self.camera_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.cameralist.adapter.selection[0].text
 
            # Remove the matching item
            self.camera_list.adapter.data.remove(selection)
 
            # Reset the ListView
            self.camera_list._trigger_reset_populate()
 
    def replace_camera(self, *args):
 
        # If a list item is selected
        if self.camera_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.camera_list.adapter.selection[0].text
 
            # Remove the matching item
            self.camera_list.adapter.data.remove(selection)
 
            # Get the student name from the TextInputs
            taskname = self.task_input.text
 
            # Add the updated data to the list
            self.camera_list.adapter.data.extend([taskname])
 
            # Reset the ListView
            self.camera_list._trigger_reset_populate()
 
 
class CameraDBApp(App):
    def build(self):
        return CameraDB()
 
 
dbApp = CameraDBApp()
 
dbApp.run()