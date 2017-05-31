from PyQt5.QtCore import (
    Qt
)
from PyQt5.QtGui import (
    QPainter
)
from PyQt5.QtWidgets import (
    QGraphicsView
)

class View(QGraphicsView):
    def __init__(self,scene,title):
        super(View,self).__init__(scene)
        self.setWindowTitle(title)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    def resizeEvent(self, event):
        super(View, self).resizeEvent(event)
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)
