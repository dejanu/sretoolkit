#kivy.require("v1.10.0")
#module for GUI
import webbrowser
from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label

class LoginScreen(BoxLayout):
    
    def __init__(self,**kwargs):
        super(LoginScreen, self).__init__(**kwargs)


        # distance between elements
        self.padding = 50

        # distance from root layout
        self.spacing = 10
        
        #self.orientation='horizontal'
        self.orientation='vertical'
       
        
        # sizing widgets with size_hint = % of layout size (600x800)
        self.b1=Button(text='First button',size=(100, 100),size_hint=(.5, .5))
        self.l1=Label(text="Empty")
        self.add_widget(self.b1)
        self.add_widget(self.l1)


        #positioning widgets  poz_hint={'x':0.5,'y':0.5}
        
        self.buton2 = Button(text='Second button',color=(0,1,1,1))
        
        self.buton2.size_hint = (None,None)
        self.buton2.width = 200
        self.buton2.height = 50
        self.l2=Label(text="Empty")
        self.add_widget(self.buton2)
        self.add_widget(self.l2)

        #bind the on_press event to clock_buton
        self.buton2.bind(on_press=self.click_buton2)
        self.b1.bind(on_press=self.click_buton1)
        
    def click_buton1(self,obj):
        self.l1.text=self.b1.text

    def click_buton2(self,obj):
        self.l2.text=self.buton2.text
   
        

class MyApp(App):
    
    def build(self):
        x=LoginScreen()
        return x
  
if __name__=='__main__':
    MyApp().run()

