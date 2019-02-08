import os

from kivy.app import App
from kivy.lang import Builder

from kivymd.list import BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.theming import ThemeManager

# User defined imports
from kivy.core.window import Window

# Window.fullscreen = "auto"


class HackedDemoNavDrawer(MDNavigationDrawer):
    # DO NOT USE
    def add_widget(self, widget, index=0):
        if issubclass(widget.__class__, BaseListItem):
            self._list.add_widget(widget, index)
            if len(self._list.children) == 1:
                widget._active = True
                self.active_item = widget
            # widget.bind(on_release=lambda x: self.panel.toggle_state())
            widget.bind(on_release=lambda x: x._set_active(True, list=self))
        elif issubclass(widget.__class__, NavigationDrawerHeaderBase):
            self._header_container.add_widget(widget)
        else:
            super(MDNavigationDrawer, self).add_widget(widget, index)


class MainApp(App):
    theme_cls = ThemeManager()
    title = "Application"

    def build(self):
        main_widget = Builder.load_file(
            os.path.join(os.path.dirname(__file__), "./app.kv")
        )
        # self.theme_cls.theme_style = 'Dark'

        main_widget.ids.text_field_error.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message)
        self.bottom_navigation_remove_mobile(main_widget)
        return main_widget

    def bottom_navigation_remove_mobile(self, widget):
        # Removes some items from bottom-navigation demo when on mobile
        if DEVICE_TYPE == 'mobile':
            widget.ids.bottom_navigation_demo.remove_widget(widget.ids.bottom_navigation_desktop_2)
        if DEVICE_TYPE == 'mobile' or DEVICE_TYPE == 'tablet':
            widget.ids.bottom_navigation_demo.remove_widget(widget.ids.bottom_navigation_desktop_1)

    def set_error_message(self, *args):
        if len(self.root.ids.text_field_error.text) == 2:
            self.root.ids.text_field_error.error = True
        else:
            self.root.ids.text_field_error.error = False

    def on_pause(self):
        return True

    def on_stop(self):
        pass


if __name__ == '__main__':
    MainApp().run()