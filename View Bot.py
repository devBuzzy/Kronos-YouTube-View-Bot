# Kronos YouTube View Bot V1.0

import wx
from selenium import webdriver
import itertools
import time


proxies = open("C:\Users\Ethan\Documents\YouTube\Bots\proxies.txt")

fp = webdriver.FirefoxProfile()
fp.set_preference('network.proxy.ssl', next(proxies))
fp.set_preference('network.proxy.http', next(proxies))
fp.set_preference('network.proxy.type', 1)

class App(wx.App):

    def OnInit(self):
      frame = MainFrame()
      frame.Show()
      self.SetTopWindow(frame)
      return True

class MainFrame(wx.Frame): # Main Frame

    title = "Kronos View Bot V1.0"
    
    def __init__(self):
      wx.Frame.__init__(self, wx.GetApp().TopWindow, title=self.title, style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
      panel=wx.Panel(self)
      textbox1 = wx.TextCtrl(panel, pos=(10,10),size=(100,-1))
      textbox1.AppendText("Video Url")
      textbox2 = wx.TextCtrl(panel, pos=(10,40),size=(100,-1))
      textbox2.AppendText("# of Views")
      def loopin(event):
        driver=webdriver.Firefox()
        i = int(textbox2.GetValue())
        for _ in itertools.repeat(None, i):
            if i > 0:
                driver.get(textbox1.GetValue())
            if i < 0:
                textbox2.SetValue("Insert a # greater than 0")
      button1=wx.Button(panel, label="View!", pos=(10,70),size=(120,30))
      self.Bind(wx.EVT_BUTTON, loopin, button1)
      
if __name__=='__main__':
    app = App(False)
    app.MainLoop()

