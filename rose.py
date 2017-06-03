#!/usr/bin/env python3
from math import sin,cos,pi

from PyQt5.QtCore import (
        QPointF, 
        QRectF,
        Qt, 
        QTimer
)
from PyQt5.QtGui import (
    QBrush, 
    QPainter, 
    QPainterPath,
    QPixmap
)
from PyQt5.QtWidgets import (
    QGraphicsItem, 
    QGraphicsScene
)

class Curve(QGraphicsItem):

    BoundingRect = QRectF(-100,-100,200,200)

    def __init__(self,fn,color,periods):
        super(Curve,self).__init__()
        self.fnText = fn
        self.fn = eval('lambda d: '+fn)
        self.color = color
        self.xres = 100 
        self.yres = 100
        self.currentTick = 0
        self.periods = periods 
        self.curve = self.getCurve()
        self.setFlag(QGraphicsItem.ItemIsMovable, True);
        self.setFlag(QGraphicsItem.ItemIsSelectable, True);

    def getCurve(self):
       qp = QPainterPath()
       r = self.fn(0)
       lastPoint = QPointF(self.xres * r[0],-1*self.yres * r[1])
       for d in range(self.periods*360):
           qp.moveTo(lastPoint)
           r = self.fn(d*pi/180.0)
           nextPoint = QPointF(self.xres * r[0],-1*self.yres * r[1])
           qp.lineTo(nextPoint)
           lastPoint = nextPoint

       return qp 

    def nextStep(self,inc):
        if self.currentTick  < self.periods*360:
            self.currentTick +=inc
        else:
            self.currentTick = 0


    def boundingRect(self):
        return Curve.BoundingRect

    def getRad(self):
        return self.currentTick * pi / 180.0 

    def unitCircle(self,m_radius,cp,ticksize):
        qp = QPainterPath()
        qp.addEllipse(cp,m_radius,m_radius)
        points = [

            # 0
            (
                QPointF(m_radius-ticksize,0),
                QPointF(m_radius+ticksize,0)
            ),
            #pi/4
            (
                QPointF(m_radius*cos(pi/4)-ticksize,
                        -m_radius*sin(pi/4)+ticksize),
                QPointF(m_radius*cos(pi/4)+ticksize,
                        -m_radius*sin(pi/4)-ticksize)

            ),
            (
                QPointF(0,-m_radius-ticksize),
                QPointF(0,-m_radius+ticksize)
            ),
            # 3pi/4
            (
                QPointF(m_radius*cos(3*pi/4)-ticksize,
                        -m_radius*sin(pi/4)-ticksize),
                QPointF(m_radius*cos(3*pi/4)+ticksize,
                       -m_radius*sin(pi/4)+ticksize)
            ),
            # 180
            (
                QPointF(-m_radius-ticksize,0),
                QPointF(-m_radius+ticksize,0)

            ),
            # 3pi/2
            (
                QPointF(0,m_radius-ticksize),
                QPointF(0,m_radius+ticksize)
            ),
            (
                QPointF(m_radius*cos(5*pi/4)-ticksize,
                        -m_radius*sin(5*pi/4)+ticksize),
                QPointF(m_radius*cos(5*pi/4)+ticksize,
                       -m_radius*sin(5*pi/4)-ticksize)
            ),
            # 7pi/4
            (
                QPointF(m_radius*cos(7*pi/4)-ticksize,
                       -m_radius*sin(7*pi/4)-ticksize),
                QPointF(m_radius*cos(7*pi/4)+ticksize,
                       -m_radius*sin(7*pi/4)+ticksize)
            )
        ]

       # build the tick marks
        for pair in points:
            qp.moveTo(cp+pair[0])
            qp.lineTo(cp+pair[1])

        qp.addEllipse(cp,2,2)

        return qp

    def paint(self,painter,option,widget):
        radius = 15
        c_size =5 
        rad = self.getRad()
        painter.setPen(self.color)
        painter.drawPath(self.curve)

        painter.setPen(Qt.red)
        r = self.fn(rad)
        cp = QPointF(self.xres * r[0],-1*self.yres * r[1])
        #painter.drawPath(self.unitCircle(radius,cp,3))
        painter.drawLine(cp,cp+QPointF(radius*cos(rad),-radius*sin(rad)))
        painter.drawLine(cp,cp+QPointF(-radius*cos(rad),radius*sin(rad)))
        painter.setBrush(Qt.blue)
        painter.drawEllipse(cp+QPointF(radius*cos(rad),-radius*sin(rad)),c_size,c_size)
        painter.setBrush(Qt.red)
        painter.drawEllipse(cp+QPointF(-radius*cos(rad),radius*sin(rad)),c_size,c_size)
        painter.setPen(Qt.black)
        painter.drawText(QPointF(self.boundingRect().center().x(),self.boundingRect().bottom()+30),self.fnText)
    
