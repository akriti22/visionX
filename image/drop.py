from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty, NumericProperty, BooleanProperty
from kivy.lang import Builder

Builder.load_string('''
<DropDown>:
    container: container
    do_scroll_x: False
    size_hint: None, None

    GridLayout:
        id: container
        size_hint_y: None
        height: self.minimum_size[1]
        cols: 1
''')


class DropDownException(Exception):
    '''DropDownException class.
    '''
    pass


class DropDown(ScrollView):
    '''DropDown class. See module documentation for more information.

    :Events:
        `on_select`: data
            Fired when a selection is done, with the data of the selection as
            first argument. Data is what you pass in the :meth:`select` method
            as first argument.
    '''

    auto_width = BooleanProperty(True)
    '''By default, the width of the dropdown will be the same as the width of
    the attached widget. Set to False if you want to provide your own width.
    '''

    max_height = NumericProperty(None, allownone=True)
    '''Indicate the maximum height that the dropdown can take. If None, it will
    take the maximum height available, until the top or bottom of the screen
    will be reached.

    :data:`max_height` is a :class:`~kivy.properties.NumericProperty`, default
    to None.
    '''

    dismiss_on_select = BooleanProperty(True)
    '''By default, the dropdown will be automatically dismissed when a selection
    have been done. Set to False to prevent the dismiss.

    :data:`dismiss_on_select` is a :class:`~kivy.properties.BooleanProperty`,
    default to True.
    '''

    attach_to = ObjectProperty(allownone=True)
    '''(internal) Property that will be set to the widget on which the drop down
    list is attached to.

    The method :meth:`open` will automatically set that property, while
    :meth:`dismiss` will set back to None.
    '''

    container = ObjectProperty()
    '''(internal) Property that will be set to the container of the dropdown
    list, which is a :class:`~kivy.uix.gridlayout.GridLayout` by default.
    '''

    def __init__(self, **kwargs):
        self._win = None
        self.register_event_type('on_select')
        super(DropDown, self).__init__(**kwargs)
        self.container.bind(minimum_size=self._container_minimum_size)
        self.bind(size=self._reposition)

    def open(self, widget):
        '''Open the dropdown list, and attach to a specific widget.
        Depending the position of the widget on the window and the height of the
        dropdown, the placement might be lower or higher off that widget.
        '''
        # ensure we are not already attached
        if self.attach_to is not None:
            self.dismiss()

        # we will attach ourself to the main window, so ensure the widget we are
        # looking for have a window
        self._win = widget.get_parent_window()
        if self._win is None:
            raise DropDownException(
                'Cannot open a dropdown list on a hidden widget')

        self.attach_to = widget
        widget.bind(pos=self._reposition, size=self._reposition)
        self._reposition()

        # attach ourself to the main window
        self._win.add_widget(self)

    def dismiss(self, *largs):
        '''Remove the dropdown widget from the iwndow, and detach itself from
        the attached widget.
        '''
        if self.parent:
            self.parent.remove_widget(self)
        if self.attach_to:
            self.attach_to.unbind(pos=self._reposition, size=self._reposition)
            self.attach_to = None

    def select(self, data):
        '''Call this method to trigger the `on_select` event, with the `data`
        selection. The `data` can be anything you want.
        '''
        self.dispatch('on_select', data)
        if self.dismiss_on_select:
            self.dismiss()

    def on_select(self, data):
        pass

    def _container_minimum_size(self, instance, size):
        if self.max_height:
            self.height = min(size[1], self.max_height)
            self.do_scroll_y = size[1] > self.max_height
        else:
            self.height = size[1]
            self.do_scroll_y = True

    def add_widget(self, *largs):
        if self.container:
            return self.container.add_widget(*largs)
        return super(DropDown, self).add_widget(*largs)

    def remove_widget(self, *largs):
        if self.container:
            return self.container.remove_widget(*largs)
        return super(DropDown, self).remove_widget(*largs)

    def clear_widgets(self):
        if self.container:
            return self.container.clear_widgets()
        return super(DropDown, self).clear_widgets()

    def on_touch_down(self, touch):
        if super(DropDown, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos):
            return True
        self.dismiss()

    def on_touch_up(self, touch):
        if super(DropDown, self).on_touch_up(touch):
            return True
        self.dismiss()

    def _reposition(self, *largs):
        # calculate the coordinate of the attached widget in the window
        # coordinate sysem
        win = self._win
        widget = self.attach_to
        if not widget or not win:
            return
        wx, wy = widget.to_window(*widget.pos)
        wright, wtop = widget.to_window(widget.right, widget.top)

        # set width and x
        if self.auto_width:
            self.width = wright - wx

        # ensure the dropdown list doesn't get out on the X axis, with a
        # preference to 0 in case the list is too wide.
        x = wx
        if x + self.width > win.width:
            x = win.width - self.width
        if x < 0:
            x = 0
        self.x = x

        # determine if we display the dropdown upper or lower to the widget
        h_bottom = wy - self.height
        h_top = win.height - (wtop + self.height)
        if h_bottom > 0:
            self.top = wy
        elif h_top > 0:
            self.y = wtop
        else:
            # none of both top/bottom have enough place to display the widget at
            # the current size. Take the best side, and fit to it.
            height = max(h_bottom, h_top)
            if height == h_bottom:
                self.top = wy
                self.height = wy
            else:
                self.y = wtop
                self.height = win.height - wtop


if __name__ == '__main__':
    from kivy.uix.button import Button
    from kivy.base import runTouchApp

    def show_dropdown(button, *largs):
        dp = DropDown()
        dp.bind(on_select=lambda instance, x: setattr(button, 'text', x))
        for i in xrange(10):
            item = Button(text='hello %d' % i, size_hint_y=None, height=44)
            item.bind(on_release=lambda btn: dp.select(btn.text))
            dp.add_widget(item)
        dp.open(button)

    def touch_move(instance, touch):
        instance.center = touch.pos

    btn = Button(text='SHOW', size_hint=(None, None), pos=(300, 200))
    btn.bind(on_release=show_dropdown, on_touch_move=touch_move)

    runTouchApp(btn)