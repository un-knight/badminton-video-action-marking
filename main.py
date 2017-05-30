"""
author: Junxian Ye
time:
link:
"""
import sys
from player import *


if __name__ == '__main__':
    player = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(player.exec_())