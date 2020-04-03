#import tensorflow as tf
#import os
#import numpy as np
#with tf.session() as session:
#        x=tf.placeholder(tf.float32,[1],name="x")
#        y=tf.placeholder(tf.float32,[1],name="y")
#        z=tf.constant(1.0)
#        y=x * z
#        x_in=[100]
#        y_output=session.run(y,{x:x_in})
#        print(y_output)   
#scalar=tf.constant(100)
#vector=tf.constant([1,2,3,4,5])
#matrix=tf.constant([[1,2,3],[4,5,6]])
#cube_matrix=tf.constant([[[1],[2],[3]],[[4],[5],[6]],[[7],[8],[9]]]) 

#scalar.get_shape()
#print(scalar.get_shape())
#print(vector.get_shape())
#print(matrix.get_shape())
#print(cube_matrix.get_shape())
#tensor_ld=np.array([1,2,3,4,5,6,7,8,9,10])
#tensor_ld=tf.constant(tensor_ld)
#with tf.session() as sess:
#    print (tensor_ld.get_shape())
#    print (sess.run(tensor_ld))
#import wx
#import wx.xrc
#import basewin
#class MianWindow(basewin.MyFrame1):
#    # 咱们给个初始化函数，将文本框初始填有‘主窗口测试’几个字
#    # 不能直接覆盖原有__ini__方法，这样会导致窗体启动失败。咱们新建一个，然后再调用
#    def init_main_window(self):
#        self.m_textCtrl1.SetValue('主窗口测试')
#    # 将点击按钮清空文本框的,功能写成函数
#    def main_button_click(self, event):
#        self.m_textCtrl1.Clear()
#if __name__ == '__main__':
#    app = wx.App()
#    # None表示的是此窗口没有上级父窗体。如果有，就直接在父窗体代码调用的时候填入‘self’就好了。
#    main_win = MianWindow(None)
#    main_win.init_main_window()
#    main_win.Show()
#    app.MainLoop()

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import wx
import wx.xrc
import os 


class MyFrame2 ( wx.Frame ):

	def __init__( self, image,parent=None,path=''):
		wx.Frame.__init__ ( self, parent, id = -1, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000,618 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
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
		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )

		m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2.Add( m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
		self.bmp = wx.StaticBitmap(m_panel3, bitmap=temp)
		#self.SetClientSize(size)

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
		    image=wx.Image(path,wx.BITMAP_TYPE_JPEG)
		    self.bmp.SetBitmap(wx.BitmapFromImage(image))
		dialog.Destroy()


	def saveResult( self, event ):
		event.Skip()

class App(wx.App):
    def OnInit(self):
        image=wx.Image('test.png',wx.BITMAP_TYPE_JPEG)
        self.frame=MyFrame2(image)
        self.frame.Show()
        return True
#if __name__ == '__main__':
#    app = wx.App()
  
#    main_win = MyFrame2(None)
#    main_win.Show()

#    app.MainLoop()
#if __name__=='__main__':
#    app=App()
#    app.MainLoop()
