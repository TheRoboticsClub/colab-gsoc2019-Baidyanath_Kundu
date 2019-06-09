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
    QMessageBox
from PyQt5.QtCore import pyqtSignal
from visualstates.core.parameter import Parameter, isParamName
from PyQt5.QtCore import *


class DuplicateParamsDialog(QDialog):
    def __init__(self, name, newParam, oldParam, newParams, oldParams):
        super(QDialog, self).__init__()
        self.setWindowTitle(name)
        self.newParam = newParam
        self.oldParam = oldParam
        self.newParams = newParams
        self.oldParams = oldParams
        self.newName = None
        self.setFixedSize(600, 400)

        self.drawWindow()

    def drawWindow(self):
        VLayout = QVBoxLayout()
        VLayout.setAlignment(Qt.AlignTop)
        if self.newParam.type == self.oldParam.type:
            msg = QLabel('You can keep the same name for both parameters if you think their descriptions are same or you can change the name of the new one')
        else:
            msg = QLabel('Change the name of the imported parameter')
        msg.setFixedHeight(50)
        msg.setWordWrap(True)
        VLayout.addWidget(msg)

        rowLayout = QHBoxLayout()
        spaceLbl = QLabel('')
        spaceLbl.setFixedWidth(100)
        rowLayout.addWidget(spaceLbl)
        titleLblStyleSheet = 'QLabel {font-weight: bold;}'
        importLbl = QLabel('Imported:')
        importLbl.setFixedWidth(235)
        importLbl.setStyleSheet(titleLblStyleSheet)
        rowLayout.addWidget(importLbl)
        existLbl = QLabel('Existing:')
        existLbl.setFixedWidth(235)
        existLbl.setStyleSheet(titleLblStyleSheet)
        rowLayout.addWidget(existLbl)
        VLayout.addLayout(rowLayout)

        rowLayout = QHBoxLayout()
        lblLayout = QVBoxLayout()
        lblLayout.setAlignment(Qt.AlignTop)
        nameLbl = QLabel('Name:')
        nameLbl.setFixedWidth(100)
        nameLbl.setFixedHeight(25)
        lblLayout.addWidget(nameLbl)
        typeLbl = QLabel('Type:')
        typeLbl.setFixedWidth(100)
        typeLbl.setFixedHeight(25)
        lblLayout.addWidget(typeLbl)
        valueLbl = QLabel('Value:')
        valueLbl.setFixedWidth(100)
        valueLbl.setFixedHeight(25)
        lblLayout.addWidget(valueLbl)
        descLbl = QLabel('Description:')
        descLbl.setFixedWidth(100)
        lblLayout.addWidget(descLbl)
        rowLayout.addLayout(lblLayout)

        importLayout = QVBoxLayout()
        importLayout.setAlignment(Qt.AlignTop)
        self.newName = QLineEdit(self.newParam.name)
        self.newName.setFixedWidth(235)
        self.newName.setFixedHeight(25)
        importLayout.addWidget(self.newName)
        typeLbl = QLabel(self.newParam.type)
        typeLbl.setFixedHeight(25)
        importLayout.addWidget(typeLbl)
        valueLbl = QLabel(self.newParam.value)
        valueLbl.setFixedHeight(25)
        importLayout.addWidget(valueLbl)
        descLbl = QLabel(self.newParam.desc)
        descLbl.setFixedHeight(180)
        descLbl.setWordWrap(True)
        descLbl.setAlignment(Qt.AlignTop)
        importLayout.addWidget(descLbl)
        rowLayout.addLayout(importLayout)

        existLayout = QVBoxLayout()
        existLayout.setAlignment(Qt.AlignTop)
        nameLbl = QLabel(self.oldParam.name)
        nameLbl.setFixedWidth(235)
        nameLbl.setFixedHeight(25)
        existLayout.addWidget(nameLbl)
        typeLbl = QLabel(self.oldParam.type)
        typeLbl.setFixedHeight(25)
        existLayout.addWidget(typeLbl)
        valueLbl = QLabel(self.oldParam.value)
        valueLbl.setFixedHeight(25)
        existLayout.addWidget(valueLbl)
        descLbl = QLabel(self.oldParam.desc)
        descLbl.setFixedHeight(180)
        descLbl.setWordWrap(True)
        descLbl.setAlignment(Qt.AlignTop)
        existLayout.addWidget(descLbl)
        rowLayout.addLayout(existLayout)

        VLayout.addLayout(rowLayout)

        btnLayout = QHBoxLayout()
        btnLayout.setAlignment(Qt.AlignRight)
        doneBtn = QPushButton("Done")
        doneBtn.setFixedWidth(80)
        doneBtn.clicked.connect(self.doneClicked)
        btnLayout.addWidget(doneBtn)
        VLayout.addLayout(btnLayout)
        self.setLayout(VLayout)

    def closeEvent(self, event):
        self.doneClicked()

    def doneClicked(self):
        if isParamName(self.newName.text()):
            if self.newParam.name == self.newName.text():
                if self.newParam.type == self.oldParam.type:
                    self.close()
                else:
                    QMessageBox.warning(self, 'Error', 'Imported and existing parameters\ncan\'t have the same name.')
            else:
                for param in self.oldParams:
                    if param.name == self.newName.text():
                        QMessageBox.warning(self, 'Error', 'Name conflicts with another existing parameter.')
                        return
                for param in self.newParams:
                    if param.name == self.newName.text():
                        QMessageBox.warning(self, 'Error', 'Name conflicts with another existing parameter.')
                        return
                self.close()
        else:
            QMessageBox.warning(self, 'Error', 'Name not valid')

    def getName(self):
        return self.newName.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    param1 = Parameter('Name', 'String', 'Value', 'Description')
    param2 = Parameter('Name', 'String', 'Value', 'Description')
    dialog = DuplicateParamsDialog('Resolve Duplicate Parameters', param1, param2, [], [])
    dialog.exec_()