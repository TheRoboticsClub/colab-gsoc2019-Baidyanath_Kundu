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

import re
from xml.dom import minidom
from github import Github
from github.GithubException import BadCredentialsException, GithubException
from requests.exceptions import ConnectionError, ReadTimeout
import sys
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, \
    QPushButton, QApplication, QHBoxLayout, QVBoxLayout, \
    QMessageBox, QPlainTextEdit
from PyQt5.QtCore import *

class GithubCredentialsDialog(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.setWindowTitle("Export to Online Library")

        self.drawCredWindow()

    def drawCredWindow(self):
        self.setFixedSize(300, 150)
        VLayout = QVBoxLayout()
        VLayout.setAlignment(Qt.AlignTop)

        titleLblStyleSheet = 'QLabel {font-weight: bold;}'
        rowLayout = QHBoxLayout()
        titleLbl = QLabel('Enter Github username and password')
        titleLbl.setStyleSheet(titleLblStyleSheet)
        rowLayout.addWidget(titleLbl)
        VLayout.addLayout(rowLayout)

        rowLayout = QHBoxLayout()
        usernameLbl = QLabel('Username:')
        usernameLbl.setFixedWidth(80)
        rowLayout.addWidget(usernameLbl)
        self.usernameBox = QLineEdit()
        self.usernameBox.setFixedWidth(190)
        rowLayout.addWidget(self.usernameBox)
        VLayout.addLayout(rowLayout)

        rowLayout = QHBoxLayout()
        passwordLbl = QLabel('Password:')
        passwordLbl.setFixedWidth(80)
        rowLayout.addWidget(passwordLbl)
        self.passwordBox = QLineEdit()
        self.passwordBox.setFixedWidth(190)
        self.passwordBox.setEchoMode(QLineEdit.Password)
        rowLayout.addWidget(self.passwordBox)
        VLayout.addLayout(rowLayout)

        btnLayout = QHBoxLayout()
        btnLayout.setAlignment(Qt.AlignRight)
        self.submitBtn = QPushButton('Submit')
        self.submitBtn.setFixedWidth(100)
        self.submitBtn.clicked.connect(self.submitClicked)
        btnLayout.addWidget(self.submitBtn)
        VLayout.addLayout(btnLayout)
        self.setLayout(VLayout)

    def submitClicked(self):
        self.submitBtn.setEnabled(False)
        self.submitBtn.setText('Checking...')
        self.submitBtn.repaint()
        if self.usernameBox.text() == '':
            QMessageBox.warning(self, 'Error', 'Username field is empty')
        elif self.passwordBox.text() == '':
            QMessageBox.warning(self, 'Error', 'Password field is empty')
        else:
            try:
                name = Github(self.usernameBox.text(), self.passwordBox.text()).get_user().name
                self.username = self.usernameBox.text()
                self.password = self.passwordBox.text()
                self.accept()
            except BadCredentialsException:
                QMessageBox.warning(self, 'Error', 'Incorrect username or password')
            except ConnectionError:
                QMessageBox.warning(self, "Error", "Cannot connect to Github")
                self.close()
            except Exception as e:
                print e
        self.submitBtn.setEnabled(True)
        self.submitBtn.setText('Submit')


class FileExportDialog(QDialog):
    def __init__(self, username, password, xmlFile):
        super(QDialog, self).__init__()
        self.setWindowTitle("Export to Online Library")
        self.username = username
        self.password = password
        self.xmlFile = xmlFile
        self.UI = []

        self.drawDescWindow()

    def drawDescWindow(self):
        self.setFixedSize(500, 330)
        VLayout = QVBoxLayout()
        VLayout.setAlignment(Qt.AlignTop)

        titleLblStyleSheet = 'QLabel {font-weight: bold;}'
        rowLayout = QHBoxLayout()
        titleLbl = QLabel('Enter name and a short description for the automata behaviour')
        titleLbl.setStyleSheet(titleLblStyleSheet)
        rowLayout.addWidget(titleLbl)
        VLayout.addLayout(rowLayout)

        rowLayout = QHBoxLayout()
        nameLbl = QLabel('Name:')
        nameLbl.setFixedWidth(50)
        rowLayout.addWidget(nameLbl)
        self.nameBox = QLineEdit()
        rowLayout.addWidget(self.nameBox)
        VLayout.addLayout(rowLayout)

        VLayout.addWidget(QLabel('Description:'))
        self.descBox = QPlainTextEdit()
        self.descBox.setFixedHeight(170)
        VLayout.addWidget(self.descBox)

        btnLayout = QHBoxLayout()
        btnLayout.setAlignment(Qt.AlignRight)
        self.submitBtn = QPushButton('Submit')
        self.submitBtn.setFixedWidth(80)
        self.submitBtn.clicked.connect(self.submitClicked)
        btnLayout.addWidget(self.submitBtn)
        VLayout.addLayout(btnLayout)

        rowLayout = QHBoxLayout()
        self.statusLbl = QLabel('')
        rowLayout.addWidget(self.statusLbl)
        VLayout.addLayout(rowLayout)
        self.setLayout(VLayout)

    def submitClicked(self):
        self.submitBtn.setEnabled(False)
        self.submitBtn.repaint()
        self.setStatus("Checking Name")
        self.name = self.nameBox.text().strip()
        if nameCheck(self.name):
            self.description = self.descBox.toPlainText()
            if self.description == "":
                self.description = "No description provided"
            try:
                self.upload()
                self.accept()
            except ConnectionError or ReadTimeout:
                QMessageBox.warning(self, "Error", "Cannot connect to Github")
                self.close()
            except Exception as e:
                QMessageBox.warning(self, "Error", e)
                self.submitBtn.setEnabled(True)
        else:
            QMessageBox.warning(self, "Error", "Names ") #TODO:Convention of automata naming in the repo
            self.submitBtn.setEnabled(True)
            self.setStatus("")

    def upload(self):
        branchName = (self.name.lower()).replace(' ','-')
        filename = (self.name).replace(' ','_')
        g = Github(self.username, self.password)

        self.setStatus("Getting library...")
        upUser = g.get_user('sudo-panda')                             #TODO:Change the repo to the actual one
        upRepo = upUser.get_repo("automata-library")                  #TODO:Change the repo to the actual one

        self.setStatus("Forking library...")
        forkUser = g.get_user()
        forkRepo = forkUser.create_fork(upRepo)
        pulls = forkRepo.get_pulls(state='open', sort='created', base='master', head=upUser.login+":master")
        count = 0
        for pr in pulls:
            count += 1
            pull = forkRepo.get_pull(pr.number)
            pull.merge()
        if count == 0:
            #TODO: Find better way to do this
            try:
                fork_pullrequest = forkRepo.create_pull("Merge upstream master into master", "", '{}'.format('master'),
                                                        '{}:{}'.format(upUser.login, 'master'), False)
                fork_pullrequest.merge()
            except Exception as e:
                pass

        self.setStatus("Checking for existing behaviours...")
        branches = list(forkRepo.get_branches())
        activeBranch = None
        exists = False
        for branch in branches:
            if branch.name == branchName:
                activeBranch = forkRepo.get_branch(branch=branchName)
                exists = True
        if activeBranch is None:
            masterBranch = forkRepo.get_branch(branch='master')
            forkRepo.create_git_ref(ref='refs/heads/' + branchName, sha=masterBranch.commit.sha)
            activeBranch = forkRepo.get_branch(branch=branchName)

        if exists:
            self.setStatus("Updating existing behaviour...")
            catalogue = forkRepo.get_contents("Catalogue.xml", ref=branchName)
            doc = minidom.parseString(catalogue.decoded_content)
            behaviour = forkRepo.get_contents(self.name+"/"+filename+".xml", ref=branchName)
            forkRepo.update_file("Catalogue.xml", "Edit behaviour description in catalogue",
                                 changeCatalogue(doc, self.name, self.description), catalogue.sha, branch=branchName)
            forkRepo.update_file(self.name+"/"+filename+".xml", "Edit behaviour file",
                                 self.xmlFile, behaviour.sha, branch=branchName)

            pulls = upRepo.get_pulls(state='open', sort='created', base='master', head=forkUser.login + ":" + branchName)
            pull_exists = False
            for pr in pulls:
                pr.edit(title="Add " + self.name + " behaviour", body=self.description)
                pull_exists = True
            if not pull_exists:
                self.setStatus("Creating pull request")
                pullrequest = upRepo.create_pull("Add " + self.name + " behaviour", self.description,
                                                 '{}'.format('master'), '{}:{}'.format(forkUser.login, branchName), True)
        else:
            self.setStatus("Creating new behaviour...")
            catalogue = forkRepo.get_contents("Catalogue.xml", ref=branchName)

            #TODO: Remove the try except after first commit to library
            try:
                doc = minidom.parseString(catalogue.decoded_content)
            except:
                doc = minidom.Document()
                catElement = doc.createElement('Catalogue')
                doc.appendChild(catElement)

            forkRepo.update_file("Catalogue.xml", "Add behaviour to catalogue",
                                 changeCatalogue(doc, self.name, self.description), catalogue.sha, branch=branchName)
            forkRepo.create_file(self.name + "/" + filename + ".xml", "Add behaviour file",
                                 self.xmlFile, branch=branchName)

            self.setStatus("Creating pull request")
            pullrequest = upRepo.create_pull("Add "+self.name+" behaviour", self.description,
                                             '{}'.format('master'), '{}:{}'.format(forkUser.login, branchName), True)

    def setStatus(self, text):
        self.statusLbl.setText(text)
        self.statusLbl.repaint()

def changeCatalogue(doc, name, description):
    exists = False
    behaviourList = doc.getElementsByTagName('Catalogue')[0].getElementsByTagName('behaviour')
    for behElement in behaviourList:
        if behElement.getAttribute('name') == name:
            descElement = behElement.getElementsByTagName('description')[0]
            descElement.childNodes[0].nodeValue = description
            exists = True
    if not exists:
        behElement = doc.createElement('behaviour')
        behElement.setAttribute('name', name)
        descElement = doc.createElement('description')
        descElement.appendChild(doc.createTextNode(description))
        behElement.appendChild(descElement)
        doc.getElementsByTagName('Catalogue')[0].appendChild(behElement)
    xmlStr = re.sub(r'(\n( *))(\1)+', r'\1', doc.toprettyxml(indent='  '))
    xmlStr = re.sub(r'\n( *)\n', '\n', xmlStr)
    return xmlStr

def nameCheck(name):
    g = Github("", "")
    repo = g.get_repo('sudo-panda/automata-library')
    files = repo.get_contents("")
    for file in files:
        if file.path == name:
            return False
    #TODO:regulate naming of behaviours in the repo
    return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    username = "test940" #TODO: Remove these
    password = "Deta1nwreck"

    dialog = FileExportDialog(username, password, '')
    if dialog.exec_():
        name = dialog.name
        description = dialog.description