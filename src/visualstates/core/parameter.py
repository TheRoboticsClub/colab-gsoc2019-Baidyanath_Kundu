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

class Parameter:
    def __init__(self):
        self.name = ''
        self.type = ''
        self.value = ''
        self.desc = ''

    def setName(self, name):
        self.name = name

    def setType(self, type):
        self.type = type

    def setValue(self, value):
        self.value = value

    def setDesc(self, desc):
        self.desc = desc

def isTypeEqualValue(type, value):
    if type == 'Boolean' and not (value == 'True' or value == 'False'):
        return False
    elif type == 'Integer' and not value.isdigit():
        return False
    elif type == 'Float' and not (value.replace('.', '', 1).isdigit()):
        return False
    else:
        return True

def isParamName(name):
    if name.replace('_', '').isalnum() and name[0].isalpha():
        return True
    else:
        return False
