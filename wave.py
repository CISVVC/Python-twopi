#!/usr/bin/env python3
import math

from PyQt5.QtCore import (pyqtProperty, pyqtSignal, QEasingCurve, QObject,
        QParallelAnimationGroup, QPointF, QPropertyAnimation, qrand, QRectF,
        QState, QStateMachine, Qt, QTimer)
from PyQt5.QtGui import (QBrush, QLinearGradient, QPainter, QPainterPath,
        QPixmap)
from PyQt5.QtWidgets import (QApplication, QGraphicsItem, QGraphicsPixmapItem,
        QGraphicsRectItem, QGraphicsScene, QGraphicsView, QGraphicsWidget,
        QStyle)

class Wave(QGraphicsItem):

    BoundingRect = QRectF(0,0,100,100)

    def __init__(self,fn,color):
        super(Wave,self).__init__()
        self.fn = fn
        self.color = color
        self.xres = 2 
        self.yres = 100
        self.currentTick = 0
        self.curve = self.getCurve()
        self.setFlag(QGraphicsItem.ItemIsMovable, True);
        self.setFlag(QGraphicsItem.ItemIsSelectable, True);

    def getCurve(self):
       qp = QPainterPath()
       lastPoint = QPointF(0.0,0.0)
       for d in range(360):
           qp.moveTo(lastPoint)
           nextPoint = QPointF(self.xres * d,-1*self.yres * self.fn(d*math.pi/180.0))
           qp.lineTo(nextPoint)
           lastPoint = nextPoint

       return qp 

    def nextStep(self,inc):
        if self.currentTick  < 360:
            self.currentTick +=inc
        else:
            self.currentTick = 0


    def boundingRect(self):
        return Wave.BoundingRect

    def getRad(self):
        return self.currentTick * math.pi / 180.0 

    def unitCircle(self,cp):
        ticksize = 3
        m_radius = 10
        qp = QPainterPath()
        qp.addEllipse(cp,m_radius,m_radius)
        points = []
        # 0
        points.append((
                QPointF(m_radius-ticksize,0),
                QPointF(m_radius+ticksize,0)
                          ))
        #pi/4
        points.append((
                            QPointF(m_radius*math.cos(math.pi/4)-ticksize,-m_radius*math.sin(math.pi/4)+ticksize),
                            QPointF(m_radius*math.cos(math.pi/4)+ticksize,-m_radius*math.sin(math.pi/4)-ticksize)
                          ))
        # pi/2
        points.append( (
                        QPointF(0,-m_radius-ticksize),
                        QPointF(0,-m_radius+ticksize)
                          ))
        # 3pi/4
        points.append((
                QPointF(m_radius*math.cos(3*math.pi/4)-ticksize,-m_radius*math.sin(math.pi/4)-ticksize),
                QPointF(m_radius*math.cos(3*math.pi/4)+ticksize,-m_radius*math.sin(math.pi/4)+ticksize)
                          ))
        # 180
        points.append((
                QPointF(-m_radius-ticksize,0),
                QPointF(-m_radius+ticksize,0)
                          ))
        # 3pi/2
        points.append((
            QPointF(0,m_radius-ticksize),
            QPointF(0,m_radius+ticksize)
                          ))
        # 3pi/2
        points.append((
            QPointF(m_radius*math.cos(5*math.pi/4)-ticksize,-m_radius*math.sin(5*math.pi/4)+ticksize),
            QPointF(m_radius*math.cos(5*math.pi/4)+ticksize,-m_radius*math.sin(5*math.pi/4)-ticksize)
                          ))
        # 7pi/4
        points.append((
                QPointF(m_radius*math.cos(7*math.pi/4)-ticksize,-m_radius*math.sin(7*math.pi/4)-ticksize),
                QPointF(m_radius*math.cos(7*math.pi/4)+ticksize,-m_radius*math.sin(7*math.pi/4)+ticksize)
                          ))

       # build the tick marks
        for pair in points:
            qp.moveTo(cp+pair[0])
            qp.lineTo(cp+pair[1])

        qp.addEllipse(cp,2,2)

        return qp

    def paint(self,painter,option,widget):
        radius = 100
        c_size = 5
        rad = self.getRad()
        painter.setPen(self.color)
        painter.drawPath(self.curve)

        painter.setPen(Qt.red)
        cp = QPointF(self.xres*self.currentTick,-self.yres*self.fn(rad))
        painter.drawPath(self.unitCircle(cp))
        #drawCircle(painter,cp)
        painter.drawLine(cp,cp+QPointF(40*math.cos(rad),-40*math.sin(rad)))
        painter.setBrush(Qt.blue)
        painter.drawEllipse(cp+QPointF(40*math.cos(rad),-40*math.sin(rad)),c_size,c_size)
    