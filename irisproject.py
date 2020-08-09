# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'irisproject.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys 
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Iris Detection")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 40, 421, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 410, 181, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sepal_length_lebel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        self.sepal_length_lebel.setFont(font)
        self.sepal_length_lebel.setObjectName("sepal_length_lebel")
        self.verticalLayout.addWidget(self.sepal_length_lebel)
        self.sepal_width_lebel_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        self.sepal_width_lebel_2.setFont(font)
        self.sepal_width_lebel_2.setObjectName("sepal_width_lebel_2")
        self.verticalLayout.addWidget(self.sepal_width_lebel_2)
        self.petal_length_lebel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        self.petal_length_lebel.setFont(font)
        self.petal_length_lebel.setObjectName("petal_length_lebel")
        self.verticalLayout.addWidget(self.petal_length_lebel)
        self.petal_width_lebel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        self.petal_width_lebel.setFont(font)
        self.petal_width_lebel.setObjectName("petal_width_lebel")
        self.verticalLayout.addWidget(self.petal_width_lebel)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(260, 400, 161, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sepal_length = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.sepal_length.setObjectName("sepal_length")
        self.verticalLayout_2.addWidget(self.sepal_length)
        self.sepal_width = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.sepal_width.setObjectName("sepal_width")
        self.verticalLayout_2.addWidget(self.sepal_width)
        self.petal_length = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.petal_length.setObjectName("petal_length")
        self.verticalLayout_2.addWidget(self.petal_length)
        self.petal_width = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.petal_width.setObjectName("petal_width")
        self.verticalLayout_2.addWidget(self.petal_width)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 641, 271))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix1/types.png);")
        self.label_3.setObjectName("label_3")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(300, 660, 121, 41))
        self.submit.setObjectName("submit")

        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(470, 440, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(26)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-80, -20, 961, 811))
        self.label_2.setStyleSheet("background-image: url(:/newPrefixbg/bg.jpg);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefixbg/bg.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.label_3.raise_()
        self.submit.raise_()
        self.result.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuAI_System = QtWidgets.QMenu(self.menubar)
        self.menuAI_System.setObjectName("menuAI_System")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionIris_Detection = QtWidgets.QAction(MainWindow)
        self.actionIris_Detection.setObjectName("actionIris_Detection")
        self.menuAI_System.addAction(self.actionIris_Detection)
        self.menuAI_System.addSeparator()
        self.menubar.addAction(self.menuAI_System.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Iris Detection"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p>heelo</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">IRIS Flower DETECTION</span></p></body></html>"))
        self.sepal_length_lebel.setText(_translate("MainWindow", "<font color=white>Sepal length"))
        self.sepal_width_lebel_2.setText(_translate("MainWindow", "<font color=white>Sepal width"))
        self.petal_length_lebel.setText(_translate("MainWindow", "<font color=white>Petal length"))
        self.petal_width_lebel.setText(_translate("MainWindow", "<font color=white>Petal width"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.submit.setText(_translate("MainWindow", "Predict"))
        self.result.setText(_translate("MainWindow", "<font color=white>Result"))
        self.menuAI_System.setTitle(_translate("MainWindow", "AI System"))
        self.actionIris_Detection.setText(_translate("MainWindow", "Iris Detection"))

        

        self.submit.clicked.connect(self.OpenClick)

    def OpenClick(self):
        a = self.sepal_length.text()
        b = self.sepal_width.text()
        c = self.petal_length.text()
        d = self.petal_width.text()

        e=float(a)
        f=float(b)
        g=float(c)
        h=float(d)
        if e>10 or f>10 or g>10 or h>10:
            new_prediction="Invalid input"
            self.result.setText(str(new_prediction))
        else: 

            plt.style.use("ggplot")
            iris = pd.read_csv("iris.csv")
            df= pd.DataFrame(iris)
            #print(df)
            y = df['species'].values
            X = df.drop('species', axis=1).values
            #Q=np.array(df['petal_length'])
            #W=np.array(df['petal_width'])
            #plt.scatter(Q,W)
            #plt.show()
            # Create a k-NN classifier with 6 neighbors: knn
            knn = knn = KNeighborsClassifier(n_neighbors=3)
            # Fit the classifier to the data
            knn.fit(X,y)

             # Predict the labels for the training data X
            _=knn.predict(X)
            
            #print(y_pred)
            X_new=[[e,f,g,h]]

            new_prediction = knn.predict(X_new)
        
            

            self.result.setText(str(new_prediction))





import bgv_rc
import blurr_rc
import types_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

