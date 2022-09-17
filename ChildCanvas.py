import os
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import cv2
from PIL import ImageTk, Image
import pickle
import Datapoint as DP

class ChildCanvas(tk.Frame):
    def __init__(self, parent):

        self.parrent = parent
        self.toplevel1 = tk.Tk()
        self.labelframe1 = tk.LabelFrame(self.toplevel1)
        self.canvas3 = tk.Canvas(self.labelframe1)
        self.canvas3.pack(side='top')
        self.labelframe1.configure(height='400', text='ภาพตัวอย่าง', width='400')
        self.labelframe1.pack(side='top')
        self.toplevel1.configure(height='800', width='800')
        self.frame3 = tk.Frame(self.toplevel1)
        self.button1 = tk.Button(self.frame3)
        self.button1.configure(text='บันทึก')
        self.button1.grid(column='0', row='0', sticky='nw')
        self.button2 = tk.Button(self.frame3)
        self.button2.configure(text='ยกเลิก')
        self.button2.grid(column='1', row='0', sticky='n')
        self.frame3.configure(height='500', width='500')
        self.frame3.pack(side='top')
       

        self.button1['command'] = self.saveAndDraw
        self.button2['command'] = self.dis

        self.canvas_width = 500
        self.canvas_height = 500
        self.line_distance = 1
        self.scale = 8


    def create_window(self):
        print("xx")
        # self.destroy()
    
    def dis(self):
        self.parrent.changemode(mode=1)
        self.toplevel1.destroy()
    
    def convertColor(self,colorCode):
        return (int(colorCode, 16))

    def saveAndDraw(self):
        self.parrent.changemode(mode=1)
        
        self.DatapointSave = np.ones((self.canvas_height*self.scale,self.canvas_width*self.scale,3),dtype=np.uint8)*255
        self.DatapointSave.shape
        for indexPoint,colorconvert in enumerate(self.GDatapoint.colorpoint):
            color1 = self.convertColor(colorconvert[1:3])
            color2 = self.convertColor(colorconvert[3:5])
            color3 = self.convertColor(colorconvert[5:])
            x,y =self.GDatapoint.datapoint[indexPoint]

            x,y = int(x),int(y)
            print(x,y)
            self.DatapointSave[y*self.scale:(y*self.scale)+self.scale,x*self.scale:(x*self.scale)+self.scale,0] = color1
            self.DatapointSave[y*self.scale:(y*self.scale)+self.scale,x*self.scale:(x*self.scale)+self.scale,1] = color2
            self.DatapointSave[y*self.scale:(y*self.scale)+self.scale,x*self.scale:(x*self.scale)+self.scale,2] = color3
            
        # background_image_data = cv2.imread("origin.jpg")
        img = ImageTk.PhotoImage(Image.fromarray(self.DatapointSave))
        self.parrent.Fullthumnal = img
        self.parrent.thumnal = self.DatapointSave
        ### redraw map
        self.parrent.redrawCanvasMini()

        ## save image
        with open("ImageMini/IndexImage.txt","r") as readIndex:
            indexImage = int(readIndex.readlines()[0])
            readIndex.close()
        with open("ImageMini/Image{:04d}.pk".format(indexImage+1), 'wb') as output:
            pickle.dump(self.DatapointSave, output, pickle.HIGHEST_PROTOCOL)
            output.close()
        with open("ImageMini/R_Image{:04d}.pk".format(indexImage+1), 'wb') as output:
            pickle.dump(self.GDatapoint, output, pickle.HIGHEST_PROTOCOL)
            output.close()

        with open("ImageMini/IndexImage.txt","w") as readIndex:
            readIndex.write("{:04d}".format(indexImage+1))

        ## reinsert listbox
        self.parrent.reloadListImage()
        self.toplevel1.destroy()



    def canvasDrawGrid(self,tempData,tempColor):
        self.parrent.changemode(mode=2)
        line_distance = 10
        #print(self.scale)
        self.GDatapoint = DP.Datapoint()
        self.GDatapoint.datapoint = tempData
        self.GDatapoint.colorpoint = tempColor
        self.GDatapoint.height = self.canvas_height
        self.GDatapoint.width = self.canvas_width

        #print(self.canvas_height*self.scale)
        #print(self.canvas_width*self.scale)
        self.canvas3.config(height=(self.canvas_height*self.scale),width=(self.canvas_width*self.scale))

        # vertical lines at an interval of "line_distance" pixel
        for x in range(0,int(self.canvas_width*self.scale),int(self.line_distance*self.scale)):
            if x%(5*self.scale) == 0:
               self.canvas3.create_line(x, 0, x, int(self.canvas_height*self.scale), fill="black")
            else: 
                self.canvas3.create_line(x, 0, x, int(self.canvas_height*self.scale), fill="gray")
        # horizontal lines at an interval of "line_distance" pixel
        for y in range(0,int(self.canvas_height*self.scale),int(self.line_distance*self.scale)):
            if y%(5*self.scale) == 0:
               self.canvas3.create_line(0, y, int(self.canvas_width*self.scale), y, fill="black")
            else: 
                self.canvas3.create_line(0, y, int(self.canvas_width*self.scale), y, fill="gray")



    def paintDataPoint(self):
        ratio = self.line_distance
        for indexpoint,datapointindex in enumerate(self.GDatapoint.datapoint):
            indexx=datapointindex[0]
            indexy=datapointindex[1]
            colorpoint = self.GDatapoint.colorpoint[indexpoint]
            myrectangle = self.canvas3.create_rectangle(indexx*self.scale, indexy*self.scale, indexx*self.scale+(ratio*self.scale),indexy*self.scale+(ratio*self.scale), fill='black')
            self.canvas3.itemconfig(myrectangle, fill=colorpoint)
            
