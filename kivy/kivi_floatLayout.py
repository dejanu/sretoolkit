
import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class cmm(FloatLayout):

    def __init__(self, **kwargs):
        super(cmm, self).__init__(**kwargs)
        
        # .pos tuplu pentru positioning
        # relativ la dimensiune, default pentru window (800,600)

        # .size_hint tuplu pentru children proportions
        # proportions are not absolute(cm/pixels) , they are relative to the Layout
    
        self.buton1 = Button(text='Primul buton')# nu mai este self.button
        self.buton1.size_hint=(0.3,0.2)
        self.buton1.pos=(500,100)
        self.add_widget(self.buton1) # nu mai este self.button


        self.buton2 = Button(text='Al doilea buton')
        self.buton2.size_hint=(0.2,0.1)
        self.buton2.pos=(100,500)
        self.add_widget(self.buton2)
        
class MyApp(App):

    def build(self):
        x=cmm()
        return x


if __name__ == '__main__':
    MyApp().run()
