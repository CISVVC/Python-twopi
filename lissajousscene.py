#!/usr/bin/env python3
from PyQt5.QtCore import (
        QPointF, Qt,QTimer)
from PyQt5.QtGui import (
    QColor
    )
from PyQt5.QtWidgets import (
        QGraphicsScene
        )

#import animatedtiles_rc
from axis import Axis
from lissajous import Curve
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
#            {"wave":Curve('lambda t,a,b,d: (sin(a*t+d),sin(b*t))',QColor(0,0,255))},
            {"wave":Curve('(sin(3*t+pi/2),sin(4*t))',QColor(255,0,0),1)},
            {"wave":Curve('(sin(5*t+pi/2),sin(6*t))',QColor(0,255,0),1)},
            {"wave":Curve('(sin(7*t+pi/2),sin(8*t))',QColor(0,0,255),1)},
            {"wave":Curve('(sin(11*t+pi/2),sin(12*t))',QColor(255,0,0),1)},
            {"wave":Curve('(sin(13*t+pi/2),sin(14*t))',QColor(0,255,0),1)},
            {"wave":Curve('(sin(15*t+pi/2),sin(16*t))',QColor(0,0,255),1)},
            # {"wave":Curve('lambda t,a,b,d: (sin(9*t+d),sin(10*t))',QColor(0,255,0))},
            # {"wave":Curve('lambda t,a,b,d: (sin(9*t+d),sin(10*t))',QColor(0,0,255))},
            # {"wave":Curve('lambda t,a,b,d: (sin(9*t+d),sin(10*t))',QColor(255,0,0))},
            # {"wave":Curve('lambda t,a,b,d: (sin(9*t+d),sin(10*t))',QColor(0,255,0))},
            # {"wave":Curve('lambda t,a,b,d: (sin(9*t+d),sin(10*t))',QColor(0,0,255))},
            # {"wave":Curve('lambda t,a,b,d: (sin(9*t+d),sin(10*t))',QColor(255,0,0))},
            # {"wave":Curve('lambda t,a,b,d: (sin(9*t+d),sin(10*t))',QColor(0,255,0))},
            # {"wave":Curve('lambda t,a,b,d: (sin(9*t+d),sin(10*t))',QColor(0,0,255))},
            # {"wave":Curve('lambda t,a,b,d: (sin(9*t+d),sin(10*t))',QColor(255,0,0))},
            # {"wave":Curve('lambda t,a,b,d: (sin(9*t+d),sin(10*t))',QColor(0,255,0))},
            # {"wave":Curve('lambda t,a,b,d: (sin(9*t+d),sin(10*t))',QColor(0,0,255))},
            #{"wave":Curve('lambda t,a,b,d: (sin(3*t+d),sin(4*t))',QColor(0,255,255))},
            #{"wave":Curve('lambda t,a,b,d: (sin(t+d),sin(t))',QColor(255,0,255))},
        ]
        self.incStep = 1
        cp = QPointF(300,0)
        self.makeWaves(cp)
        self.axis = Axis(QColor(0,0,0))
        self.unitcircle = UnitCircle(Qt.blue)
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
