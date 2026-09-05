from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from jarvis_brain_v4 import JarvisAI
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        layout.add_widget(Label(text='JARVIS V6.0 ONLINE', font_size='28sp', bold=True, size_hint_y=0.3))
        self.user_input = TextInput(hint_text='Usuario: jarvis', multiline=False, size_hint_y=0.12)
        self.pass_input = TextInput(hint_text='Senha: JARVIS-2026', password=True, multiline=False, size_hint_y=0.12)
        self.msg = Label(text='', color=(1,0,0,1), size_hint_y=0.1)
        btn = Button(text='ACESSAR ONLINE', size_hint_y=0.15, background_color=(0,0.6,1,1))
        btn.bind(on_press=self.validar)
        layout.add_widget(self.user_input)
        layout.add_widget(self.pass_input)
        layout.add_widget(self.msg)
        layout.add_widget(btn)
        self.add_widget(layout)
    def validar(self, instance):
        if self.user_input.text.strip() == "jarvis" and self.pass_input.text.strip() == "JARVIS-2026":
            self.manager.current = 'jarvis'
        else:
            self.msg.text = 'Use jarvis / JARVIS-2026'
class JarvisLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.jarvis = JarvisAI()
        self.add_widget(Label(text='JARVIS V6 ONLINE - 100% ONLINE', size_hint_y=0.08, bold=True))
        self.chat_history = Label(text='[ONLINE ATIVO]\nJARVIS: Fala Tony Stark, 100% online!\n', size_hint_y=None)
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        scroll = ScrollView(size_hint_y=0.6)
        scroll.add_widget(self.chat_history)
        self.add_widget(scroll)
        box_input = BoxLayout(size_hint_y=0.1)
        self.input_text = TextInput(hint_text='Ordem online...', multiline=False)
        self.input_text.bind(on_text_validate=self.enviar_mensagem)
        box_input.add_widget(self.input_text)
        btn_enviar = Button(text='Enviar', size_hint_x=0.3, background_color=(0,0.6,1,1))
        btn_enviar.bind(on_press=self.enviar_mensagem)
        box_input.add_widget(btn_enviar)
        self.add_widget(box_input)
        box_cmd = BoxLayout(size_hint_y=0.15, spacing=5)
        for txt,cmd in [("Japao","vai chover no Japao hoje?"),("Limpar",None),("Logout",None)]:
            b=Button(text=txt, font_size='10sp')
            if cmd: b.bind(on_press=lambda x,c=cmd: self.executar(c))
            elif txt=="Limpar": b.bind(on_press=lambda x: setattr(self.chat_history,'text','Chat limpo ONLINE\n'))
            else: b.bind(on_press=lambda x: setattr(App.get_running_app().root,'current','login'))
            box_cmd.add_widget(b)
        self.add_widget(box_cmd)
    def executar(self, cmd):
        self.add_chat(f"\nTony: {cmd}\nJARVIS: {self.jarvis.get_response_auto(cmd)}\n")
    def enviar_mensagem(self, instance):
        t=self.input_text.text.strip()
        if not t: return
        self.input_text.text=""
        self.add_chat(f"\nTony: {t}\nJARVIS: {self.jarvis.get_response_auto(t)}\n")
    def add_chat(self, texto):
        self.chat_history.text+=texto+"\n"
class JarvisScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(JarvisLayout())
class JarvisApp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(JarvisScreen(name='jarvis'))
        return sm
if __name__ == '__main__':
    JarvisApp().run()
