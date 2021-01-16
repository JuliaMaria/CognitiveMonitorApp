from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import sqlite3


class Results(Screen):

    def __init__(self, **kwargs):

        super(Results, self).__init__(**kwargs)

        # Get example user data...
        self.get_user_data()

        layout_box = BoxLayout(orientation='vertical')
        layout_box.add_widget(Label(text='Twoje wyniki', font_size='20sp'))
        plt.plot(self.user_data.get('dates'), self.user_data.get('scores'))
        plt.xlabel('Data')
        plt.ylabel('Wynik')
        layout_box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        back_button = Button(
            text="Powrót", pos_hint={"center_x": 0.5, "center_y": 0.5}, on_press=self.on_back
        )
        layout_box.add_widget(back_button)
        self.add_widget(layout_box)

    def get_user_data(self):

        db_path = r'./sqlite/app_database.db'
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql = f'SELECT * FROM results WHERE username=? AND phone_email=?'
        recs = cursor.execute(sql, ("Grażyna", "grazyna@gmail.com"))
        rows = cursor.fetchall()
        cursor.close()

        self.user_data = {
            'dates': list(map(lambda x: x[2], rows)),
            'scores': list(map(lambda x: x[3], rows))
        }

    def on_back(self, instance):
        self.parent.current = 'main_menu'
