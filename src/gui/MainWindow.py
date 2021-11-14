from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, \
    QFileDialog, QLineEdit, QSlider, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import csv
import numpy


class GUIWindow(QWidget):
    def __init__(self):
        super(GUIWindow, self).__init__()
        self.criteria_number = 0
        self.alternative_number = 0
        self.criteria = []
        self.initGUI()

    def initGUI(self):
        self.setGeometry(200, 200, 500, 300)
        self.setWindowTitle("AHP-Ranking")
        self.setWindowIcon(QIcon('pathology.png'))
        self.setStyleSheet("background-color:#b8b8b8")
        self.title = QLabel(self)
        self.title.setText("Prosta aplikacja licząca ranking AHP")
        self.title.setStyleSheet("color:black; font-size:20px;text-transform:uppercase; text-align:center;")
        self.title.setGeometry(0, 10, 500, 50)
        self.title.setAlignment(Qt.AlignCenter)
        self.subtitle = QLabel(self)
        self.subtitle.setText("Wprowadź parametry:")
        self.subtitle.setStyleSheet("color:black; font-size:15px;text-transform:uppercase; text-align:center;")
        self.subtitle.setGeometry(0, 50, 500, 50)
        self.subtitle.setAlignment(Qt.AlignCenter)
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.param = QWidget(self)
        self.param.setGeometry(0, 100, 500, 150)
        self.param_layout = QGridLayout()
        self.param_layout.setColumnStretch(0, 0)
        self.param_title_1 = QLabel()
        self.param_title_1.setText("Liczba kryteriów:")
        self.param_title_1.setGeometry(10, 0, 200, 50)
        # self.param_title_1.setAlignment(Qt.AlignCenter)
        self.param_title_2 = QLabel(self.param)
        self.param_title_2.setText("Liczba alternatyw:")
        self.param_title_2.setGeometry(10, 20, 200, 50)
        # self.param_title_2.setAlignment(Qt.AlignCenter)
        self.param_edit_1 = QLineEdit(self.param)
        self.param_edit_1.setGeometry(0, 0, 100, 50)
        self.param_edit_2 = QLineEdit(self.param)
        self.param_edit_2.setGeometry(0, 0, 100, 50)
        self.param_layout.addWidget(self.param_title_1, 0, 0)
        self.param_layout.addWidget(self.param_edit_1, 0, 1)
        self.param_layout.addWidget(self.param_title_2, 1, 0)
        self.param_layout.addWidget(self.param_edit_2, 1, 1)
        self.param.setLayout(self.param_layout)
        self.load = QPushButton("Załaduj plik z danymi", self)
        self.load.setStyleSheet("background:#3f3f3f; color:#d1d1d1; text-transform:uppercase;")
        self.load.setGeometry(170, 250, 150, 30)
        self.load.clicked.connect(self.read_file)
        self.forward = QPushButton("Dalej", self)
        self.forward.setStyleSheet("background:#3f3f3f; color:#d1d1d1; text-transform:uppercase;")
        self.forward.setGeometry(170, 270, 150, 30)
        self.forward.clicked.connect(self.processing)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.subtitle)
        self.layout.addWidget(self.param)
        self.layout.addWidget(self.load)
        self.layout.addWidget(self.forward)
        self.setLayout(self.layout)
        self.show()

    def read_file(self):
        self.criteria_number = int(self.param_edit_1.text())
        self.alternative_number = int(self.param_edit_2.text())
        print("liczba kryterów: ", self.criteria_number)
        print("liczba alternatyw: ", self.alternative_number)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog.getOpenFileName(self, 'Open File', "")
        if file_name:
            print(file_name)
        reader = csv.reader(open(file_name[0], "rt"), delimiter=";")
        x = list(reader)
        result = numpy.array(x)
        c = self.criteria_number
        a = self.alternative_number
        criteria = result[0][0:c]
        print(criteria)
        alternatives = result[1][0:a]
        print(alternatives)
        matrixes = [[]] * c
        beg = 2
        for i in range(c):
            matrixes[i] = result[beg:beg + 6].astype("float")
            beg = beg + 6
            print(matrixes[i])

    def set_criteria_window(self):
        self.criteria_number = int(self.param_edit_1.text())
        self.alternative_number = int(self.param_edit_2.text())
        print("liczba kryterów: ", self.criteria_number)
        print("liczba alternatyw: ", self.alternative_number)
        print(self.criteria_number + self.alternative_number)
        self.setGeometry(200, 200, 800, 500)
        self.subtitle.setText("Wprowadź kryteria")
        self.title.setGeometry(0, 10, 800, 50)
        self.subtitle.setGeometry(0, 50, 800, 50)
        #self.param.hide()
        #self.forward.hide()
        self.layout.itemAt(2).widget().deleteLater()
        self.layout.itemAt(3).widget().deleteLater()
        self.criteria_widget = QWidget(self)
        self.criteria_widget.setGeometry(0, 0, 800, 300)
        self.criteria_layout = QGridLayout(self.criteria_widget)
        self.criteria_list = []
        for i in range(self.criteria_number):
            print("kryterium ", i)
            criteria_label = QLabel(self.criteria_widget)
            text = str(i) + "."
            criteria_label.setText(text)
            criteria_edit = QLineEdit(self.criteria_widget)
            self.criteria_list.append(criteria_edit)
            self.criteria_layout.addWidget(criteria_label, i, 0)
            self.criteria_layout.addWidget(criteria_edit, i, 1)
        self.criteria_widget.setLayout(self.criteria_layout)
        self.layout.addWidget(self.criteria_widget)
        self.forward_2 = QPushButton("Dalej", self)
        self.forward_2.setStyleSheet("background:#3f3f3f; color:#d1d1d1; text-transform:uppercase;")
        self.forward_2.setGeometry(170, 400, 150, 30)
        self.forward_2.clicked.connect(self.read_file_window)
        self.layout.addWidget(self.forward_2)

    def read_file_window(self):
        for i in range(self.criteria_number):
            print(self.criteria_list[i].text())
            self.criteria.append(self.criteria_list[i].text())

    def processing(self):
        print("processing")
