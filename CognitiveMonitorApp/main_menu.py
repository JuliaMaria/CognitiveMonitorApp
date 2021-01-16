from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_string("""
<MainMenu>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Menu'
            font_size: '20sp'
        BoxLayout:
            Button:
                text: 'Twój profil'
                on_press: root.manager.current = 'profile'
            Button:
                text: 'Twoje wyniki'
                on_press: root.manager.current = 'results'
        BoxLayout:
            Button:
                text: 'Twoje gry'
                on_press: root.manager.current = 'tests'
        BoxLayout:
            Button:
                text: 'Wyloguj'
                on_press: root.manager.current = 'login'
""")


class MainMenu(Screen):
    pass
