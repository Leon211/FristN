
import wx
 
if __name__ == "__main__":
    app = wx.App()
    dialog = wx.DirDialog(None, "Choose a directory:",
          style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
        print(path)
        wx.Execute("explorer "+path) #打开所选目录
    dialog.Destroy()