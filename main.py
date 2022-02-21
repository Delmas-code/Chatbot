

Main ='''
MDScreen:
    name: "main"
    bot_name: bot_name
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        Image:
            source: "images/chatbot.jpg"
            size_hint: .8, .5
            pos_hint: {"center_x": .5, "center_y": .8}
        MDLabel:
            text: 'Hello sir'
            font_name: "fonts/Poppins-SemiBold"
            font_size: "35sp"
            pos_hint: {"center_x": .5, "center_y": .58}
            halign: "center"
            theme_text_color: "Custom"
            text_color: 53/255, 56/255, 60/255, 1

        MDLabel:
            text: "Your digital assistant here to guide you through our products and services"
            size_hint_x: .9
            font_name: "fonts/Poppins-Regular"
            font_size: "18sp"
            pos_hint: {"center_x": .5, "center_y": .45}
            halign: "center"
            theme_text_color: "Custom"
            text_color: 53/255, 56/255, 60/255, 1

        MDLabel:
            text: "Read Me First"
            size_hint_x: .9
            font_name: "fonts/Poppins-Regular"
            font_size: "18sp"
            pos_hint: {"center_x": .5, "center_y": .33}
            halign: "center"
            underline: "True"
            theme_text_color: "Custom"
            text_color: 1, 170/255, 23/255, 1

        MDFloatLayout:
            size_hint: .85, .08
            pos_hint: {"center_x": .5, "center_y": .22} 
            canvas:
                Color:
                    rgb: (238/255, 238/255, 238/255, 1)  
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [22, 22, 22, 22]
            TextInput:
                id: bot_name
                hint_text: "ChatBot's Name"
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

        MDFloatLayout:
            size_hint: .45, .08
            pos_hint: {"center_x": .5, "center_y": .1} 
            canvas:
                Color:
                    rgb: (1, 170/255, 23/255, 1)  
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [22, 22, 22, 22]

            Button:
                text: ""
                size_hint: .45, .08
                pos_hint: {"center_x": .5, "center_y": .4}
                background_color: 0, 0, 0, 0
                on_release: app.bot_name()

            MDLabel:
                text: "LET'S CHAT"
                halign: 'center'
                pos_hint: {"center_x": .5,"center_y": .4}
                font_name: "fonts/Poppins-SemiBold"
                font_size: "18sp"
                color: 1, 1, 1, 1






'''