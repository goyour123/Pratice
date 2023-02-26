import sys
import numpy
import matplotlib
matplotlib.use("Qt5Agg")

from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from sklearn import datasets
from pla_ui import Ui_MainWindow


class IrisDataset ():
    def __init__ (self):
        self.iris = datasets.load_iris()
        self.iris_classes = ['Setosa', 'Versicolour', 'Virginica']
        self.instances_num = int(len(self.iris['data']) / len(self.iris_classes))

        self.iris_scatter_dict, self.iris_dataset_dict = {}, {'sepel': {}, 'petal': {}}
        for idx, c in enumerate(self.iris_classes):
            sepel_len = [d[0] for d in self.iris['data'][self.instances_num * idx:self.instances_num * (idx + 1)]]
            sepel_width = [d[1] for d in self.iris['data'][self.instances_num * idx:self.instances_num * (idx + 1)]]
            petal_len = [d[2] for d in self.iris['data'][self.instances_num * idx:self.instances_num * (idx + 1)]]
            petal_width = [d[3] for d in self.iris['data'][self.instances_num * idx:self.instances_num * (idx + 1)]]
            self.iris_scatter_dict.update({c: {'sepel_len': sepel_len, 'sepel_width': sepel_width, 'petal_len': petal_len, 'petal_width': petal_width}})
            self.iris_dataset_dict['sepel'].update({c: list(zip(sepel_len, sepel_width))})
            self.iris_dataset_dict['petal'].update({c: list(zip(petal_len, petal_width))})

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=7, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi, linewidth=1)
        self.axes = fig.add_subplot(111)
        self.iris_dataset = IrisDataset()
        self.marker_color = ['blue', 'green', 'red']
        self.select_class = []
        self.select_attr = ''
        self._perceptron_count = 0
        super(MplCanvas, self).__init__(fig)

    def iris_plot(self, iris_class, attr_name):
        self.axes.cla()
        self._perceptron_count = 0
        self.select_class = ['Setosa', iris_class]
        self.select_attr = attr_name

        attr_len, attr_width = self.select_attr.lower() + '_len', self.select_attr.lower() + '_width'
        length, width = self.iris_dataset.iris_scatter_dict['Setosa'][attr_len], self.iris_dataset.iris_scatter_dict['Setosa'][attr_width]
        self.axes.scatter(length, width, color=self.marker_color[0], marker='x', label='Setosa')

        length, width = self.iris_dataset.iris_scatter_dict[iris_class][attr_len], self.iris_dataset.iris_scatter_dict[iris_class][attr_width]
        self.axes.scatter(length, width, color=self.marker_color[1], marker='x', label=iris_class)

        self.axes.set_xlabel(f'{self.select_attr} Length')
        self.axes.set_ylabel(f'{self.select_attr} Width')
        self.axes.legend()
        self.draw()

    def perceptron_plot(self):
        self._perceptron_count += 1

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
        self.ui.comboBox.addItems(self.sc.iris_dataset.iris_classes[1:3])

        self.sc.iris_plot(self.ui.comboBox.currentText(), 'Petal')
        self.show()

    def show_iris_sepel(self):
        self.sc.iris_plot(self.ui.comboBox.currentText(), 'Sepel')

    def show_iris_petal(self):
        self.sc.iris_plot(self.ui.comboBox.currentText(), 'Petal')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()
