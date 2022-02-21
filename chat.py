Chat = '''
<Command>
    size_hint_y: None
    pos_hint: {"right": .98}
    height: self.texture_size[1]
    padding: 12, 10
    theme_text_color: "Custom"
    text_color: 1, 1, 1, 1

    canvas.before:
        Color:
            rgb: (1, 170/255, 23/255, 1)
        RoundedRectangle:
            size: self.width, self.height
            pos: self.pos
            radius: [23, 23, 0, 23]

<Response>
    size_hint_y: None
    pos_hint: {"x": .02}
    height: self.texture_size[1]
    padding: 12, 10
    canvas.before:
        Color:
            rgb: (1, 1, 1, 1)
        RoundedRectangle:
            size: self.width, self.height
            pos: self.pos
            radius: [23, 23, 23, 0]


MDScreen:
    bot_name: bot_name
    text_input: text_input
    chat_list: chat_list
    name: "chats"

    MDFloatLayout:
        MDFloatLayout:
            md_bg_color: 245/255, 245/255, 245/255, 255/255
            size_hint_y: .11
            pos_hint: {"center_y": .95}
            MDLabel:
                id: bot_name
                text: "Jarvis AI"
                pos_hint: {"center_y": .5}
                halign: "center"
                font_name: "fonts/Poppins-SemiBold"
                theme_color: "Custom"
                text_color: 53/255, 56/255, 60/255, 1

        ScrollView:
            size_hint_y: .75
            pos_hint: {"x": 0, "y": .116}
            do_scroll_x: False
            do_scroll_y: True
            BoxLayout: 
                id: chat_list
                orientation: 'vertical'
                size: (root.width, root.height)
                height: self.minimum_height
                size_hint: None, None
                pos_hint: {'top': 10}
                cols: 1
                spacing: 5
        MDFloatLayout:
            md_bg_color: 245/255, 245/255, 245/255, 255/255
            size_hint_y: .11
            MDFloatLayout:
                size_hint: .8, .75
                pos_hint: {"center_x": .43, "center_y": .5} 
                canvas:
                    Color:
                        rgb: (238/255, 238/255, 238/255, 1)  
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [23, 23, 23, 23]
                TextInput:
                    id: text_input
                    hint_text: "Enter yor message..."
                    size_hint: 1, None
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_size: "18sp"
                    height: self.minimum_height
                    cursor_color:  1, 170/255, 23/255, 1
                    cursor_width: "2sp"
                    foreground_color: 1, 170/255, 23/255, 1
                    background_color: 0, 0, 0, 0
                    padding: 15
                    font_name: "fonts/Poppins-Regular"
            MDIconButton:
                icon: 'send'
                pos_hint: {"center_x": .91, "center_y": .5}
                user_font_size: '18sp'
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: 1, 170/255, 23/255, 1
                on_release: app.send()
                    
                




'''
           
           
            #    height: self.texture_size[1]
