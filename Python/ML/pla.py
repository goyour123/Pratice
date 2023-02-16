import sys
import numpy
import matplotlib
matplotlib.use("Qt5Agg")

from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from sklearn import datasets
from pla_ui import Ui_MainWindow

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=7, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi, linewidth=1)
        self.axes = fig.add_subplot(211)
        self.axes2 = fig.add_subplot(212)

        iris = datasets.load_iris()
        iris_classes = ['Setosa', 'Versicolour', 'Virginica']
        marker_color = ['blue', 'red', 'green']
        instances_num = int(len(iris['data']) / len(iris_classes))

        for idx, iris_class in enumerate(iris_classes):
            sepel_len = [d[0] for d in iris['data'][instances_num*idx:instances_num*(idx+1)]]
            sepel_width = [d[1] for d in iris['data'][instances_num*idx:instances_num*(idx+1)]]
            self.axes.scatter(sepel_len, sepel_width, color=marker_color[idx], marker='x', label=iris_class)

        self.axes.set_xlabel('Sepel Length')
        self.axes.set_ylabel('Sepel Width')
        self.axes.legend()


        for idx, iris_class in enumerate(iris_classes):
            petal_len = [d[2] for d in iris['data'][instances_num*idx:instances_num*(idx+1)]]
            petal_width = [d[3] for d in iris['data'][instances_num*idx:instances_num*(idx+1)]]
            self.axes2.scatter(petal_len, petal_width, color=marker_color[idx], marker='x',  label=iris_class)

        self.axes2.set_xlabel('Petal Length')
        self.axes2.set_ylabel('Petal Width')
        self.axes2.legend()

        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.sc = MplCanvas(self, width=10, height=9, dpi=100)
        self.ui.verticalLayout.addWidget(self.sc)
        self.setWindowTitle("Iris")
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()
