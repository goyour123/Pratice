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
        self.axes = fig.add_subplot(111)

        self.iris = datasets.load_iris()
        self.iris_classes = ['Setosa', 'Versicolour', 'Virginica']
        self.marker_color = ['blue', 'red', 'green']
        self.instances_num = int(len(self.iris['data']) / len(self.iris_classes))
        self.iris_attr_idx = {
            'Sepel': (0, 1),
            'Petal': (2, 3)
        }

        super(MplCanvas, self).__init__(fig)

    def iris_plot(self, iris_class, attr_name):
        self.axes.cla()
        len_idx, width_idx = self.iris_attr_idx[attr_name]
        for idx, c in enumerate(self.iris_classes):
            if idx != 0 and iris_class != c:
                continue
            sepel_len = [d[len_idx] for d in self.iris['data'][self.instances_num * idx:self.instances_num * (idx + 1)]]
            sepel_width = [d[width_idx] for d in self.iris['data'][self.instances_num * idx:self.instances_num * (idx + 1)]]
            self.axes.scatter(sepel_len, sepel_width, color=self.marker_color[idx], marker='x', label=c)

        self.axes.set_xlabel(f'{attr_name} Length')
        self.axes.set_ylabel(f'{attr_name} Width')
        self.axes.legend()
        self.draw()

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Iris")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sc = MplCanvas(self, width=10, height=9, dpi=100)
        self.ui.verticalLayout.addWidget(self.sc)

        self.ui.actionIris_Sepel.triggered.connect(self.show_iris_sepel)
        self.ui.actionIris_Petal.triggered.connect(self.show_iris_petal)
        self.ui.comboBox.addItems(self.sc.iris_classes[1:3])

        self.sc.iris_plot(self.ui.comboBox.currentText(), 'Sepel')
        self.show()

    def show_iris_sepel(self):
        self.sc.iris_plot(self.ui.comboBox.currentText(), 'Sepel')

    def show_iris_petal(self):
        self.sc.iris_plot(self.ui.comboBox.currentText(), 'Petal')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()
