
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.listview import ListItemButton
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
#from os.path import join, dirname
#from kivy.clock import Clock
#from kivy.uix.carousel import Carousel
 
 
class VisionListButton(ListItemButton):
    pass

 
 
class Vision(BoxLayout):
 
    
    text_input = ObjectProperty()
    
    camera_list = ObjectProperty()


    def navigation(self):
        dropdown = DropDown()
            
        mainbutton = Button(text='Menu', size_hint=(0.1, 0.07))
        mainbutton.bind(on_release=dropdown.open)
        btn = Button(text='camera_view', size_hint_y=None, pos_hint=( 0.9,  0.5),height=34)

        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            
        dropdown.add_widget(btn)

        btn1 = Button(text='text_view', size_hint_y=None,height=34)

        btn1.bind(on_release=lambda btn1: dropdown.select(btn1.text))
            
        dropdown.add_widget(btn1)

        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        runTouchApp(mainbutton)
        

 
    def add(self):
 
        
        taskname = self.text_input.text
 
        # Add the camera to the ListView
        self.camera_list.adapter.data.extend([taskname])
 
        # Reset the ListView
        self.camera_list._trigger_reset_populate()




 
    def delete(self, *args):
 
        # If a list item is selected
        if self.camera_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.camera_list.adapter.selection[0].text
 
            # Remove the matching item
            self.camera_list.adapter.data.remove(selection)
 
            # Reset the ListView
            self.camera_list._trigger_reset_populate()

# class Imageslide(Carousel):

#     def update(self, dt):
#         self.load_next()

# Clock.schedule_interval(Imageslide.update, 1)

   




class VisionApp(App):
    def build(self):
        return Vision()
 
 
dbApp = VisionApp()
 
dbApp.run()



