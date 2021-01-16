from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import sqlite3


class Login(Screen):

    def __init__(self, **kwargs):

        super(Login, self).__init__(**kwargs)

        layout_box = BoxLayout(orientation='vertical')
        layout_box.add_widget(Label(text='Zaloguj się', font_size='20sp'))

        data_box = BoxLayout(orientation='vertical')
        data_box.add_widget(Label(text='Login', font_size='20sp'))
        self.login = TextInput(
            multiline=False, readonly=False, halign="center", font_size=20
        )
        data_box.add_widget(self.login)
        data_box.add_widget(Label(text='Twoje hasło', font_size='20sp'))
        self.password = TextInput(
            multiline=False, readonly=False, halign="center", font_size=20
        )
        data_box.add_widget(self.password)
        layout_box.add_widget(data_box)

        submit_button = Button(
            text="Zaloguj się", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        submit_button.bind(on_press=self.on_submit)
        layout_box.add_widget(submit_button)

        self.add_widget(layout_box)

    def on_submit(self, instance):

        db_path = './sqlite/app_database.db'
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        sql = f'SELECT * FROM users WHERE username=? AND password=?'
        recs = cursor.execute(sql, (self.login.text, self.password.text))
        rows = cursor.fetchall()
        cursor.close()

        if rows:
            self.parent.current = 'main_menu'
        else:
            content = Button(text='Błędna nazwa użytkownika lub hasło')
            popup = Popup(title='Error', content=content, auto_dismiss=False)
            content.bind(on_press=popup.dismiss)
            popup.open()
