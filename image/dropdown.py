from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.app import App 

class Akriti(App):

	def secim(self,nesne):
		if nesne.text=="view1":
			self.resin.color=(0,0,1.1)

		elif nesne.text=="View2":
			self.resin.color=(1,0,0,1)
		self.dropdown.select(nesne.text)
		self.anaDugme.text=nesne.text


	def biuild(self):
		self.renkler=(["view1"], ["View2"],["View3"])
		duzen=BoxLayout()
		seld.dropdown=Dropdown()
		self.resin=Image()
		for renk in self.renkler:
			
			dugme = Button(text=renk[0],size_hint_y=None,height=50)
			dugme.bind(on_release=self.secim)
			self.dropdown.add_widget(dugme)

		self.anaDugme=Button(text="Renkler",size_hint=(None,None))
		self.anaDugme.bind(on_release=self.dropdown.open)
		duzen.add_widget(self.anaDugme)
		duzen.add_widget(self.resin)
		return duzen

Akriti().run()
