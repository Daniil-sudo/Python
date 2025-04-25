from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

import random
from kivy.metrics import dp
from kivymd.uix.card import MDCard

class Demo(MDApp):
    def generate_password(self, length=20):
        """Генерирует случайный пароль."""
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        symbols = ["!", "@", "#", "$", "%"]
        all_chars = letters + numbers + symbols
        password = ''.join(random.choice(all_chars) for _ in range(length))
        return password

    def build(self):
        screen = Screen()
        self.password = self.generate_password() # Генерируем пароль здесь

        #MDCard для улучшения контраста
        card = MDCard(
            size_hint=(None, None),
            size=(dp(300), dp(50)),  # Размеры карточки
            pos_hint={'center_x': 0.5, 'center_y': 0.5},  # Положение в центре
            md_bg_color=(0.2, 0.2, 0.2, 1)  # Темно-серый фон карточки
        )

        # defining label with all the parameters
        l = MDLabel(text=self.password, halign='center',  # Используем self.password
                    theme_text_color="Custom",
                    text_color=(0, 1, 0, 1), # Ярко-зеленый цвет (R, G, B, A)
                    font_style='Body1' #Более крупный шрифт
                    )
        l.pos_hint = {'center_x': 0.5, 'center_y': 0.5} # Центрируем метку внутри карточки

        # adding widgets to screen
        card.add_widget(l)
        screen.add_widget(card)
        # returning the screen
        return screen

if __name__ == "__main__":
    Demo().run()