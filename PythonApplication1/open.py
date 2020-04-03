def openImage( self, event ):
		dialog = wx.DirDialog(None, "Choose a directory:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
		if dialog.ShowModal() == wx.ID_OK:
		    path = dialog.GetPath()
		    dialog.Destroy()

	def saveResult( self, event ):
		event.Skip()
