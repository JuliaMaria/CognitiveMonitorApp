from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
import sqlite3


class Profile(Screen):

    def __init__(self, **kwargs):

        super(Profile, self).__init__(**kwargs)

        self.get_user_data()

        layout_box = BoxLayout(orientation='vertical')
        layout_box.add_widget(Label(text='Twój profil', font_size='10sp'))
        layout_box.add_widget(Label(text='Tutaj możesz zmieniać swoje dane', font_size='10sp'))

        age_box = BoxLayout(orientation='vertical')
        age_box.add_widget(Label(text='Twój rok urodzenia', font_size='10sp'))
        self.age = TextInput(
            input_filter='int', text=str(self.user_data.get('year_of_birth')), multiline=False, readonly=False, halign="center", font_size=10
        )
        age_box.add_widget(self.age)
        layout_box.add_widget(age_box)

        data_box = BoxLayout(orientation='vertical')
        data_box.add_widget(Label(text='Twój numer lub adres email', font_size='10sp'))
        self.phone_email = TextInput(
            text=str(self.user_data.get('phone_email')), multiline=False, readonly=True, halign="center", font_size=7
        )
        data_box.add_widget(self.phone_email)
        data_box.add_widget(Label(text='Twoje hasło', font_size='10sp'))
        self.password = TextInput(
            text=str(self.user_data.get('password')), multiline=False, readonly=True, halign="center", font_size=10
        )
        data_box.add_widget(self.password)
        layout_box.add_widget(data_box)

        email_box = BoxLayout(orientation='vertical')
        email_box.add_widget(Label(text='Adres email do bliskiej osoby', font_size='10sp'))
        self.family_email = TextInput(
            text=str(self.user_data.get('family_email')), multiline=False, readonly=False, halign="center", font_size=7
        )
        email_box.add_widget(self.family_email)
        email_box.add_widget(Label(text='Adres email do lekarza', font_size='10sp'))
        self.doctor_email = TextInput(
            text=str(self.user_data.get('doctor_email')), multiline=False, readonly=False, halign="center", font_size=7
        )
        email_box.add_widget(self.doctor_email)
        layout_box.add_widget(email_box)

        gender_box = BoxLayout(orientation='horizontal')
        gender_box.add_widget(Label(text='Twoja płeć', font_size='20sp'))
        btn1 = ToggleButton(text='Mężczyzna', group='sex', on_press=self.on_set_sex,
                            state=('down' if self.sex == 'M' else 'normal'))
        btn2 = ToggleButton(text='Kobieta', group='sex', on_press=self.on_set_sex,
                            state=('down' if self.sex == 'K' else 'normal'))
        gender_box.add_widget(btn1)
        gender_box.add_widget(btn2)
        layout_box.add_widget(gender_box)

        disability_box = BoxLayout(orientation='horizontal')
        disability_box.add_widget(Label(text='Powód korzystania z aplikacji', font_size='20sp'))
        btn1 = ToggleButton(text='Zespół otępienny', group='disability', on_press=self.on_set_disability, state='down')
        btn2 = ToggleButton(text='Ryzyko zespołu otępiennego', group='disability', on_press=self.on_set_disability)
        disability_box.add_widget(btn1)
        disability_box.add_widget(btn2)
        layout_box.add_widget(disability_box)

        submit_button = Button(
            text="Zatwierdź", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        submit_button.bind(on_press=self.on_submit)
        back_button = Button(
            text="Powrót", pos_hint={"center_x": 0.5, "center_y": 0.5}, on_press=self.on_back
        )
        layout_box.add_widget(submit_button)
        layout_box.add_widget(back_button)

        self.add_widget(layout_box)

    def get_user_data(self):

        db_path = r'./sqlite/app_database.db'
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql = f'SELECT * FROM users WHERE username=? AND phone_email=?'
        recs = cursor.execute(sql, ("Grażyna", "grazyna@gmail.com"))
        rows = cursor.fetchall()[0]
        cursor.close()

        self.user_data = {'username': rows[0], 'password': '*'*len(rows[1]), 'phone_email': rows[2],
                          'year_of_birth': rows[3], 'sex': rows[4], 'disability': rows[5], 'doctor_email': rows[6],
                          'family_email': rows[7]}
        self.sex = self.user_data['sex']
        self.disability = self.user_data['disability']

    def on_set_sex(self, instance):
        if instance.text == "Mężczyzna":
            self.sex = 'M'
        elif instance.text == "Kobieta":
            self.sex = 'K'

    def on_set_disability(self, instance):
        if instance.text == "Zespół otępienny":
            self.disability = 1
        elif instance.text == "Ryzyko zespołu otępiennego":
            self.disability = 0

    def on_back(self, instance):
        self.parent.current = 'main_menu'

    def on_submit(self, instance):
        db_path = r'./sqlite/app_database.db'
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""UPDATE users SET year_of_birth=?, sex=?, disability=?, family_email=?, doctor_email=? WHERE username=? AND phone_email=?""",
                       (self.age.text, self.sex, self.disability, self.family_email.text, self.doctor_email.text, "Grażyna", "grazyna@gmail.com"))
        conn.commit()
        cursor.close()
        self.parent.current = 'main_menu'
