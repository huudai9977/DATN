import wx


class MyForm(wx.Frame):

    # ----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Camera history")

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        self.index = 0

        self.list_ctrl = wx.ListCtrl(panel, size=(-1, 400),
                                     style=wx.LC_REPORT
                                           | wx.BORDER_SUNKEN
                                     )
        self.list_ctrl.InsertColumn(0, 'STT')
        self.list_ctrl.InsertColumn(1, 'Name',width=105)
        self.list_ctrl.InsertColumn(2, 'Time', width=205)
        with open('history.csv', 'r+') as f:
            myDataList = f.readlines()
            for line in myDataList:
                entry = line.split(',')  # tách theo dấu ,
                line = "%s" % self.index
                self.list_ctrl.InsertItem(self.index, line)
                self.list_ctrl.SetItem(self.index, 1, entry[0])
                self.list_ctrl.SetItem(self.index, 2, entry[-1])
                self.index += 1
        btnClose = wx.Button(panel, label="Close")
        btnClose.Bind(wx.EVT_BUTTON, self.close)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(btnClose, 0, wx.ALIGN_RIGHT | wx.RIGHT , 5)
        panel.SetSizer(sizer)

    # ----------------------------------------------------------------------
    def close(self,event):
        wx.Exit()


# ----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()