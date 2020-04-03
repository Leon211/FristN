import wx
class Frame(wx.Frame):
    """Frame class that displays an image."""
    def __init__(self, image, parent=None, id=-1,
                 pos=wx.DefaultPosition, title='Hello, wxPython!'):
        """Create a Frame instance and display image."""
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        panel = wx.Panel(self)
        self.bmp = wx.StaticBitmap(parent=panel, bitmap=temp)
        self.SetClientSize(size)
class App(wx.App):
    """Application class."""
    def OnInit(self):
        # create a image object
        image = wx.Image('test.png', wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
def main():
    app = App()
    app.MainLoop()
if __name__ == '__main__':
    main()

