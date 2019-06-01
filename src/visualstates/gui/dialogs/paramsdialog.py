'''
   Copyright (C) 1997-2019 JDERobot Developers Team

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU Library General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, see <http://www.gnu.org/licenses/>.

   Authors : Baidyanath Kundu (kundubaidya99@gmail.com)

  '''
import sys
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, \
    QPushButton, QApplication, QHBoxLayout, QVBoxLayout, \
    QScrollArea, QGroupBox, QBoxLayout
from PyQt5.QtCore import pyqtSignal
from visualstates.gui.dialogs.paramprop import ParamPropDialog
from visualstates.core.parameter import Parameter
from PyQt5.QtCore import *


class ParamsDialog(QDialog):
    paramsChanged = pyqtSignal(list)

    def __init__(self, name, params):
        super(QDialog, self).__init__()
        self.setWindowTitle(name)
        self.params = params
        self.paramUIs = []
        self.removeIds = []
        self.setFixedSize(800, 500)

        self.drawWindow()

    def drawWindow(self):
        VLayout = QVBoxLayout()

        rowLayout = QHBoxLayout()

        rowLayout.setAlignment(Qt.AlignLeft)
        rowLayout.addSpacing(10)
        titleLblStyleSheet = 'QLabel {font-weight: bold;}'
        nameLbl = QLabel('Name')
        nameLbl.setStyleSheet(titleLblStyleSheet)
        nameLbl.setFixedWidth(100)
        rowLayout.addWidget(nameLbl)
        typeLbl = QLabel('Type')
        typeLbl.setStyleSheet(titleLblStyleSheet)
        typeLbl.setFixedWidth(60)
        rowLayout.addWidget(typeLbl)
        valueLbl = QLabel('Value')
        valueLbl.setStyleSheet(titleLblStyleSheet)
        valueLbl.setFixedWidth(100)
        rowLayout.addWidget(valueLbl)
        descLbl = QLabel('Description')
        descLbl.setStyleSheet(titleLblStyleSheet)
        descLbl.setFixedWidth(280)
        rowLayout.addWidget(descLbl)

        VLayout.addLayout(rowLayout)

        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #scrollArea.setStyleSheet('QScrollArea {border: 0px;}')
        self.scrollVlayout = QVBoxLayout()
        self.scrollVlayout.setDirection(QBoxLayout.TopToBottom)
        self.scrollVlayout.setAlignment(Qt.AlignTop)
        dummyBox = QGroupBox()
        dummyBox.setStyleSheet('QGroupBox {padding: 0px; margin: 0px;}')
        dummyBox.setLayout(self.scrollVlayout)
        scrollArea.setWidget(dummyBox)
        VLayout.addWidget(scrollArea)

        btnLayout = QHBoxLayout()
        btnLayout.setAlignment(Qt.AlignRight)
        newBtn = QPushButton("New")
        newBtn.setFixedWidth(80)
        newBtn.clicked.connect(self.newClicked)
        btnLayout.addWidget(newBtn)
        doneBtn = QPushButton("Done")
        doneBtn.setFixedWidth(80)
        doneBtn.clicked.connect(self.doneClicked)
        btnLayout.addWidget(doneBtn)
        VLayout.addLayout(btnLayout)
        for i in range(len(self.params)):
            self.addParam(i)
        self.setLayout(VLayout)

    def newClicked(self):
        dialog = ParamPropDialog(params=self.params)
        dialog.paramAdded.connect(self.paramAddedHandler)
        dialog.exec_()

    def addParam(self, id):
        param = self.params[id]
        rowLayout = QHBoxLayout()
        nameLbl = QLabel(param.name)
        nameLbl.setToolTip(param.name)
        nameLbl.setFixedWidth(100)
        rowLayout.addWidget(nameLbl)
        typeLbl = QLabel(param.type)
        typeLbl.setFixedWidth(60)
        rowLayout.addWidget(typeLbl)
        valueLbl = QLabel(param.value)
        valueLbl.setToolTip(param.value)
        valueLbl.setFixedWidth(100)
        rowLayout.addWidget(valueLbl)
        descLbl = QLabel(param.desc)
        descLbl.setFixedHeight(17)
        descLbl.setToolTip(param.desc)
        descLbl.setFixedWidth(280)
        rowLayout.addWidget(descLbl)

        editBtn = QPushButton('Edit')
        editBtn.setFixedWidth(80)
        editBtn.setObjectName(str(id))
        editBtn.clicked.connect(self.editHandler)
        rowLayout.addWidget(editBtn)
        removeBtn = QPushButton('Remove')
        removeBtn.setFixedWidth(80)
        removeBtn.setObjectName(str(id))
        removeBtn.clicked.connect(self.removeHandler)
        rowLayout.addWidget(removeBtn)

        self.scrollVlayout.addLayout(rowLayout)
        UI = [nameLbl, typeLbl, valueLbl, descLbl, editBtn, removeBtn]
        self.paramUIs.append(UI)

    def paramAddedHandler(self, params):
        self.params = params
        self.addParam(len(self.params)-1)

    def removeHandler(self):
        removeId = int(self.sender().objectName())
        self.removeIds.append(removeId)
        for uiItem in self.paramUIs[removeId]:
            uiItem.deleteLater()


    def editHandler(self):
        editID = int(self.sender().objectName())
        dialog = ParamPropDialog(params=self.params, id=editID)
        dialog.paramUpdated.connect(self.paramUpdatedHandler)
        dialog.exec_()

    def paramUpdatedHandler(self, params, id):
        self.params = params
        param = self.params[id]
        UI = self.paramUIs[id]
        UI[0].setText(param.name)
        UI[1].setText(param.type)
        UI[2].setText(param.value)
        UI[3].setText(param.desc)


    def doneClicked(self):
        count = 0
        for id in self.removeIds:
            id = id - count
            self.params.pop(id)
            count += 1
        self.paramsChanged.emit(self.params)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ParamsDialog('Parameters', params=[])
    dialog.exec_()