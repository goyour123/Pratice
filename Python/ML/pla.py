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
        self.iris_attrs = ['Sepel', 'Petal']
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
        self.current_dataset = []
        self._perceptron_count = 0
        self.org_x, self.org_y = 0, 0
        super(MplCanvas, self).__init__(fig)

    def iris_plot(self, iris_classes, attr_name):
        self.axes.cla()
        self._perceptron_count = 0
        self.select_class = iris_classes
        self.select_attr = attr_name

        attr_len, attr_width = self.select_attr.lower() + '_len', self.select_attr.lower() + '_width'
        
        class_1 = iris_classes[0]
        length, width = self.iris_dataset.iris_scatter_dict[class_1][attr_len], self.iris_dataset.iris_scatter_dict[class_1][attr_width]
        self.axes.scatter(length, width, color=self.marker_color[0], marker='x', label=class_1)

        class_2 = iris_classes[1]
        length, width = self.iris_dataset.iris_scatter_dict[class_2][attr_len], self.iris_dataset.iris_scatter_dict[class_2][attr_width]
        self.axes.scatter(length, width, color=self.marker_color[1], marker='x', label=class_2)

        self.current_dataset = list(zip(self.iris_dataset.iris_dataset_dict[self.select_attr.lower()][class_1], [1] * self.iris_dataset.instances_num))
        self.current_dataset.extend(list(zip(self.iris_dataset.iris_dataset_dict[self.select_attr.lower()][class_2], [-1] * self.iris_dataset.instances_num)))

        self.axes.set_xlabel(f'{self.select_attr} Length')
        self.axes.set_ylabel(f'{self.select_attr} Width')
        self.axes.legend()
        self.draw()

    def check_sign(self, w):
        err_count, err_list = 0, []
        for p, sign in self.current_dataset:
            t = (p[0] - self.org_x, p[1] - self.org_y)
            t_sign = numpy.sign(numpy.dot(numpy.array(w), numpy.array(t)))
            if t_sign != numpy.sign(sign):
                err_count += 1
                err_list.append((p, sign))
        return err_count, err_list

    def perceptron_plot(self):
        if self._perceptron_count == 0:
            position, _sign = self.current_dataset[0]
            self.org_x = sum(t[0]for t, s in self.current_dataset) / (self.iris_dataset.instances_num * 2)
            self.org_y = sum(t[1]for t, s in self.current_dataset) / (self.iris_dataset.instances_num * 2)
            self.w_x, self.w_y = position[0] - self.org_x, position[1] - self.org_y
            slope = - (self.w_x) / (self.w_y)
            self.axes.axline((self.org_x, self.org_y), slope=slope)
            self.draw()
        else:
            err_count, err_list = self.check_sign((self.w_x, self.w_y))
            if err_count > 0:
                self.axes.lines[-1].remove()
                self.w_x, self.w_y = numpy.array(err_list[-1][0] - self.org_x, err_list[-1][1] - self.org_y) * err_list[-1][1] + numpy.array(self.w_x, self.w_y)
                slope = - (self.w_x) / (self.w_y)
                self.axes.axline((self.org_x, self.org_y), slope=slope)
                self.draw()
        self._perceptron_count += 1

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Iris")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sc = MplCanvas(self, width=10, height=9, dpi=100)
        self.ui.verticalLayout.addWidget(self.sc)

        self.ui.pushButton.clicked.connect(self.perceptron_button)
        self.ui.comboBox.addItems(self.sc.iris_dataset.iris_classes)
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox_2.addItems(self.sc.iris_dataset.iris_attrs)
        self.ui.comboBox_3.addItems(self.sc.iris_dataset.iris_classes)
        self.ui.comboBox_3.setCurrentIndex(1)
        self.ui.comboBox.currentTextChanged.connect(self.show_iris_plot)
        self.ui.comboBox_2.currentTextChanged.connect(self.show_iris_plot)
        self.ui.comboBox_3.currentTextChanged.connect(self.show_iris_plot)

        self.sc.iris_plot([self.ui.comboBox.currentText(), self.ui.comboBox_3.currentText()], self.ui.comboBox_2.currentText())
        self.show()

    def show_iris_plot(self):
        self.sc.iris_plot([self.ui.comboBox.currentText(), self.ui.comboBox_3.currentText()], self.ui.comboBox_2.currentText())

    def perceptron_button(self):
        self.sc.perceptron_plot()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()
