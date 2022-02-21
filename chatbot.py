from inspect import FrameInfo
from os import name
from kivy.clock import Clock
from kivy.core import window
from kivy.core import text
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from kivy.core.text import LabelBase

from chat import Chat
from main import Main


Window.size = (350, 550)


class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "fonts/Poppins-Regular"
    font_size = 17


class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "fonts/Poppins-Regular"
    font_size = 17


class ChatBotApp(MDApp):

    #Fuction to handle the multiple screens
    def change_screens(self, name):
        screen_manager.current = name

    #This is the main function which build and renders our widgets
    def build(self):
        global screen_manager

        screen_manager = ScreenManager()
        
        screen_manager.add_widget(Builder.load_string(Main))
        screen_manager.add_widget(Builder.load_string(Chat))


        return screen_manager

    def bot_name(self):
        if screen_manager.get_screen('chats').bot_name.text != "":
            screen_manager.get_screen('chats').bot_name.text = screen_manager.get_screen('main').bot_name.text 
            screen_manager.current = "chats"
        

    #This function will be incharge of sendx a reply to the user
    def response(self, *args):
        response = ""
        if value.lower() == 'hello' or value.lower() == 'hey':
            response = f'Hello, I am your Digital Assistang {screen_manager.get_screen("chats").bot_name.text}. what can i do for you'
        elif value.lower() == 'how are you':
            response = "I'm doing extremely well thanks for asking"
        elif value.lower() == 'who is your father' or 'who created you' or 'who made you':
            response = "That will be Delmas. He made me and I regard Him as my Dad"
        else:
            response = 'Please can you repeat that'

        screen_manager.get_screen('chats').chat_list.add_widget(Response(text=response, size_hint_x=.75))

    #Thisfunction is called when the user sends a msg
    def send(self):
        global size, halign, value
        if screen_manager.get_screen('chats').text_input != "":
            value = screen_manager.get_screen('chats').text_input.text
            if len(value) < 6:
                size = .22
                halign = "center"
            elif len(value) < 11:
                size = .32
                halign = "center"
            elif len(value) < 16:
                size = .45
                halign = "center"
            elif len(value) < 21:
                size = .58
                halign = "center"
            elif len(value) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"

            screen_manager.get_screen('chats').chat_list.add_widget(Command(text=value, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response, 2)
            screen_manager.get_screen('chats').text_input.text = ""


if __name__ == '__main__':

    #Now where ever we want the font to be poppins-reglar.ttf we just put poppins
    # LabelBase.register(name="Poppins", fn_regular="Poppins-Regular.ttf")
    
    ChatBotApp().run()