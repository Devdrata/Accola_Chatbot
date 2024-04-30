from kivy.core.text import markup
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from threading import Thread
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.image import Image
from kivy.graphics import Color, Rectangle
import time
import sys
from kivy.config import Config
from kivy.core.window import Window
import response
Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '700')
Config.set('graphics','position','custom')
Config.write()
Window.top = 50
Window.left = 540
class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.transit_scene, 3)
    def transit_scene(self, *args):
        try:
            file = open("Data.txt")
            if len(file.readlines())!=0:
                self.manager.current = "Chat with bot"
            else:
                self.manager.current = "form"
        except:
            self.manager.current = "form"

class DetailsScreen(Screen):
    def formbutton(self):
        file = open("Data.txt","a+")
        file.truncate(0)
        file.write(f"{self.ids.username.text} \n")
        file.write(f"{self.ids.schl.text} \n")
        file.write(f"{self.ids.grade.text} \n")
        file.write(f"{self.ids.board.text} \n")
        file.write(f"{self.ids.goal.text} \n")
        file.write(f"{self.ids.name.text}")
        file.close()
        self.manager.current = "Chat with bot"


class ChathistScreen(Screen,GridLayout):

  count = -1
  labellist = []
  def __init__(self,**kwargs):
    super(Screen,self).__init__(**kwargs)
    Clock.schedule_interval(self.ch,2)
  historytext=StringProperty("")

  etext = StringProperty(f"Waiting for data...")
  def ch(self,dt=0):
      #file = open("res.txt","r")
      #try:
      #  dat = file.readlines()[-1]
      #  self.ids.emotionlabel.text = f"You seem {dat}"
      #  #if dat == "Sad":
      #  #    pass
      #  #    trivia
      #except:
      #      pass
      #    self.ids.emotionlabel.text = "Waiting for data..."
      pass
      #file.close()
  count = 0
  def send(self,count):
    abcdf = self.ids.msg.cursor
    labeltxt = self.ids.msg.text
    labeltxtretain = labeltxt
    self.ids.msg.text = ""
    tl = f"You: {labeltxtretain}"
    responset = response.idk()
    label1 = Label(text= f'[color=fbe86c]{tl}[/color]',font_size = 25,text_size= (self.width, None),size_hint_y=None,halign = "right",markup = True)
    #label1 = TextInput(text= tl,size_hint_x = None, width = abcdf[0]*60,size_hint_y = None,font_size = 20,  height=var,halign = "right",disabled = True,background_color = (0,0,0,0),disabled_foreground_color = (251/255, 232/255, 108/255,1))
    label2 = Label(text=f"ABC:{responset}",font_size = 25,text_size= (self.width, None),size_hint_y = None, halign="left", color=(1,1,1, 1))
    self.ids.BL.add_widget(label1)
    self.ids.BL.add_widget(label2)
    self.count+=1
            
class ScreenManagement(ScreenManager):
    pass
class QCEApp(App):
  pass
QCEApp().run()
