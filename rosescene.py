#!/usr/bin/env python3
from PyQt5.QtCore import (
        QPointF, Qt,QTimer)
from PyQt5.QtGui import (
    QColor
    )
from PyQt5.QtWidgets import (
        QGraphicsScene,QGraphicsItem
        )

#import animatedtiles_rc
from axis import Axis
from rose import Curve
from unitcircle import UnitCircle
from legend import Legend

class Scene(QGraphicsScene):


    def addWave(self,wave,cp):
        self.addItem(wave)
        #wave.setPos(wave.pos()-cp)
        #wave.setPos(QPointF(-300,0))

    def makeWaves(self,cp):
        [self.addWave(fn['wave'],cp) for fn in self.functions]

    def __init__(self):
        super(Scene,self).__init__(-350, -350, 900, 700)
        self.functions = [
            {"wave":Curve('(cos(2*d)*cos(d),cos(2*d)*sin(d))',QColor(0,255,255),2)},
            {"wave":Curve('(cos(3/2.0*d)*cos(d),cos(3/2.0*d)*sin(d))',QColor(128,0,255),2)},
            {"wave":Curve('(cos(7/8.0*d)*cos(d),cos(7/8.0*d)*sin(d))',QColor(0,0,255),8)},
            {"wave":Curve('(cos(3/4.0*d)*cos(d),cos(3/4.0*d)*sin(d))',QColor(255,0,0),4)},
            {"wave":Curve('(cos(3/8.0*d)*cos(d),cos(3/8.0*d)*sin(d))',QColor(0,255,0),8)},
            {"wave":Curve('(cos(1/3.0*d)*cos(d),cos(1/3.0*d)*sin(d))',QColor(0,0,255),2)},
        ]
        self.incStep = 5
        cp = QPointF(300,0)
        self.makeWaves(cp)
        self.axis = Axis(QColor(0,0,0))
        self.unitcircle = UnitCircle(Qt.blue)
        self.unitcircle.setFlag(QGraphicsItem.ItemIsMovable, True);
        self.unitcircle.setFlag(QGraphicsItem.ItemIsSelectable, True);
        self.addItem(self.unitcircle)
        self.unitcircle.setPos(QPointF(-300,-275))
        self.legend = Legend(self.functions)
        #self.addItem(self.legend)
        self.legend.setPos(QPointF(-200,-350))
        #self.addItem(self.axis) 
        #self.axis.setPos(self.axis.pos()-cp)
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTick)
        self.timer.start(50)

    def resizeEvent(self, event):
        super(Scene, self).resizeEvent(event)
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)

    def updateTick(self):
        [fn["wave"].nextStep(self.incStep) for fn in self.functions]
        self.unitcircle.nextStep(self.incStep)
        self.update()
