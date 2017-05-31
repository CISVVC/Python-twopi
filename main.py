#!/usr/bin/env python3

from PyQt5.QtWidgets import (
    QApplication
)

from view import View
from scene import Scene


if __name__ == '__main__':

    import sys
    import math

    app = QApplication(sys.argv)

    scene = Scene()
    view = View(scene,"Animated 2Pi")
    view.show()



    sys.exit(app.exec_())
