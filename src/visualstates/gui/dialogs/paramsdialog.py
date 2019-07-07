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
from PyQt5.QtWidgets import QDialog, QLabel,  \
    QPushButton, QApplication, QHBoxLayout, QVBoxLayout, \
    QScrollArea, QGroupBox, QBoxLayout
from PyQt5.QtCore import pyqtSignal, Qt
from visualstates.gui.tools.elidedlabel import ElidedLabel


class ImportedParamsDialog(QDialog):
    paramsChanged = pyqtSignal(list)

    def __init__(self, name, rootState):
        super(QDialog, self).__init__()
        self.setWindowTitle(name)
        self.rootState = rootState
        self.paramUIs = []
        self.removeIds = []
        self.setMinimumSize(800, 500)

        self.drawWindow()

    def drawWindow(self):
        VLayout = QVBoxLayout()

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
        doneBtn = QPushButton("Done")
        doneBtn.setFixedWidth(80)
        doneBtn.clicked.connect(self.doneClicked)
        btnLayout.addWidget(doneBtn)
        VLayout.addLayout(btnLayout)
        self.addStates(self.scrollVlayout, self.rootState, root=True)
        self.setLayout(VLayout)

    def addStates(self, layout, state, root=False):
        titleLblStyleSheet = 'QLabel {font-weight:bold;}'
        childTitleLblStyleSheet = 'QLabel {font:italic; font-weight:bold;}'
        bulletLblStyleSheet = 'QLabel {font-size: 25px; font-weight:bold;}'
        if not root:
            rowLayout = QHBoxLayout()
            rowLayout.addSpacing(10)
            bulletLbl = QLabel(u"\u2022")
            bulletLbl.setFixedWidth(10)
            bulletLbl.setStyleSheet(bulletLblStyleSheet)
            rowLayout.addWidget(bulletLbl)
            nameLbl = QLabel(state.getName())
            nameLbl.setMinimumWidth(100)
            nameLbl.setStyleSheet(titleLblStyleSheet)
            rowLayout.addWidget(nameLbl)
            layout.addLayout(rowLayout)

            #if len(state.getNamespace().getParams()) > 0 or len(state.getChildren()) > 0:
            rowLayout = QHBoxLayout()
            rowLayout.addSpacing(14)
            newLayout = QVBoxLayout()
            newLayout.setDirection(QBoxLayout.TopToBottom)
            newLayout.setAlignment(Qt.AlignTop)
            dummyBox = QGroupBox()
            dummyBox.setStyleSheet('QGroupBox {padding: 0px; margin: 0px; border-left: 1px solid gray; '
                                   'border-top: 0px;}')
            dummyBox.setLayout(newLayout)
            rowLayout.addWidget(dummyBox)
            layout.addLayout(rowLayout)
        else:
            newLayout = layout

        if len(state.getNamespace().getParams()) > 0:
            paramTitleLbl = QLabel('Parameters:')
            paramTitleLbl.setStyleSheet(childTitleLblStyleSheet)
            newLayout.addWidget(paramTitleLbl)
            for param in state.getNamespace().getParams():
                self.addParam(newLayout, param)

        if len(state.getChildren()) > 0:
            childStatesTitleLbl = QLabel('Child States:')
            childStatesTitleLbl.setStyleSheet(childTitleLblStyleSheet)
            newLayout.addWidget(childStatesTitleLbl)
            for child in state.getChildren():
                self.addStates(newLayout, child)

        return layout

    def addParam(self, layout, param):
        titleLblStyleSheet = 'QLabel {font: italic;}'
        rowLayout = QHBoxLayout()
        rowLayout.addSpacing(10)
        titleLbl = QLabel('Name:')
        titleLbl.setStyleSheet(titleLblStyleSheet)
        titleLbl.setFixedWidth(43)
        rowLayout.addWidget(titleLbl)
        nameLbl = ElidedLabel(param.name)
        nameLbl.setToolTip(param.name)
        nameLbl.setFixedWidth(150)
        rowLayout.addWidget(nameLbl)
        rowLayout.addSpacing(5)
        titleLbl = QLabel('Type:')
        titleLbl.setStyleSheet(titleLblStyleSheet)
        titleLbl.setFixedWidth(36)
        rowLayout.addWidget(titleLbl)
        typeLbl = ElidedLabel(param.type)
        typeLbl.setFixedWidth(60)
        rowLayout.addWidget(typeLbl)
        rowLayout.addSpacing(5)
        titleLbl = QLabel('Value:')
        titleLbl.setStyleSheet(titleLblStyleSheet)
        titleLbl.setFixedWidth(47)
        rowLayout.addWidget(titleLbl)
        valueLbl = ElidedLabel(param.value)
        valueLbl.setToolTip(param.value)
        valueLbl.setFixedWidth(100)
        rowLayout.addWidget(valueLbl)
        rowLayout.addSpacing(5)
        titleLbl = QLabel('Description:')
        titleLbl.setStyleSheet(titleLblStyleSheet)
        titleLbl.setFixedWidth(80)
        rowLayout.addWidget(titleLbl)
        descLbl = ElidedLabel(param.desc)
        descLbl.setAlignment(Qt.AlignTop)
        descLbl.setFixedHeight(17)
        descLbl.setToolTip(param.desc)
        descLbl.setMinimumWidth(400)
        rowLayout.addWidget(descLbl)

        layout.addLayout(rowLayout)


    def doneClicked(self):
        self.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ImportedParamsDialog('Parameters')
    dialog.exec_()