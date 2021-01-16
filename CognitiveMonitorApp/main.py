from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from main_menu import MainMenu
from profile import Profile
from results import Results
from tests import Tests
from login import Login


class MainApp(App):

    def build(self):

        sm = ScreenManager()
        sm.add_widget(Login(name='login'))
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(Profile(name='profile'))
        sm.add_widget(Results(name='results'))
        sm.add_widget(Tests(name='tests'))

        return sm


if __name__ == "__main__":
    app = MainApp()
    app.run()
