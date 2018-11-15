# NODE $ERVER$Y$TEM ## CLASSES #
'''
Classes are used to create consistent data structures and namespaces 
within other modules in the repository. 
'''

# -- Imports -- # 
import datetime


class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.reputation = 0.0
        self.fullname = self.fullname_construction()

    def fullname_construction(self):
        return '{}{}'.format(self.first, self.last)
        
    # method for storing user reputation status
    def reputation_calc(self):
        category_rep = self.reputation

class Admin:
    # TODO: make the admin class an inherited class under the user
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Idea:
    def __init__(self, title, category, value, creator):
        self.title = title
        self.category = category
        self.value = value
        self.creator = creator  

class DateTime():
    def dt(self):
        return datetime.datetime.now()

class Command:
    def __init__(self, cmd, func):
        self._command = cmd
        self._function = func
    
