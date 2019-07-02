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

from xml.dom import minidom
from github import Github
import threading
from github.GithubException import BadCredentialsException, GithubException
from requests.exceptions import ConnectionError, ReadTimeout
import sys
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton,\
    QApplication, QHBoxLayout, QVBoxLayout, QScrollArea, \
    QGroupBox, QBoxLayout, QPlainTextEdit
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from ..tools.elidedlabel import ElidedLabel

class FileImportDialog(QDialog):
    fileStr = pyqtSignal('QString')
    def __init__(self):
        super(QDialog, self).__init__()
        self.setWindowTitle("Import behaviour from online library")
        self.setMinimumSize(700, 450)
        self.drawWindow()

    def drawWindow(self):
        VLayout = QVBoxLayout()

        rowLayout = QHBoxLayout()

        titleLblStyleSheet = 'QLabel {font-weight: bold;}'
        rowLayout.setAlignment(Qt.AlignLeft)
        rowLayout.addSpacing(10)
        titleLbl = QLabel('Select the behaviour to import:')
        titleLbl.setStyleSheet(titleLblStyleSheet)
        rowLayout.addWidget(titleLbl)

        VLayout.addLayout(rowLayout)

        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
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
        cancelBtn = QPushButton("Cancel")
        cancelBtn.setFixedWidth(80)
        cancelBtn.clicked.connect(self.cancelClicked)
        btnLayout.addWidget(cancelBtn)
        VLayout.addLayout(btnLayout)

        self.statusLbl = QLabel('')
        VLayout.addWidget(self.statusLbl)


        self.setLayout(VLayout)
        self.show()
        getCatalogue = GetCatalogue()
        getCatalogue.xmlStr.connect(self.displayCatalogue)
        getCatalogue.run()

    def displayCatalogue(self, catalogue):
        self.doc = minidom.parseString(catalogue)
        behaviourList = self.doc.getElementsByTagName('Catalogue')[0].getElementsByTagName('behaviour')
        count = 0
        for behElement in behaviourList:
            name = behElement.getAttribute('name')
            description = behElement.getElementsByTagName('description')[0].childNodes[0].nodeValue
            self.addBehaviour(count, name, description)
            count += 1

    def addBehaviour(self, id, name, description):
        nameLblStyleSheet = 'QLabel {font-weight: bold;}'
        rowLayout = QHBoxLayout()

        behLayout = QVBoxLayout()
        nameLbl = ElidedLabel(name)
        nameLbl.setMinimumWidth(530)
        nameLbl.setToolTip(name)
        nameLbl.setStyleSheet(nameLblStyleSheet)

        behLayout.addWidget(nameLbl)
        descLbl = ElidedLabel(description)
        descLbl.setMinimumWidth(530)
        descLbl.setFixedHeight(17)
        descLbl.setAlignment(Qt.AlignTop)
        behLayout.addWidget(descLbl)

        rowLayout.addLayout(behLayout)

        selectBtn = QPushButton('Select')
        selectBtn.setObjectName(str(id))
        selectBtn.setFixedWidth(100)
        selectBtn.clicked.connect(self.selected)
        rowLayout.addWidget(selectBtn)
        self.scrollVlayout.addLayout(rowLayout)

    def selected(self):
        id = int(self.sender().objectName())
        behElement = self.doc.getElementsByTagName('Catalogue')[0].getElementsByTagName('behaviour')[id]
        name = behElement.getAttribute('name')
        description = behElement.getElementsByTagName('description')[0].childNodes[0].nodeValue
        behDialog = BehaviourDialog(name, description)
        if behDialog.exec_():
            self.fileStr.emit(behDialog.fileStr)
            self.accept()

    def cancelClicked(self):
        self.close()

class BehaviourDialog(QDialog):
    def __init__(self, name, description):
        super(QDialog, self).__init__()
        self.setMinimumSize(600, 500)
        self.name = name
        self.description = description
        self.fileStr = ''
        self.setWindowTitle(self.name)
        self.drawWindow()

    def drawWindow(self):
        VLayout = QVBoxLayout()
        titleLblStyleSheet = 'QLabel {font-weight: bold;}'

        rowLayout = QHBoxLayout()
        titleLbl = QLabel('Description:')
        titleLbl.setMinimumWidth(200)
        titleLbl.setStyleSheet(titleLblStyleSheet)
        rowLayout.addWidget(titleLbl)
        titleLbl = QLabel('Snapshot:')
        titleLbl.setMinimumWidth(200)
        titleLbl.setStyleSheet(titleLblStyleSheet)
        rowLayout.addWidget(titleLbl)
        VLayout.addLayout(rowLayout)

        rowLayout = QHBoxLayout()
        descBox = QPlainTextEdit(self.description)
        descBox.setReadOnly(True)
        rowLayout.addWidget(descBox)
        descBox = QPlainTextEdit('')
        rowLayout.addWidget(descBox)
        VLayout.addLayout(rowLayout)

        btnLayout = QHBoxLayout()
        btnLayout.setAlignment(Qt.AlignRight)
        importBtn = QPushButton("Import")
        importBtn.setFixedWidth(80)
        importBtn.clicked.connect(self.importClicked)
        btnLayout.addWidget(importBtn)
        cancelBtn = QPushButton("Cancel")
        cancelBtn.setFixedWidth(80)
        cancelBtn.clicked.connect(self.cancelClicked)
        btnLayout.addWidget(cancelBtn)
        VLayout.addLayout(btnLayout)
        self.setLayout(VLayout)
        self.t = threading.Thread(target=self.downloadFile)
        self.t.start()

    def cancelClicked(self):
        self.close()

    def downloadFile(self):
        g = Github("", "")
        repo = g.get_repo("sudo-panda/automata-library")  # TODO: Change repo
        self.fileStr = repo.get_contents(self.name + "/" + self.name.replace(' ', '_') + ".xml").decoded_content

    def importClicked(self):
        self.t.join()
        self.accept()

class GetCatalogue(QThread):
    xmlStr = pyqtSignal('QString')
    def __init__(self):
        super(QThread, self).__init__()

    def run(self):
        g = Github("", "")
        repo = g.get_repo("sudo-panda/automata-library")  # TODO: Replace with actual repo
        catalogue = repo.get_contents("Catalogue.xml")
        self.xmlStr.emit(catalogue.decoded_content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = FileImportDialog()
    dialog.exec_()