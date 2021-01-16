from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class Tests(Screen):

    def __init__(self, **kwargs):

        super(Tests, self).__init__(**kwargs)

        layout_box = BoxLayout(orientation='vertical')
        layout_box.add_widget(Label(text='Twoje gry', font_size='20sp'))
        layout_box.add_widget(Label(
            text='Tutaj docelowo będą znajdować się gry umożliwiające zbadanie funkcji poznawczych użytkownika',
            font_size='10sp'))
        back_button = Button(
            text="Powrót", pos_hint={"center_x": 0.5, "center_y": 0.5}, on_press=self.on_back
        )
        layout_box.add_widget(back_button)
        self.add_widget(layout_box)

    def on_back(self, instance):
        self.parent.current = 'main_menu'
