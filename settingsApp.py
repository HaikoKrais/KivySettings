# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.settings import SettingsWithTabbedPanel
from kivy.uix.settings import SettingsWithSpinner
from kivy.uix.settings import SettingsWithSidebar
from kivy.uix.settings import SettingsWithNoMenu
from kivy.uix.togglebutton import ToggleButton


class SettingsApp(App):
    choices = {'TabbedPanel': SettingsWithTabbedPanel,
               'Spinner': SettingsWithSpinner,
               'Sidebar': SettingsWithSidebar,
               'NoMenu': SettingsWithNoMenu}

    def build(self):
        self.settings_cls = SettingsWithSidebar
        self.config.read('mysettings.ini')

    def build_settings(self, settings):
        '''The json file will be loaded and constructs the layout of the menu'''
        settings.add_json_panel('Panel 1', self.config, 'settings.json')

    def set_type(self, settings_type):
        # old layout needs to be removed or nothing will be updated
        self.destroy_settings()
        # set chosen layout
        self.settings_cls = self.choices[settings_type]

    def untoggle(self, active_button):
        buttons = ('TabbedPanel', 'Spinner', 'Sidebar', 'NoMenu')

        for button in buttons:
            if button != active_button:
                self.get_running_app().root.ids[button].state = 'normal'

    def print_current_settings(self):
        # get all items of the settings
        items = self.config.items('Panel 1')

        # loop over the items and print them to the label
        text = ''
        for item in items:
            text = text + self.config.get('Panel 1', item[0]) + '\n'

        self.root.ids['settings_content'].text = text

    def on_config_change(self, config, section, key, value):
        print('config has changed.\nsection: {}, key: {}, new value: {}'.format(section, key, value))
        if key == 'item 3':
            if value == 'Blau':
                self.root.ids['settings_content'].color = (0, 0, 1, 1)
                print('Blue selected')
            if value == 'Gelb':
                self.root.ids['settings_content'].color = (0, 1, 0, 1)
                print('Yellow selected')
            if value == 'Schwarz':
                self.root.ids['settings_content'].color = (0, 0, 0, 1)
                print('Black selected')


SettingsApp().run()
