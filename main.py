from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import requests

Window.clearcolor = (0.05, 0.05, 0.1, 1)

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        layout.add_widget(Label(text='J.A.R.V.I.S V6 ONLINE', font_size=28, bold=True, color=(0,0.8,1,1)))
        layout.add_widget(Label(text='Acesso Restrito - Tony Stark', font_size=14, color=(0.7,0.7,0.7,1)))
        self.user = TextInput(hint_text='Usuario', multiline=False, size_hint_y=None, height=50)
        self.pwd = TextInput(hint_text='Senha', password=True, multiline=False, size_hint_y=None, height=50)
        self.msg = Label(text='Usuario: jarvis | Sen
