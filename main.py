from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.05, 0.1, 1)

class LoginScreen(BoxLayout):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20
        self.app = app

        self.add_widget(Label(text='[b]JARVIS V6 ONLINE[/b]', markup=True, font_size='28sp', color=(0, 1, 1, 1)))
        self.add_widget(Label(text='Sistema 100% Online', font_size='16sp', color=(0.7, 0.7, 0.7, 1)))

        self.user = TextInput(hint_text='Usuario: jarvis', multiline=False, size_hint_y=None, height=50)
        self.passw = TextInput(hint_text='Senha: JARVIS-2026', password=True, multiline=False, size_hint_y=None, height=50)
        self.add_widget(self.user)
        self.add_widget(self.passw)

        self.msg = Label(text='', color=(1, 0.3, 0.3, 1
