#Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.shapes import _DrawingEditorMixin, Drawing, Group, Wedge
from reportlab.lib.colors import Color, CMYKColor, PCMYKColor

class ExplodedDrawing_Drawing(_DrawingEditorMixin,Drawing):
	def __init__(self,width=400,height=200,*args,**kw):
		Drawing.__init__(self,width,height,*args,**kw)
		self.transform = (1,0,0,1,0,0)
		self.add(Wedge(200,100,75,-176.4,90,yradius=75,annular=False,fillColor=Color(.27451,.509804,.705882,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=1,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Wedge(200,100,75,-180,-176.4,yradius=75,annular=False,fillColor=Color(.847059,.74902,.847059,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=1,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Wedge(200,100,75,-270,-180,yradius=75,annular=False,fillColor=Color(.392157,.584314,.929412,1),fillOpacity=None,strokeColor=Color(0,0,0,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=1,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))


if __name__=="__main__": #NORUNTESTS
	ExplodedDrawing_Drawing().save(formats=['pdf'],outDir='.',fnRoot=None)