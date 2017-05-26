#!/usr/bin/env python3
from PyQt5.QtCore import (
    QTimer,Qt
)
from PyQt5.QtGui import (
    QPainter 
)
from PyQt5.QtWidgets import (
    QApplication,QGraphicsView
)

from scene import Scene


class View(QGraphicsView):
    def resizeEvent(self, event):
        super(View, self).resizeEvent(event)
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)


if __name__ == '__main__':

    import sys
    import math

    app = QApplication(sys.argv)

    scene = Scene()
    view = View(scene)
    view.setWindowTitle("Animated 2Pi")
    view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
    #view.setBackgroundBrush(QBrush(bgPix))
    view.setCacheMode(QGraphicsView.CacheBackground)
    view.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
    view.show()

    timer = QTimer()
    timer.timeout.connect(scene.updateTick)
    timer.start(100)


    sys.exit(app.exec_())
