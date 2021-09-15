import wx

class Calulator(wx.Frame):
    def __init__(self, parent, id,  title):
        wx.Frame.__init__(self, parent, id, title, size=(600, 400))
        self.initialise()

    def initialise(self):
        # create title
        self.pnl = wx.Panel(self, size=(600, 400))
        self.row = wx.BoxSizer(wx.VERTICAL)
        self.title = wx.StaticText(self.pnl, label="Simple Calculator")
        self.font = self.title.GetFont()
        self.font = self.font.Bold()
        self.title.SetFont((self.font))
        self.row.Add(self.title, 1, wx.ALIGN_CENTER|wx.BOTTOM, border=2)

        # create two inputs
        self.number = wx.BoxSizer(wx.HORIZONTAL)
        self.number1 = wx.TextCtrl(self.pnl)
        self.number2 = wx.TextCtrl(self.pnl)
        self.number.Add(self.number1, 1, wx.ALIGN_CENTER|wx.RIGHT, border=5)
        self.number.Add(self.number2, 1, wx.ALIGN_CENTER|wx.RIGHT, border=5)
        self.row.Add(self.number, 2, wx.ALIGN_CENTER)
        self.SetSizerAndFit(self.row)

        # create a answer title
        self.title = wx.StaticText(self.pnl, label="Answer")
        self.font = self.title.GetFont()
        self.font = self.font.Bold()
        self.title.SetFont((self.font))
        self.row.Add(self.title, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=2)

        # create answer box
        self.answer = wx.StaticText(self.pnl, label=" ")
        self.answer.SetBackgroundColour(wx.Colour(255, 255, 255, 255))
        self.answer.SetMinSize((100, 50))
        self.row.Add(self.answer, 1, wx.ALIGN_CENTER|wx.BOTTOM, border=10)

        # create 4 buttons
        self.button = wx.BoxSizer(wx.HORIZONTAL)
        self.theButtonPlus = wx.Button(self.pnl, label="+")
        self.theButtonMinus = wx.Button(self.pnl, label="-")
        self.theButtonTime = wx.Button(self.pnl, label="x")
        self.theButtonDivide = wx.Button(self.pnl, label="/")
        self.theButtonClear = wx.Button(self.pnl, label="clear")
        self.button.Add(self.theButtonPlus, 1, wx.ALIGN_CENTER|wx.BOTTOM, border=10)
        self.button.Add(self.theButtonMinus, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=10)
        self.button.Add(self.theButtonTime, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=10)
        self.button.Add(self.theButtonDivide, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=10)
        self.button.Add(self.theButtonClear, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=10)
        self.row.Add(self.button, 1, wx.ALIGN_CENTER)

        self.Bind(wx.EVT_BUTTON, self.buttonPressAdd, self.theButtonPlus)
        self.Bind(wx.EVT_BUTTON, self.buttonPressMinus, self.theButtonMinus)
        self.Bind(wx.EVT_BUTTON, self.buttonPressTime, self.theButtonTime)
        self.Bind(wx.EVT_BUTTON, self.buttonPressDivide, self.theButtonDivide)
        self.Bind(wx.EVT_BUTTON, self.buttonPressClear, self.theButtonClear)

        self.pnl.SetSizerAndFit(self.row)
        self.Show(True)

    def buttonPressAdd(self, event):
        try:
            num1 = int(self.number1.Value)
            num2 = int(self.number2.Value)
            self.result = num1 + num2
            self.answer.Label = str(self.result)
            self.number1.Value = ""
            self.number2.Value = ""

        except ValueError:
            wx.MessageBox("Enter 2 numbers")
            self.number1.Value = ""
            self.number2.Value = ""
            self.answer.Label = ""

    def buttonPressMinus(self, event):
        try:
            num1 = int(self.number1.Value)
            num2 = int(self.number2.Value)
            self.result = num1 - num2
            self.answer.Label = str(self.result)
            self.number1.Value = ""
            self.number2.Value = ""

        except ValueError:
            wx.MessageBox("Enter 2 numbers")
            self.number1.Value = ""
            self.number2.Value = ""
            self.answer.Label = ""

    def buttonPressTime(self, event):
        try:
            num1 = int(self.number1.Value)
            num2 = int(self.number2.Value)
            self.result = num1 * num2
            self.answer.Label = str(self.result)
            self.number1.Value = ""
            self.number2.Value = ""

        except ValueError:
            wx.MessageBox("Enter 2 numbers")
            self.number1.Value = ""
            self.number2.Value = ""
            self.answer.Label = ""

    def buttonPressDivide(self, event):
        try:
            num1 = int(self.number1.Value)
            num2 = int(self.number2.Value)
            self.result = num1 / num2
            self.answer.Label = str(self.result)
            self.number1.Value = ""
            self.number2.Value = ""

        except ValueError:
            wx.MessageBox("Enter 2 numbers")
            self.number1.Value = ""
            self.number2.Value = ""
            self.answer.Label = ""

    def buttonPressClear(self, event):
        self.number1.Value = ""
        self.number2.Value = ""
        self.answer.Label = ""


app = wx.App()
frame = Calulator(None, -1,'My Calculator')

app.MainLoop()
