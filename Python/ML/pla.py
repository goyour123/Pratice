import numpy
import matplotlib
matplotlib.use("Qt5Agg")

from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from sklearn import datasets
import sys

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=7, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi, linewidth=1)
        self.axes = fig.add_subplot(211)
        self.axes2 = fig.add_subplot(212)
        
        iris = datasets.load_iris()
        iris2 = datasets.load_iris()
        
        sepelLen = [d[0] for d in iris['data'][:50]]
        sepelWidth = [d[1] for d in iris['data'][:50]]
        self.axes.scatter(sepelLen, sepelWidth, marker='x')

        sepelLen = [d[0] for d in iris['data'][50:100]]
        sepelWidth = [d[1] for d in iris['data'][50:100]]
        self.axes.scatter(sepelLen, sepelWidth, marker='o')

        sepelLen = [d[0] for d in iris['data'][100:150]]
        sepelWidth = [d[1] for d in iris['data'][100:150]]
        self.axes.scatter(sepelLen, sepelWidth, marker='^')

        self.axes.set_xlabel('Sepel Length')
        self.axes.set_ylabel('Sepel Width')

        sepelLen = [d[2] for d in iris['data'][:50]]
        sepelWidth = [d[3] for d in iris['data'][:50]]
        self.axes2.scatter(sepelLen, sepelWidth, marker='x')

        sepelLen = [d[2] for d in iris['data'][50:100]]
        sepelWidth = [d[3] for d in iris['data'][50:100]]
        self.axes2.scatter(sepelLen, sepelWidth, marker='o')

        sepelLen = [d[2] for d in iris['data'][100:150]]
        sepelWidth = [d[3] for d in iris['data'][100:150]]
        self.axes2.scatter(sepelLen, sepelWidth, marker='^')

        self.axes2.set_xlabel('Petal Length')
        self.axes2.set_ylabel('Petal Width')

        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(sc)
        self.setWindowTitle("Iris")
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()
