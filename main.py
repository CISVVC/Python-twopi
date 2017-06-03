#!/usr/bin/env python3

from PyQt5.QtWidgets import (
    QApplication
)
from PyQt5.QtGui import (
        QIcon
)
import resources_qrc

from mainwindow import Window as MainWindow

if __name__ == '__main__':

    import sys
    import math

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('pi-symbol.png'))

    window = MainWindow()
    window.show()


    sys.exit(app.exec_())
