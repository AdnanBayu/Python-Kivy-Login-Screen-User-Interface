#import all the needed package
import kivy
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.animation import Animation
from kivy.properties import NumericProperty

#Set the app size (x axis, y axis)
Window.size = (320, 600)

#class for the first window
class FirstScreen(Screen):
    pass

#class for the second window
class SecondScreen(Screen):
    pass

#class for window manager
#window manager used for the managing between the first and second window
class WindowManager(ScreenManager):
    pass

#class for the music disc in the second window
#something still don't work (i can't figure out what is happening)
class SongCover(MDBoxLayout):
    angle = NumericProperty()
    anim = Animation(angle=360, d=3, t='linear')
    anim += Animation(angle=0, d=0, t='linear')
    
    progress = Animation(value=100, d=100, t='linear')
    anim.repeat = True
    
    def rotate(self):
        if self.anim.have_properties_to_animate(self):
            self.anim.stop(self)
            self.progress.stop(self.widget)
        else:
            self.anim.start(self)
            self.progress.start(self.widget)
    def play (self, widget):
        self.widget = widget
        self.progress.start(widget)
        self.rotate()

#assign "music.kv" file as kv and load it using Builder.load_file
kv = Builder.load_file("music.kv")

#class for the main app (main class)
class MyApp(MDApp):
    def build(self):
        return kv                                           #return the program to load "music.kv" file

#run the program
if __name__ == "__main__":
    MyApp().run()