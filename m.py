from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivymd.theming import ThemeManager
#from kivymd.navigationdrawer import NavigationDrawer
from kivymd.toolbar import Toolbar
from navigationdrawer import NavigationDrawer

main_widget_kv = '''
#:import Toolbar kivymd.toolbar.Toolbar

BoxLayout:
    orientation: 'vertical'
    Toolbar:
        id: toolbar
        title: 'Welcome'
        background_color: app.theme_cls.primary_dark
        left_action_items: [['menu',lambda x: app.nav_drawer.toggle()]]
        right_action_items: [['more-vert', lambda x: app.raised_button.open(self.parent)]]
    Label:

<Navigator>:
    NavigationDrawerIconButton:
        icon: 'face'
        text: 'Akriti Singh'
    NavigationDrawerIconButton:
        icon: 'email'
        text: 'akriti@gmail.com'
        on_release: app.root.ids.scr_mngr.current = 'bottomsheet'
    NavigationDrawerIconButton:
        icon: 'phone'
        text: '+91-797XXXXXX'
    NavigationDrawerIconButton:
        icon: 'cake'
        text: '22/01/1995'
    NavigationDrawerIconButton:
        icon: 'city-alt'
        text: 'jamshedpur'
    NavigationDrawerIconButton:
        icon: 'settings'
        text: 'Settings'
    '''

class Navigator(NavigationDrawer):
    
    image_source = StringProperty('a.png')

class NavigateApp(App):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    def build(self):
        main_widget = Builder.load_string(main_widget_kv)
        #self.nav_drawer = Navigator()
        return main_widget

NavigateApp().run()

