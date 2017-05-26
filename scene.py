#!/usr/bin/env python3
from math import sin,cos
from PyQt5.QtCore import (
        QPointF, Qt)
from PyQt5.QtGui import (
    QColor
    )
from PyQt5.QtWidgets import (
        QGraphicsScene
        )

#import animatedtiles_rc
from axis import Axis
from wave import Wave

class Scene(QGraphicsScene):

    functions = [
        {"wave":Wave(eval('lambda d: sin(d)'),QColor(0,0,255))},
        {"wave":Wave(eval('lambda d: cos(d)'),QColor(255,128,0))},
        {"wave":Wave(eval('lambda d: sin(4*d)*-2.5'),QColor(0,128,128))},
        {"wave":Wave(eval('lambda d: cos(4*d)*0.5'),QColor(0,128,128))},
    ]

    def addWave(self,wave,cp):
        self.addItem(wave)
        wave.setPos(wave.pos()-cp)

    def makeWaves(self,cp):
        [self.addWave(fn['wave'],cp) for fn in Scene.functions]

    def __init__(self):
        super(Scene,self).__init__(-350, -350, 900, 700)
        self.incStep = 5
        cp = QPointF(300,0)
        self.makeWaves(cp)
        self.axis = Axis(QColor(0,0,0))
        self.addItem(self.axis) 
        self.axis.setPos(self.axis.pos()-cp)

    def resizeEvent(self, event):
        super(Scene, self).resizeEvent(event)
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)

    def updateTick(self):
        [fn["wave"].nextStep(self.incStep) for fn in Scene.functions]
        self.update()
