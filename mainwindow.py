#!/usr/bin/env python3

from PyQt5.QtCore import (
    Qt
)
from PyQt5.QtGui import (
    QPainter,
    QIcon
)
from PyQt5.QtWidgets import (
    QAction,
    QMenuBar,
    QMainWindow
)

from view import View
from wavescene import Scene as WaveScene
from rosescene import Scene as RoseScene
from lissajousscene import Scene as LissajousScene

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        scene = WaveScene()
        self.view = View(scene,"Animated 2Pi")
        self.setCentralWidget(self.view)
        self.initUI()


    def initUI(self):

        exitAction = QAction(QIcon(':/assets/images/exit24.png'), 'App Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)


        self.statusBar()

        self.menubar = self.menuBar()
        #print(self.menubar.isNativeMenuBar())
        self.menubar.setNativeMenuBar(False)
        #print(self.menubar.isNativeMenuBar())
        self.fileMenu = self.menubar.addMenu('&File')
        self.fileMenu.addAction(exitAction)
        self.newMenu = self.menubar.addMenu('&Scene')
        sineWaveAction = QAction(QIcon(':/assets/images/tile.png'), 'Sine Waves', self)
        sineWaveAction.setStatusTip('Trig Waves')
        sineWaveAction.triggered.connect(self.sineWaveScene)
        self.newMenu.addAction(sineWaveAction)
        roseAction = QAction(QIcon(':/assets/images/tile.png'), 'Roses', self)
        roseAction.setStatusTip('Roses')
        roseAction.triggered.connect(self.roseScene)
        self.newMenu.addAction(roseAction)
        lissajousAction = QAction(QIcon(':/assets/images/tile.png'), 'Lissajous', self)
        lissajousAction.setStatusTip('Lissajous')
        lissajousAction.triggered.connect(self.lissajousScene)
        self.newMenu.addAction(lissajousAction)
        self.setWindowTitle("Sine Waves")

    def sineWaveScene(self):
        scene = WaveScene()
        self.view.setScene(scene)
        self.setWindowTitle("Sine Waves")

    def roseScene(self):
        scene = RoseScene()
        self.view.setScene(scene)
        self.setWindowTitle("Rose or Rhodonea Curves")

    def lissajousScene(self):
        scene = LissajousScene()
        self.view.setScene(scene)
        self.setWindowTitle("Lissajous Curves")
