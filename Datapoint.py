import pickle
from tkinter import *
from tkinter import filedialog

class Datapoint(object):
    def __init__(self, *args):
        self.datapoint = []
        self.colorpoint = []
        self.currentColor = "#ff0000"
        self.filename = ""
        self.height= None
        self.width = None
        self.prepic = []

    def getfilename(self):
        return self.filename
    
    def setfilename(self,pathfile):
        self.filename = pathfile

        
    

   

  
    
    