# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os 
import module5 as vggtest


###########################################################################
## Class MyFrame2
###########################################################################
pathD='blank.jpg'
path=''
file_name=''
class MyFrame2 ( wx.Frame ):

	def __init__( self, image,parent=None,path=''):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 810,335 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		temp=image.ConvertToBitmap()
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer4.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"打开", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button4, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button5, 0, wx.ALL, 5 )
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"识别", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,50 ), wx.TE_READONLY )
		bSizer4.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,200 ), wx.TE_READONLY )
		bSizer4.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )

		m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2.Add( m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
		self.bmp = wx.StaticBitmap(m_panel3, bitmap=temp)


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button4.Bind( wx.EVT_BUTTON, self.openImage )
		self.m_button5.Bind( wx.EVT_BUTTON, self.saveResult )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def openImage( self, event ):
	    wildcard = "j(*.png)|*.png|All files(*.*)|*.*"
	    dialog = wx.FileDialog(self, "Choose a file", os.getcwd(), "", wildcard, wx.FD_OPEN)
	    if dialog.ShowModal() == wx.ID_OK:
	        path = dialog.GetPath()
	        file_name = dialog.GetFilename()
	        image=wx.Image(path,wx.BITMAP_TYPE_JPEG)
	        self.bmp.SetBitmap(wx.BitmapFromImage(image))
	    dialog.Destroy()
	    if(path!=pathD):
	        self.m_textCtrl5.SetValue(file_name)

	def saveResult( self, event ):
		event.Skip()
#class App(wx.App):
#    def OnInit(self):
#        image=wx.Image('test.png',wx.BITMAP_TYPE_JPEG)
#        self.frame=MyFrame2(image)
#        self.frame.Show()
#        return True
def main(path):
    app=wx.App()
    #if(path!=None):
    image=wx.Image(path,wx.BITMAP_TYPE_JPEG)
    win=MyFrame2(image)
    #else:
    #    mage=wx.Image(pathb,wx.BITMAP_TYPE_JPEG)
    #    win=MyFrame2(imageb)
    win.Show()
    app.MainLoop()
if __name__=='__main__':
    main(pathD)

