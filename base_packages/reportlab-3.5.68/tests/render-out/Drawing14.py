#Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.shapes import _DrawingEditorMixin, Drawing, Group, Image
from reportlab.lib.colors import Color, CMYKColor, PCMYKColor

class ExplodedDrawing_Drawing(_DrawingEditorMixin,Drawing):
	def __init__(self,width=400,height=200,*args,**kw):
		Drawing.__init__(self,width,height,*args,**kw)
		self.transform = (1,0,0,1,0,0)
		self.add(Image(0,0,None,None,<PIL.GifImagePlugin.GifImageFile image mode=P size=10x7 at 0x7F093687C610>,fillColor=Color(0,0,0,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Image(380,186,20,14,<PIL.GifImagePlugin.GifImageFile image mode=P size=10x7 at 0x7F093687C7F0>,fillColor=Color(0,0,0,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))


if __name__=="__main__": #NORUNTESTS
	ExplodedDrawing_Drawing().save(formats=['pdf'],outDir='.',fnRoot=None)
