import wx

import wx.grid


class Calulator(wx.Frame):
    def __init__(self, parent, id,  title):
        wx.Frame.__init__(self, parent, id, title, size=(600, 400))

        self.cal()

    def cal(self):
        self.Show(True)
        self.pnl = wx.Panel(self, size=(600, 400))
        self.number1 = wx.TextCtrl(self.pnl, pos=(1,5))
        self.number2 = wx.TextCtrl(self.pnl, pos=(1,30))
        self.answer= wx.TextCtrl(self.pnl, pos=(1,60))

        self.theButtonPlus = wx.Button(self.pnl, label="+")
        self.theButtonMinus = wx.Button(self.pnl, label="-")
        self.theButtonTime = wx.Button(self.pnl, label="x")
        self.theButtonDivide = wx.Button(self.pnl, label="/")
        self.theButtonClear = wx.Button(self.pnl, label="clear")

        self.Bind(wx.EVT_BUTTON, self.buttonPressAdd, self.theButtonPlus)
        self.Bind(wx.EVT_BUTTON, self.buttonPressMinus, self.theButtonMinus)
        self.Bind(wx.EVT_BUTTON, self.buttonPressTime, self.theButtonTime)
        self.Bind(wx.EVT_BUTTON, self.buttonPressDivide, self.theButtonDivide)
        self.Bind(wx.EVT_BUTTON, self.buttonPressClear, self.theButtonClear)

        self.sizer = wx.GridBagSizer(hgap=200, vgap=40)

        self.sizer.Add(self.theButtonPlus, pos=(1, 1), flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.sizer.Add(self.theButtonMinus, pos=(2, 1), flag=wx.ALIGN_CENTER | wx.ALL, border=2)
        self.sizer.Add(self.theButtonTime, pos=(3, 1), flag=wx.ALIGN_CENTER | wx.ALL, border=2)
        self.sizer.Add(self.theButtonDivide, pos=(4, 1), flag=wx.ALIGN_CENTER | wx.ALL, border=2)
        self.sizer.Add(self.theButtonClear, pos=(5, 1), flag=wx.ALIGN_CENTER | wx.ALL, border=2)
        self.pnl.SetSizerAndFit(self.sizer)

    #def getValues(self):


    def buttonPressAdd(self, event):
        int1 = int(self.number1.Value)
        int2 = int(self.number2.Value)
        self.result = int1+int2
        self.answer.display= self.result
        self.number1.Value = ""
        self.number2.Value = ""



    def buttonPressMinus(self, event):
        int1 = int(self.number1.Value)
        int2 = int(self.number2.Value)





        return int1+int2

    def buttonPressTime(self, event):
        int1 = int(self.number1.Value)
        int2 = int(self.number2.Value)

        return int1+int2

    def buttonPressDivide(self, event):
        int1 = int(self.number1.Value)
        int2 = int(self.number2.Value)
        return int1+int2

    def buttonPressClear(self, event):
        int1 = int(self.number1.Value)
        int2 = int(self.number2.Value)
        return int1+int2



app = wx.App()
frame = Calulator(None,-1,'My App')
#frame = GridFrame(None)
app.MainLoop()
