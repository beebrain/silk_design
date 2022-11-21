from ast import Delete
from asyncio import events
from cgitb import text
import os
from pickletools import string1
from re import T
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
#import numpy as np
import pickle
from turtle import onclick, position
from webbrowser import get
from cv2 import scaleAdd
import Datapoint as Dp
import ChildClass as CCD
import ChildCanvas as CCV
# import Previewpic as PRV
import Datapoint as DP

from scipy import misc
from PIL import ImageTk, Image, ImageDraw
import numpy as np
import cv2
import glob
from tkinter import colorchooser,filedialog
import os,sys
from fpdf import FPDF
# import win32print
# import win32api
import tempfile
from tkinter.messagebox import showinfo
from win32api import GetSystemMetrics
from tkPDFViewer import tkPDFViewer as pdf
from scipy.ndimage import rotate
import math
#from screeninfo import get_monitors
from os import listdir
from os.path import isfile, join
import numpy
import cv2
#for m in get_monitors():
#    print(str(m))
import cv2 as cv


PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "GUI Test.ui")

class GuiTestApp:
    def __init__(self, master=None):
        # build ui
        self.titleData = "untitle.pkl"
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.title("Silk Design Program - {}".format(self.titleData))
        width= self.toplevel1.winfo_screenwidth()
        height= self.toplevel1.winfo_screenheight()
        #setting tkinter window size
        self.toplevel1.geometry("%dx%d" % (width,height))
        
        self.scale = 8
        self.scale_int = 8
        
        #canvas Parameter
        self.canvas_width = 1200     
        self.canvas_height = 768

        self.width = 50 
        self.height = 50 
        #CanvasDraw
        self.canvas_draw_width = 50*self.scale
        self.canvas_draw_height = 50*self.scale

        self.canvasMini_height =10
        self.canvasMini_width =10

        
        self.frame1 = ttk.Frame(self.toplevel1)
        
        self.canvasMain = tk.Canvas(self.frame1, bd=0)
        #self.canvasMain2 = tk.Canvas(self.canvasMain)
        #self.toplevel1.attributes("-fullscreen", True)

        
        
        
        self.canvasMain.configure(background='#FFFFFF', borderwidth='0', closeenough='1', confine='true')
        self.canvasMain.configure( highlightcolor='#100000', insertwidth='0')
        self.canvasMain.configure()
        self.canvasMain.grid(column='0', row='0')
        self.canvasMain.grid(row='0', column='0')
        
        
    
        #Scroll bar 
        frame=Frame(self.canvasMain)
        frame.pack(expand = True, fill=BOTH)

        #self.canvasMain = Canvas(frame,bg='white',height=self.canvas_draw_height,width=self.canvas_draw_width,
        self.canvasMain = Canvas(frame,bg='white',height=self.canvas_height,width=self.canvas_width,
                    scrollregion=(0,0,self.canvas_draw_width*self.scale,self.canvas_draw_height*self.scale))
        
        
        hbar = Scrollbar(frame,orient = HORIZONTAL)
        hbar.pack(side = BOTTOM, fill = X)
        hbar.config(command = self.canvasMain.xview)

        vbar = Scrollbar(frame,orient = VERTICAL)
        vbar.pack(side = RIGHT, fill = Y)
        vbar.config(command = self.canvasMain.yview)

        
        self.canvasMain.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvasMain.pack(side=LEFT, expand = True, fill = BOTH)
        


        self.frame1.configure()
        self.frame1.grid(column='0', padx='10', row='0', sticky='ne')
        self.frame3 = ttk.Frame(self.toplevel1)
        self.frame4 = ttk.Frame(self.frame3)
        self.canvasMini = tk.Canvas(self.frame4,bd=0)
        self.canvasMini.configure(background='#DDDDDD', height='100', width='100')
        self.canvasMini.grid(column='0', row='0')
        
        self.listbox1 = tk.Listbox(self.frame4)
        self.listbox1.configure(exportselection='true', height='5', width='20')
        self.listbox1.grid(column='0', row='1')
        self.scrollbar = tk.Scrollbar(self.frame4, orient="vertical",command=self.listbox1.yview)
        self.scrollbar.grid(column='1', row='1', ipady='20',sticky=N+S)
        self.listbox1.config(yscrollcommand=self.scrollbar.set)

        #ฟังก์ชั่นภาพย่อย
        self.LoadMini = ttk.Button(self.frame4)
        self.LoadMini.configure(text='โหลด', width='5')
        self.LoadMini.grid(column='0', ipadx='5', padx='5', row='2', sticky='nw')
        self.LoadMini.rowconfigure('2', minsize='0')
        self.CancelMini = ttk.Button(self.frame4)
        self.CancelMini.configure(text='ยกเลิก', width='7')
        self.CancelMini.grid(column='0', padx='5', row='2', sticky='ne')
        self.CancelMini.rowconfigure('2', minsize='0')
        self.frame4.configure(height='100', width='100')
        self.frame4.grid(column='0', row='5', sticky='n')
        
        
        self.frame6 = ttk.Frame(self.frame3)
        self.labelframe1 = ttk.Labelframe(self.frame6)
        self.New = ttk.Button(self.labelframe1)
        self.New.configure(text='สร้างใหม่', width='15',command=self.create_windowsBox)
        self.New.pack(side='top')
        self.button4 = ttk.Button(self.labelframe1)
        self.button4.configure(text='โหลดข้อมูลเดิม', width='15',command=self.openData)
        self.button4.pack(side='top')
        self.Save = ttk.Button(self.labelframe1)
        self.Save.configure(text='บันทึก', width='15',command=self.saveData)
        self.Save.pack(side='top')
        self.SaveAs = ttk.Button(self.labelframe1)
        self.SaveAs.configure(text='บันทึกเป็น', width='15',command=self.saveasData)
        self.SaveAs.pack(side='top')
        self.createTem = ttk.Button(self.labelframe1)
        self.createTem.configure(text='สร้างรูปย่อย', width='15')
        self.createTem.pack(side='top')
        self.colorSelect = ttk.Button(self.labelframe1)
        self.colorSelect.configure(text='เลือกสี', width='15')
        self.colorSelect.pack(side='top')
        self.printReport = ttk.Button(self.labelframe1)
        self.printReport.configure(text='Preview', width='15',command=self.reportExample)
        self.printReport.pack(side='top')
        #self.printReport1 = ttk.Button(self.labelframe1)
        #self.printReport1.configure(text='Previewlanscape', width='15',command=self.reportExamplelanscape)
        #self.printReport1.pack(side='top')
        # self.printReport1 = ttk.Button(self.labelframe1)
        # self.printReport1.configure(text='Print', width='15',command=self.locprinter)
        # self.printReport1.pack(side='top')
        
        self.pageimage = 1
        self.zoomin1 = ttk.Button(self.labelframe1)
        self.zoomin1.configure(text='zoom in', width='15',command=self.zoomin)
        self.zoomin1.pack(side='left')
        self.zoomout2 = ttk.Button(self.labelframe1)
        self.zoomout2.configure(text='zoom out', width='15',command=self.zoomout)
        self.zoomout2.pack(side='right')

        print("Width =", GetSystemMetrics(0))
        print("Height =", GetSystemMetrics(1))


        self.labelframe1.configure(height='100', labelanchor='nw', padding='20', relief='groove')
        self.labelframe1.configure(takefocus=True, text='เครื่องมือ', width='100')
        self.labelframe1.grid(column='0', columnspan='20', row='0', rowspan='20', sticky='e')
        self.frame6.configure(height='100', width='100')
        self.frame6.grid(column='0', row='6')
        self.frame3.configure(height='400', width='100')
        self.frame3.grid(column='1', row='0', sticky='ne')

        self.toplevel1.configure()
        self.toplevel1.resizable(True, True)
        #Tk.attributes("-fullscreen", False)
        # Main widget
        self.mainwindow = self.toplevel1
        
        # bind function
        self.canvasMain.bind( "<ButtonPress-1>", self.paintButton_Press)
        self.canvasMain.bind( "<B1-Motion>", self.paintButton_Move)
        # self.canvasMain.bind("<ButtonPress-1>", self.on_button_press)
        # self.canvasMain.bind("<B1-Motion>", self.on_move_press)
        self.canvasMain.bind("<ButtonRelease-1>", self.on_button_release)
        self.listbox1.bind("<<ListboxSelect>>", self.selectitem)
        self.canvasMain.bind("<Motion>", self.move_window)
        self.toplevel1.bind("<F11>", lambda event: self.toplevel1.attributes("-fullscreen",not self.toplevel1.attributes("-fullscreen")))
        self.toplevel1.bind("<Escape>", lambda event: self.toplevel1.attributes("-fullscreen", False))

        #bind colorbutton
        self.colorSelect['command'] = self.selectcolor
        self.colorSelect.pack()

        self.LoadMini['command'] = self.overLayImage
        self.CancelMini['command'] = self.cancleMode
        self.createTem['command'] = lambda: self.changemode(2)
        self.createTem.pack()

        

        ### image parameter
        self.moveImage = None
        self.FullImageBackground = None
        self.Fullthumnal = None
        self.Fullpreview =  None
        ## image array 
        self.ImageBackground = None
        self.thumnal = None
        self.preview = None
       

         # general parameter
        self.GdataPointObj = Dp.Datapoint()
        self.currentindexX = ""
        self.currentindexY = ""
        self.changemode(mode=1)

        #parameter rectangle draw
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.x = self.y = 0
        
        self.line_distance = 1
       
        ######## call init grid
        self.drawgrid()
        #### reloadListthermail image
        self.reloadListImage()
        #self.reloadListImagePreview()
        
        self.dataThum = None
    ################# This function for create sub Windows
    def cancleMode(self):
        self.canvasMain.delete("all")
        self.drawgrid()
        self.paintwithDataPoint()
        self.changemode(1)


    def create_windowsBox(self):
        self.kid = CCD.ChildClass(self)

    
       

    def move_window(self,event):
        event2canvas = lambda e, c: (c.canvasx(e.x), c.canvasy(e.y))
        if self.mode == 3:
            cx, cy = event2canvas(event, self.canvasMain)
            x,y = (int(cx),int(cy))
            self.window_data = self.thumnal.copy()
            ratio = self.line_distance*self.scale
            self.bg_img = self.ImageBackground.copy()
            
            ### find Current Index ตำแหน่งวางรูป
            indexx = (x//ratio)*ratio
            indexy = (y//ratio)*ratio
            
            positionx,positiony = indexx//self.scale,indexy//self.scale
            print(positionx,positiony)
            
            print(self.thumnal.shape[1]//self.scale,self.thumnal.shape[0]//self.scale)
           
            gpoint_np = np.array(self.GdataPointObj.datapoint)
            print(gpoint_np)
            if gpoint_np.size != 0:

                datainrange = gpoint_np[((\
                    gpoint_np >= [positionx, positiony]) \
                        & (gpoint_np <[positionx+self.thumnal.shape[1]//self.scale, positiony+self.thumnal.shape[0]//self.scale])).all(1)]
                
                print(datainrange)

                offset_data = datainrange-[positionx,positiony]
                for inx,overlaydata  in enumerate(datainrange):
                    
                    firstslice = int(overlaydata[1]*self.scale)
                    endslice = int(overlaydata[0]*self.scale)
                    sample = self.bg_img[firstslice:firstslice+self.scale,\
                        endslice:endslice+self.scale,\
                            :]
                    

                    offset = overlaydata-[positionx,positiony]
                    firstoffset = int(offset[1]*self.scale)
                    endoffset = int(offset[0]*self.scale)
                    self.window_data[firstoffset:firstoffset+self.scale,\
                        endoffset:endoffset+self.scale,:] = sample
                    
                    # cv2.imshow("{}".format(inx),sample)
                    # cv2.waitKey(1)


            # for idexbg in datainrange:
            #     self.window_data[]  = self.bg_img[idexbg[0]*self.scale:idexbg[0]*self.scale+self.scale,\
            #         idexbg[1:]*self.scale:idexbg[0]*self.scale+self.scale]

            if indexx+self.thumnal.shape[1] <= self.bg_img.shape[1] and indexy+self.thumnal.shape[0] <= self.bg_img.shape[0]:
                # print(self.window_data)
                self.bg_img[indexy:indexy+self.thumnal.shape[0],indexx:indexx+self.thumnal.shape[1]] = self.window_data

                shapes = np.zeros_like(self.bg_img, np.uint8)
    
            
                # Put the overlay at the bottom-right corner
               # shapes[y:y+self.window_data.shape[0],x:x+self.window_data.shape[1]] = self.window_data
                mask = shapes.astype(bool)
                #bg_img = background.copy()
                # Create the overlay
                # self.bg_img[mask] = cv2.addWeighted(self.bg_img, 1 - 0.1, shapes,
                                        # 0.5, 0)[mask]
                #cv2.imshow("s",self.bg_img)
                #cv2.waitKey(10)

                self.img = ImageTk.PhotoImage(Image.fromarray(self.bg_img))
                self.canvasMain.create_image(0, 0,image=self.img,anchor="nw")
                # self.ImageBackground = ImageBackground
               
            print("overlay end")





            
    ########### Main Function 
    def convertColor(self,colorCode):
        return (int(colorCode, 16))

    def regenImageWithData(self):
        self.ImageBackground = np.ones((self.canvas_draw_height,self.canvas_draw_width,3),dtype=np.uint8)*255
        for indexPoint,colorconvert in enumerate(self.GdataPointObj.colorpoint):
            color1 = self.convertColor(colorconvert[1:3])
            color2 = self.convertColor(colorconvert[3:5])
            color3 = self.convertColor(colorconvert[5:])
            x,y = self.GdataPointObj.datapoint[indexPoint]
            x,y = int(x),int(y)

            # color blackground
            self.ImageBackground[y*self.scale:(y*self.scale)+self.scale,x*self.scale:(x*self.scale)+self.scale,0] = color1
            self.ImageBackground[y*self.scale:(y*self.scale)+self.scale,x*self.scale:(x*self.scale)+self.scale,1] = color2
            self.ImageBackground[y*self.scale:(y*self.scale)+self.scale,x*self.scale:(x*self.scale)+self.scale,2] = color3
          
        color = (0, 0, 0)
        thickness = 1
       

        #draw grid พื้นหลัง balckground main canvas

        # vertical lines at an interval of "line_distance" pixel
        for x in range(0,self.canvas_draw_height*self.scale,self.line_distance*self.scale):
             self.ImageBackground = cv2.line(self.ImageBackground,(x, 0), ( x, self.canvas_draw_height), color, thickness)
        # horizontal lines at an interval of "line_distance" pixel
        for y in range(0,self.canvas_draw_width*self.scale,self.line_distance*self.scale):
             self.ImageBackground = cv2.line(self.ImageBackground,(0, y), (self.canvas_draw_width, y), color, thickness)

         

    def regenImageThumnal(self):
        color = (0, 0, 0)
        thickness = 1
        #draw grid
        # vertical lines at an interval of "line_distance" pixel

        ## resize thumnal with default size is 8
        org_x  = self.thumnal.shape[1]
        org_y  = self.thumnal.shape[0]
        scale_env = 8
        multiply_scale = self.scale / scale_env  
        self.thumnal = cv2.resize(self.thumnal,(int(org_x*multiply_scale),int(org_y*multiply_scale)))  

        for x in range(0,self.thumnal.shape[1],self.line_distance*self.scale):   
                self.thumnal = cv2.line(self.thumnal,(x, 0), ( x,self.thumnal.shape[0]), color, thickness)
        # horizontal lines at an interval of "line_distance" pixel
        for y in range(0,self.thumnal.shape[0],self.line_distance*self.scale):
                self.thumnal = cv2.line(self.thumnal,(0, y), (self.thumnal.shape[1], y), color, thickness)
            
                 
        self.thumnal = cv2.rectangle(self.thumnal,(0,0),(self.thumnal.shape[1],self.thumnal.shape[0]),\
             (0,0,0),2)


    def transparentOverlay(self,scr,overlay,pos=(0,0),scale = 1):
        h,w,_ = overlay.shape
        rows,cols,_ = scr.shape
        y,x = pos[0],pos[1]

        for i in range(h):
            for j in range(w):
                if x+i >=rows or y+j >= cols:
                    continue
                alpha = float(overlay[i][j][3]/255.0)
                scr[x+i][y+j] = alpha*overlay[:3]+(1-alpha)*scr[x+i][y+j]
        return scr
    

    def overLayImage(self):
        self.reloadImageTemp(self.dataThum)
        self.regenImageWithData()
        self.regenImageThumnal()
        # Here is where the mouse coordinates should be injected to move the window over the background image
        # self.window_data = self.thumnal 
        self.bg_img = self.ImageBackground.copy() 
        # Here is where the mouse coordinates should be injected to move the window over the background image
        # x,y = (100,200)

        
        # self.window_data = self.transparentOverlay(self.bg_img[y:y+self.window_data.shape[0],x:x+self.window_data.shape[1]],self.window_data)
        
        
        # self.bg_img[y:y+self.window_data.shape[0],x:x+self.window_data.shape[1]] = self.window_data
        self.img = ImageTk.PhotoImage(Image.fromarray(self.bg_img))
        ### disable All button
        print("Overlay function")
        self.changemode(mode=3)
        self.canvasMain.update()




    def drawgrid(self):
        #self.canvasMain.config(width=self.canvas_draw_width, height=self.canvas_draw_width)
        self.canvasMain.delete("all")
        # vertical lines at an interval of "line_distance" pixel
        for x in range(0,int(self.canvas_draw_width),int(self.line_distance*self.scale)):
            if x%(5*self.scale) == 0:
               self.canvasMain.create_line(x, 0, x, int(self.canvas_draw_height), fill="black")
            else: 
                self.canvasMain.create_line(x, 0, x, int(self.canvas_draw_height), fill="gray")
        # horizontal lines at an interval of "line_distance" pixel
        for y in range(0,int(self.canvas_draw_height),int(self.line_distance*self.scale)):
            if y%(5*self.scale) == 0:
               self.canvasMain.create_line(0, y, int(self.canvas_draw_width), y, fill="black")
            else: 
                self.canvasMain.create_line(0, y, int(self.canvas_draw_width), y, fill="gray")
        self.canvasMain.update()




    def selectcolor(self):
        my_clolor = colorchooser.askcolor()
        #    dataPointObj.currentColor = my_clolor[1]
        #print(my_clolor)
        self.GdataPointObj.currentColor = my_clolor[1]

    def changemode(self,mode=1):  
        self.mode= mode
        if self.mode == 3:
            self.button4['state'] = tk.DISABLED
            self.Save['state'] = tk.DISABLED
            self.createTem['state'] = tk.DISABLED
            self.colorSelect['state'] = tk.DISABLED
            self.SaveAs['state'] = tk.DISABLED
            self.New['state'] = tk.DISABLED
            self.printReport['state'] = tk.DISABLED
            #self.printReport1['state'] = tk.DISABLED
            self.zoomin1['state'] = tk.DISABLED
            self.zoomout2['state'] = tk.DISABLED
        elif self.mode == 2:
            self.button4['state'] = tk.DISABLED
            self.Save['state'] = tk.DISABLED
            self.createTem['state'] = tk.DISABLED
            self.colorSelect['state'] = tk.DISABLED
            self.New['state'] = tk.DISABLED
            self.LoadMini['state'] = tk.DISABLED
            self.CancelMini['state'] = tk.NORMAL
            self.SaveAs['state'] = tk.DISABLED
            self.printReport['state'] = tk.DISABLED
            #self.printReport1['state'] = tk.DISABLED
            self.zoomin1['state'] = tk.DISABLED
            self.zoomout2['state'] = tk.DISABLED
        elif self.mode == 1:
            
            self.button4['state'] = tk.NORMAL
            self.Save['state'] = tk.NORMAL
            self.createTem['state'] = tk.NORMAL
            self.colorSelect['state'] = tk.NORMAL
            self.New['state'] = tk.NORMAL
            self.SaveAs['state'] = tk.NORMAL
            self.LoadMini['state'] = tk.NORMAL
            self.CancelMini['state'] = tk.NORMAL
            self.printReport['state'] = tk.NORMAL
            #self.printReport1['state'] = tk.NORMAL
            self.zoomin1['state'] = tk.NORMAL
            self.zoomout2['state'] = tk.NORMAL
            

    def saveMenu_click(self):
        self.saveData(self.GdataPointObj)

    ### general function 
    def showinfo(self, title, message):
        self.title("xxxx")

    def saveasData(self): 
        data = [('pkl', '*.pkl')]
        filesave = filedialog.asksaveasfile(filetypes=data,defaultextension='pkl',initialfile ='untitle')
        print(filesave)
        if (filesave != None): 
            self.GdataPointObj.setfilename(filesave.name)
            with open(filesave.name, 'wb') as output:
                pickle.dump(self.GdataPointObj, output, pickle.HIGHEST_PROTOCOL)
            
            (filename, ext) = os.path.splitext(os.path.basename(self.GdataPointObj.getfilename()))
            self.toplevel1.title("Skill Design Program - {}.pkl".format(filename))

            filesave.close()

    def saveData(self):
        if self.GdataPointObj.getfilename() != "":
                with open(self.GdataPointObj.getfilename(), 'wb') as output:
                    pickle.dump(self.GdataPointObj, output, pickle.HIGHEST_PROTOCOL)

                (filename, ext) = os.path.splitext(os.path.basename(self.GdataPointObj.getfilename()))
                self.toplevel1.title("Skill Design Program - {}.pkl".format(filename))
        else:
                self.saveasData()

    def openData(self):
        data = [('pkl', '*.pkl')]
        fileopen = filedialog.askopenfile(filetypes=data,defaultextension='pkl')
        print(fileopen.name)

        if (fileopen != None): 
            with open(fileopen.name, 'rb') as input:
                dataPointObj = pickle.load(input)
                print(dataPointObj.datapoint)  
                print(dataPointObj.colorpoint) 
                # master.title( "Painting using Ovals" )
                ## call reprint dataporint 
                self.GdataPointObj=dataPointObj
                print(self.GdataPointObj.datapoint)
                fileopen.close()
                #list
                #numpy libery
                self.canvasMain.delete("all")
                self.canvas_draw_height = self.GdataPointObj.height
                self.canvas_draw_width = self.GdataPointObj.width

                self.drawgrid()
                self.paintwithDataPoint()
                (filename, ext) = os.path.splitext(os.path.basename(fileopen.name))
                self.toplevel1.title("Skill Design Program - {}.pkl".format(filename))

    def newsheet(self):
        self.paintwithDataPoint(fixcolor=True)
        self.GdataPointObj = Dp.Datapoint()
        self.GdataPointObj.height = self.canvas_draw_height
        self.GdataPointObj.width = self.canvas_draw_width
        self.canvasMain.update()

    ## print datapoint
    def paintwithDataPoint(self,fixcolor=False):
        ratio = self.line_distance
        for indexpoint,datapointindex in enumerate(self.GdataPointObj.datapoint):    
            indexx=datapointindex[0]
            indexy=datapointindex[1]
            colorpoint = self.GdataPointObj.colorpoint[indexpoint]
            if fixcolor:
                colorpoint = "#FFFFFF" 
            #print("scale",self.scale)
           
        #    myrectangle = self.canvasMain.create_rectangle(1079.0,1081.0, 1100.0+(ratio*self.scale), 1100.0+(ratio*self.scale), fill='black')
            myrectangle = self.canvasMain.create_rectangle((indexx*self.scale), indexy*self.scale, indexx*self.scale+(ratio*self.scale),indexy*self.scale+(ratio*self.scale), fill='black')
            self.canvasMain.itemconfig(myrectangle, fill=colorpoint)

    """
    def paintwithDataPoint2(self,fixcolor=False):
        ratio = 10
        for indexpoint,datapointindex in enumerate(self.GdataPointObj.datapoint): 
            (indexx)=datapointindex[0]
            (indexy)=datapointindex[1]
            colorpoint = self.GdataPointObj.colorpoint[indexpoint]
            if fixcolor:
                colorpoint = "#FFFFFF"
           #print("scale",self.scale)
        #    myrectangle = self.canvasMain.create_rectangle(1079.0,1081.0, 1100.0+(ratio*self.scale), 1100.0+(ratio*self.scale), fill='black')
            if self.scale ==1 :
                indexx//2
                indexy//2
                #print("Scale6666",self.scale)
            myrectangle = self.canvasMain.create_rectangle(indexx//2, indexy//2, indexx//2+(ratio*self.scale),indexy//2+(ratio*self.scale), fill='black')
            self.canvasMain.itemconfig(myrectangle, fill=colorpoint)
    """

    def clearCanvas(self,start=(0,0),width=30,height=50):
        ratio = self.line_distance*self.scale
        for x in range(int(start[0]),int(start[0])+width,self.line_distance*self.scale):
            for y in range(int(start[1]),int(start[1])+height,self.line_distance*self.scale):
                if [x,y] in self.GdataPointObj.datapoint:
                    indexofList = self.GdataPointObj.datapoint.index([x,y])
                    del self.GdataPointObj.datapoint[indexofList]
                    del self.GdataPointObj.colorpoint[indexofList]
                myrectangle = self.canvasMain.create_rectangle(x,y, x+(ratio),y+(ratio), fill='red')
                self.canvasMain.itemconfig(myrectangle, fill='white')
                
                

    def paintButton_Move(self,event):

        ## for draw mega pixel
        ratio = self.line_distance*self.scale
        
        x = self.canvasMain.canvasx(event.x)
        y = self.canvasMain.canvasy(event.y)
        indexx = (x//ratio)*ratio
        indexy = (y//ratio)*ratio
        if x >= self.canvas_draw_width-1:
            indexx = (((self.canvas_draw_width-1))*ratio)*self.scale 
        if y >= self.canvas_draw_height-1:
            indexy = (((self.canvas_draw_height-1)//ratio)*ratio)*self.scale 
            
        
        if self.mode == 1:
            ## for draw mega pixel
            current_color = self.GdataPointObj.currentColor
            print(event.x,event.y)
            #print("curcer {},{} index {},{} current {},{}".format(x,y,indexx,indexy,self.currentindexX,self.currentindexY))


            dataPoint = self.GdataPointObj.datapoint
            indexx_s1,indexy_s1 = indexx//self.scale,indexy//self.scale
            if [indexx_s1,indexy_s1] in dataPoint:
                print( indexx,indexy)         ### It filled
                print(self.currentindexX)
                ### filled white color and remove indexx, indexy
                if str(event.type) == "6" and (self.currentindexX != indexx or self.currentindexY != indexy):
                    indexofList = dataPoint.index([indexx_s1,indexy_s1])
                    del self.GdataPointObj.datapoint[indexofList]
                    del self.GdataPointObj.colorpoint[indexofList]

                    
                    myrectangle = self.canvasMain.create_rectangle(indexx,indexy, indexx+(ratio),indexy+(ratio), fill='black')
                    self.canvasMain.itemconfig(myrectangle, fill='white')
            else:
                if str(event.type) == "6" and (self.currentindexX != indexx or self.currentindexY != indexy):
                    self.GdataPointObj.datapoint +=[[indexx_s1,indexy_s1]] ## new filled
                    self.GdataPointObj.colorpoint+=[self.GdataPointObj.currentColor]
                    myrectangle = self.canvasMain.create_rectangle(indexx,indexy, indexx+(ratio),indexy+(ratio), fill='black')
                    self.canvasMain.itemconfig(myrectangle, fill=current_color)
            
            #print(self.GdataPointObj.datapoint)

        elif self.mode ==2: # draw rectangle mode
            
            
            if x >= self.canvas_draw_width-1:
                indexx = (((self.canvas_draw_width-1))*ratio)*self.scale 
            if y >= self.canvas_draw_height-1:
                indexy = (((self.canvas_draw_height-1)//ratio)*ratio)*self.scale


            curX = self.canvasMain.canvasx(indexx)
            curY = self.canvasMain.canvasy(indexy)
            w, h = self.canvasMain.winfo_width(), self.canvasMain.winfo_height()
            # expand rectangle as you drag the mouse
            self.canvasMain.coords(self.rect, self.start_x, self.start_y, curX, curY) 
        self.currentindexX = indexx
        self.currentindexY = indexy

    def paintButton_Press(self,event):
        ## for draw mega pixel
        
        ratio = self.line_distance*self.scale

        x = self.canvasMain.canvasx(event.x)
        y = self.canvasMain.canvasy(event.y)

        #print("canvaspoint1 = {},{}".format(self.canvasMain.canvasx(x)//self.scale,self.canvasMain.canvasy(y)//self.scale))

        indexx = (x//ratio)*ratio
        indexy = (y//ratio)*ratio
        if x >= self.canvas_draw_width-1:
            indexx = (((self.canvas_draw_width-1))*ratio)*self.scale 
        if y >= self.canvas_draw_height-1:
            indexy = (((self.canvas_draw_height-1)//ratio)*ratio)*self.scale 
            
        if self.mode == 1:
            current_color = self.GdataPointObj.currentColor
         
           # print("curcer {},{} index {},{} current {},{}".format(x,y,indexx,indexy,self.currentindexX,self.currentindexY))


            dataPoint = self.GdataPointObj.datapoint
            indexx_s1,indexy_s1 = indexx//self.scale,indexy//self.scale
            if [indexx_s1,indexy_s1] in dataPoint:
                #print( indexx_s1,indexy_s1)         ### It filled
                ### filled white color and remove indexx, indexy

                if (str(event.type) == "4"): #Button Press
                    indexofList = dataPoint.index([indexx_s1,indexy_s1])
                    del self.GdataPointObj.datapoint[indexofList]
                    del self.GdataPointObj.colorpoint[indexofList]

                    myrectangle = self.canvasMain.create_rectangle(indexx,indexy, indexx+(ratio),indexy+(ratio), fill='black')
                    self.canvasMain.itemconfig(myrectangle, fill='white')
            else:
                if str(event.type) == "4":
                    self.GdataPointObj.datapoint +=[[indexx_s1,indexy_s1]] ## new filled
                    self.GdataPointObj.colorpoint+=[self.GdataPointObj.currentColor]
                    myrectangle = self.canvasMain.create_rectangle(indexx,indexy, indexx+(ratio),indexy+(ratio), fill='black')
                    self.canvasMain.itemconfig(myrectangle, fill=current_color)

            #print(self.GdataPointObj.datapoint)
            
        elif self.mode == 2: # draw rec mode
            self.start_x = self.canvasMain.canvasx(indexx)+2
            self.start_y = self.canvasMain.canvasy(indexy)+2

            # create rectangle if not yet exist
            if not self.rect:
                self.rect = self.canvasMain.create_rectangle(self.x, self.y, 0, 0, outline='red',width=2)
        elif self.mode == 3:
            #### replace data to mainCanvas
            indexx = (x//self.scale)
            indexy = (y//self.scale)
            print("Helloooo")
            # self.clearCanvas(start=(indexx,indexy),width=self.MiniGDataPoint.width,height=self.MiniGDataPoint.height)
            array_temp = np.array(self.MiniGDataPoint.datapoint)
            array_temp[:,:] =array_temp[:,:] + np.array([indexx,indexy])
            array_temp = array_temp.astype(np.int)
            miniDatapoint = array_temp.tolist()

            

            #tocheck dupicate
            for indexpoint,minidata in enumerate(miniDatapoint):
                datapoint = np.array(self.GdataPointObj.datapoint)
                mininp = np.array(minidata)
                miniDatapointcolor = self.MiniGDataPoint.colorpoint

                if datapoint.size == 0:
                    self.GdataPointObj.datapoint += [minidata]
                    self.GdataPointObj.colorpoint += [miniDatapointcolor[indexpoint]]
                    continue
                
                col0m = (datapoint[:,0]==mininp[0])
                col1m = (datapoint[:,1]==mininp[1])
                if (col0m & col1m).any():
                    print("Found")
                else:
                    print("not Found")
                    self.GdataPointObj.datapoint += [minidata]
                    self.GdataPointObj.colorpoint += [miniDatapointcolor[indexpoint]]
                


                
            self.canvasMain.delete("all")
            self.drawgrid()
            self.paintwithDataPoint()
            self.changemode(mode=1)
            
        self.currentindexX = indexx
        self.currentindexY = indexy
            
    def on_button_release(self,event):
        if self.mode == 2:
            self.changemode(mode=1)

            self.canvasMain.coords(self.rect, 0, 0, 0, 0) 

            self.kid_canvas = CCV.ChildCanvas(self)

            startX = min(self.start_x//self.scale,self.currentindexX//self.scale)
            startY = min(self.start_y//self.scale,self.currentindexY//self.scale)
            endX = max(self.start_x//self.scale,self.currentindexX//self.scale)
            endY = max(self.start_y//self.scale,self.currentindexY//self.scale)
            endX = endX
            endY = endY
            tempData = []
            tempColor = []
            for indexPoint,(x,y) in enumerate(self.GdataPointObj.datapoint):
                if  x >= startX and x < endX and y>=startY and y<endY:
                    tempData += [[x-startX,y-startY]]         ## with Reindexing
                    tempColor += [self.GdataPointObj.colorpoint[indexPoint]]
            dwidth = int(endX - startX)
            dheight  = int(endY - startY)
        #   print(dwidth,dheight)
            self.kid_canvas.canvas_width = dwidth
            self.kid_canvas.canvas_height = dheight
            self.canvasMini_width = dwidth
            self.canvasMini_height = dheight
           # print(self.kid_canvas.scale)
            self.kid_canvas.canvasDrawGrid(tempData,tempColor)
            self.kid_canvas.paintDataPoint()      

        # ------------------------------ หน้าต่างแสดงตัวอย่างภาพย่อยที่บันทึกแล้ว -------------------------------------
    def redrawCanvasMini(self):
        # self.canvasMini.config(width=100, height=100)
        # self.canvasMini.config(height=self.canvasMini_height,width=self.canvasMini_width)
        #self.scale = 8
        print(self.Fullthumnal.width())
        print(self.Fullthumnal.height())
        self.canvasMini.configure(background='#FFFFFF', height=self.Fullthumnal.height(), width=self.Fullthumnal.width())
        self.canvasMini.create_image(0,0, anchor=NW, image=self.Fullthumnal)     
        

        # vertical lines at an interval of "line_distance" pixel
        for x in range(0,self.Fullthumnal.width()*8,self.line_distance*8):
            if x%(5*8) == 0:
                self.canvasMini.create_line(x, 0, x, self.Fullthumnal.height()*8, fill="black")
            else: 
                self.canvasMini.create_line(x, 0, x, self.Fullthumnal.height()*8, fill="gray")

        for y in range(0,self.Fullthumnal.height()*8,int(self.line_distance*8)):
            if y%(5*8) == 0:
               self.canvasMini.create_line(0, y, self.Fullthumnal.width()*8, y, fill="black")
            else: 
                self.canvasMini.create_line(0, y, self.Fullthumnal.width()*8, y, fill="gray")





    def reloadImageTemp(self,fileData):
        with open("./ImageMini/{}.pk".format(fileData), 'rb') as input:
            self.thumnal = pickle.load(input)
            #print(self.thumnal)

            img = ImageTk.PhotoImage(Image.fromarray(self.thumnal))
            self.Fullthumnal = img
        
        with open("./ImageMini/R_{}.pk".format(fileData), 'rb') as input:
            self.MiniGDataPoint = pickle.load(input)

        self.redrawCanvasMini()
        







    def selectitem(self,event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            self.dataThum = event.widget.get(index)
            print(self.dataThum )
            #### reload  Data Items
            self.reloadImageTemp(self.dataThum )
        else:
            print("No Data")





    def reloadListImage(self):  
        if os.path.isdir("ImageMini"):
            listFile = os.listdir("ImageMini")
            listFile=glob.glob("ImageMini/Image*.pk")
                # clear listbox
            self.listbox1.delete(0, 'end')
            for filename in listFile:
                (file, ext) = os.path.splitext(os.path.basename(filename))
                self.listbox1.insert(END, file) 
        else:
            os.makedirs("ImageMini")
            with open("ImageMini/IndexImage.txt","w") as readIndex:
                readIndex.write("{:04d}".format(0))







    def reportExample(self):
       # self.overLaypreview()
        
        #b = Preview.Preview(self.GdataPointObj,self.canvas_draw_height,self.canvas_draw_width)
         
        #self.canvaspreview = PRV.Previewpic(self)
        #c = Report.Report(self.GdataPointObj,self.canvas_draw_height,self.canvas_draw_width)
    
        #Window Preview
        
        # if os.path.exists("preview"):
        #     os.removedirs("preview")
        for i in os.listdir("./preview"):
            os.remove("./preview/{}".format(i))

        self.toplevel = tk.Toplevel()
        self.toplevel.title("preview")    
        width= 1000
        height= 1000
        self.toplevel.geometry("%dx%d" % (width,height))
        self.toplevel.configure()
        self.toplevel.resizable(True, True)

        #Button
        self.button1 = tk.Button(self.toplevel)
        self.button1.configure(text='บันทึกpdf')
        self.button1.grid(column='0', row='2', sticky='nw')
        self.button1['command'] = self.exportpdf
        self.button1 = tk.Button(self.toplevel)
        self.button2 = tk.Button(self.toplevel)
        self.button2.configure(text='แนวนอน')
        self.button2.grid(column='2', row='2', sticky='nw')
        self.button2['command'] = self.reportexaplelanscape
        self.button2 = tk.Button(self.toplevel)
        self.buttonnext = tk.Button(self.toplevel)
        self.buttonnext.configure(text='ถัดไป')
        self.buttonnext.grid(column='5', row='2', sticky='nw')
        self.buttonnext['command'] = self.next
        self.buttonback = tk.Button(self.toplevel)
        self.buttonback.configure(text='ก่อนหน้า')
        self.buttonback.grid(column='4', row='2', sticky='nw')
        self.buttonback['command'] = self.back
        
        


        #  #Label
        self.labelpreview = tk.LabelFrame(self.toplevel)
        self.labelpreview.configure(height=750 , takefocus=True, text='แนวตั้ง'.format(self.pageimage),width=570)
        self.labelpreview.grid(column='5', row='3')
        
        # self.button1 = tk.Button(self.toplevel)
        # self.button1.configure(text='บันทึกpdf')
        # self.button1.grid(column='0', row='2', sticky='nw')
        # self.button1['command'] = self.exportpdf
        # self.button1 = tk.Button(self.toplevel)
         
        #scrollbar
       



        #canvas
        self.canvaspreview = tk.Canvas(self.labelpreview)
        self.canvaspreview.place(relwidth=1, relheight=1)
        paperheigth = self.toplevel.winfo_fpixels('1m') * 297
        paperwidth = self.toplevel.winfo_fpixels('1m') * 210
        self.canvaspreview.create_rectangle(15, 10, 10+paperwidth, 20+paperheigth, outline='', fill='white')
        #self.canvaspreview.create_text(5, 5, text="self.pageimage", fill="gray", font=('Helvetica  '))
        
        
        

       
      
        
        setMaxwidth = 950
        setMaxheight = 1350
        draw_height = self.canvas_draw_height//8 *10
        draw_width = self.canvas_draw_width // 8 * 10
        

        self.pageImagee = 0
        for row in range(math.ceil(draw_height / setMaxheight)):
            for col in range(math.ceil(draw_width / setMaxwidth)):
                if draw_width > 0  <= setMaxwidth:
                    DatapointSavepic = np.ones((draw_height,draw_width,3),dtype=np.uint8)*255        
                    for indexPoint,colorconvert in enumerate(self.GdataPointObj.colorpoint):
                        color1 = self.convertColor(colorconvert[1:3])
                        color2 = self.convertColor(colorconvert[3:5])
                        color3 = self.convertColor(colorconvert[5:])
                        x,y =self.GdataPointObj.datapoint[indexPoint]
                        x,y = int(x),int(y)
                        
                        xmin = col*setMaxwidth//10
                        ymin = row*setMaxheight // 10
                        print(col*setMaxwidth//10 , row*setMaxheight // 10)
                        print(col*setMaxwidth//10 + setMaxwidth//10 -1, row*setMaxheight // 10 + setMaxheight//10 -1)
                        # print(col*setMaxwidth//10,min(setMaxwidth,self.canvas_draw_width-(setMaxwidth*col))//10)
                        if xmin <= x <xmin + setMaxwidth//10 and ymin <= y < ymin + setMaxheight//10 :
                            print(x,y)
                            DatapointSavepic[(y-ymin)*10:((y-ymin)*10)+10,(x-xmin)*10:((x-xmin)*10)+10,0] = color3
                            DatapointSavepic[(y-ymin)*10:((y-ymin)*10)+10,(x-xmin)*10:((x-xmin)*10)+10,1] = color2
                            DatapointSavepic[(y-ymin)*10:((y-ymin)*10)+10,(x-xmin)*10:((x-xmin)*10)+10,2] = color1

                    color = (0, 0, 0)
                    thickness = 1
                    for x in range(0,min(setMaxwidth,draw_width-(setMaxwidth*col))+10,10):
                        DatapointSavepic = cv2.line(DatapointSavepic,(x, 0), ( x, min(setMaxheight,draw_height-(setMaxheight*row))), color, thickness)
                        # horizontal lines at an interval of "line_distance" pixel
                    for y in range(0,min(setMaxheight,draw_height-(setMaxheight*row))+10,10):
                        DatapointSavepic = cv2.line(DatapointSavepic,(0, y), (min(setMaxwidth,draw_width-(setMaxwidth*col)), y), color, thickness)
                    
                    if not os.path.exists("preview"):
                        os.makedirs("preview")
                    self.pageImagee += 1
                    cv2.imwrite("./preview/image_{}.jpg".format( self.pageImagee),DatapointSavepic)
                    

      
    
        filename = "image_{}.jpg".format(1)
        filepath = f"./preview/{filename}"

        # Load the original image, and get its size and color mode.
        #img= (Image.open(filepath))     
        image=Image.open(filepath)  
        # Resize the image in the given (width, height)
        img=image.resize((self.canvas_draw_width//2+100, self.canvas_draw_height//2+100))

        # Conver the image in TkImage
        my_img=ImageTk.PhotoImage(img)   
        self.canvaspreview.create_image(45,45,anchor=NW,image=my_img)
        self.canvaspreview.create_text(10, 10, text=self.pageimage, fill="gray", font=('Helvetica 10 '))

        #อาจจะดูงงๆหน่อยครับ แต่ใช้งานได้ครับ 555
        if self.pageImagee == 1 :
            self.buttonnext['state'] = tk.DISABLED
            self.buttonback['state'] = tk.DISABLED
        if self.pageimage == 1 :
            
            self.buttonback['state'] = tk.DISABLED   

        if self.pageimage >= 2 < self.pageImagee:
            self.buttonnext['state'] = tk.NORMAL
            self.buttonback['state'] = tk.NORMAL
        
        print("pageimagee",self.pageImagee)
        print("pageimage",self.pageimage)
        print("row",row)
        self.toplevel2.destroy()
        self.toplevel.mainloop()

    def reportexaplelanscape(self):
        
        for i in os.listdir("./preview1"):
            os.remove("./preview1/{}".format(i))
        self.toplevel2 = tk.Toplevel()
        self.toplevel2.title("preview")    
        width= 1000
        height= 1000
        self.toplevel2.geometry("%dx%d" % (width,height))
        self.toplevel.configure()
        self.toplevel2.resizable(True, True)
        self.button1 = tk.Button(self.toplevel2)
        self.button1.configure(text='บันทึกpdf')
        self.button1.grid(column='0', row='2', sticky='nw')
        self.button1['command'] = self.exportpdflanscape
        self.button1 = tk.Button(self.toplevel2)
        self.button2 = tk.Button(self.toplevel2)
        self.button2.configure(text='แนวตั้ง')
        self.button2.grid(column='2', row='2', sticky='nw')
        self.button2['command'] = self.reportExample
        self.button2 = tk.Button(self.toplevel2)
        self.buttonnext = tk.Button(self.toplevel2)
        self.buttonnext.configure(text='ถัดไป')
        self.buttonnext.grid(column='5', row='2', sticky='nw')
        self.buttonnext['command'] = self.next1
        self.buttonback = tk.Button(self.toplevel2)
        self.buttonback.configure(text='ก่อนหน้า')
        self.buttonback.grid(column='4', row='2', sticky='nw')
        self.buttonback['command'] = self.back1
       


        #  #Label
        self.labelpreview1 = tk.LabelFrame(self.toplevel2)
        self.labelpreview1.configure(height=570 , takefocus=True, text='แนวนอน'.format(self.pageimage),width=750)
        self.labelpreview1.grid(column='5', row='3')
        
        # self.button1 = tk.Button(self.toplevel)
        # self.button1.configure(text='บันทึกpdf')
        # self.button1.grid(column='0', row='2', sticky='nw')
        # self.button1['command'] = self.exportpdf
        # self.button1 = tk.Button(self.toplevel)
         
        #scrollbar
       



        #canvas
        self.canvaspreview = tk.Canvas(self.labelpreview1)
        self.canvaspreview.place(relwidth=1, relheight=1)
        paperheigth = self.toplevel2.winfo_fpixels('1m') * 210
        paperwidth = self.toplevel2.winfo_fpixels('1m') * 297
        self.canvaspreview.create_rectangle(15, 10, 10+paperwidth, 20+paperheigth, outline='', fill='white')
        # self.canvaspreview.create_text(240, 20, text="Silk Design Program", fill="gray", font=('Helvetica 10 '))
        

                
        setMaxwidth = 1350
        setMaxheight = 950
        draw_height = self.canvas_draw_height//8 *10
        draw_width = self.canvas_draw_width // 8 * 10
        

        self.pageImagee = 0
        for row in range(math.ceil(draw_height / setMaxheight)):
            for col in range(math.ceil(draw_width / setMaxwidth)):
                if draw_width > 0  <= setMaxwidth:
                    DatapointSavepic = np.ones((draw_height,draw_width,3),dtype=np.uint8)*255        
                    for indexPoint,colorconvert in enumerate(self.GdataPointObj.colorpoint):
                        color1 = self.convertColor(colorconvert[1:3])
                        color2 = self.convertColor(colorconvert[3:5])
                        color3 = self.convertColor(colorconvert[5:])
                        x,y =self.GdataPointObj.datapoint[indexPoint]
                        x,y = int(x),int(y)
                        
                        xmin = col*setMaxwidth//10
                        ymin = row*setMaxheight // 10
                        print(col*setMaxwidth//10 , row*setMaxheight // 10)
                        print(col*setMaxwidth//10 + setMaxwidth//10 -1, row*setMaxheight // 10 + setMaxheight//10 -1)
                        # print(col*setMaxwidth//10,min(setMaxwidth,self.canvas_draw_width-(setMaxwidth*col))//10)
                        if xmin <= x <xmin + setMaxwidth//10 and ymin <= y < ymin + setMaxheight//10 :
                            print(x,y)
                            DatapointSavepic[(y-ymin)*10:((y-ymin)*10)+10,(x-xmin)*10:((x-xmin)*10)+10,0] = color3
                            DatapointSavepic[(y-ymin)*10:((y-ymin)*10)+10,(x-xmin)*10:((x-xmin)*10)+10,1] = color2
                            DatapointSavepic[(y-ymin)*10:((y-ymin)*10)+10,(x-xmin)*10:((x-xmin)*10)+10,2] = color1

                    color = (0, 0, 0)
                    thickness = 1
                    for x in range(0,min(setMaxwidth,draw_width-(setMaxwidth*col))+10,10):
                        DatapointSavepic = cv2.line(DatapointSavepic,(x, 0), ( x, min(setMaxheight,draw_height-(setMaxheight*row))), color, thickness)
                        # horizontal lines at an interval of "line_distance" pixel
                    for y in range(0,min(setMaxheight,draw_height-(setMaxheight*row))+10,10):
                        DatapointSavepic = cv2.line(DatapointSavepic,(0, y), (min(setMaxwidth,draw_width-(setMaxwidth*col)), y), color, thickness)
                    
                    if not os.path.exists("preview1"):
                        os.makedirs("preview1")
                    self.pageImagee += 1
                    cv2.imwrite("./preview1/image_{}.jpg".format( self.pageImagee),DatapointSavepic)



        filename = "image_{}.jpg".format(1)
        filepath = f"./preview1/{filename}"

        image=Image.open(filepath)  
        # Resize the image in the given (width, height)
        img=image.resize((self.canvas_draw_width//2+100, self.canvas_draw_height//2+100))

        # Conver the image in TkImage
        my_img=ImageTk.PhotoImage(img)   
        self.canvaspreview.create_image(45,45,anchor=NW,image=my_img)

        #อาจจะดูงงๆหน่อยครับ แต่ใช้งานได้ครับ 555
        if self.pageImagee == 1 :
            self.buttonnext['state'] = tk.DISABLED
            self.buttonback['state'] = tk.DISABLED
        if self.pageimage == 1 :
            
            self.buttonback['state'] = tk.DISABLED   

        if self.pageimage >= 2 < self.pageImagee:
            self.buttonnext['state'] = tk.NORMAL
            self.buttonback['state'] = tk.NORMAL
        
        print("pageimagee",self.pageImagee)
        print("pageimage",self.pageimage)
        print("row",row) 
        self.toplevel.destroy()     
        self.toplevel2.mainloop()
        
    def next(self):
        
        self.pageimage = self.pageimage +1
        self.canvaspreview.delete("all")
        if self.pageimage == self.pageImagee:
            self.buttonnext['state'] = tk.DISABLED
            self.buttonback['state'] = tk.NORMAL
        if self.pageimage >= 2 < self.pageImagee:
            
            self.buttonback['state'] = tk.NORMAL
         #canvas
        self.canvaspreview = tk.Canvas(self.labelpreview)
        self.canvaspreview.place(relwidth=1, relheight=1)
        paperheigth = self.toplevel.winfo_fpixels('1m') * 297
        paperwidth = self.toplevel.winfo_fpixels('1m') * 210
        self.canvaspreview.create_rectangle(15, 10, 10+paperwidth, 20+paperheigth, outline='', fill='white')
        #self.canvaspreview.create_text(5, 5, text="self.pageimage", fill="gray", font=('Helvetica  '))
       
                
        filename = "image_{}.jpg".format(self.pageimage)
        filepath = f"./preview/{filename}"        
        
        # Load the original image, and get its size and color mode.
        image=Image.open(filepath)  
        # Resize the image in the given (width, height)
        img=image.resize((self.canvas_draw_width//2+100, self.canvas_draw_height//2+100))

        # Conver the image in TkImage
        my_img=ImageTk.PhotoImage(img)   
        self.canvaspreview.create_image(45,45,anchor=NW,image=my_img)
        self.canvaspreview.create_text(15, 15, text=self.pageimage, fill="gray", font=('Helvetica 10 '))
        print("pageimage",self.pageimage)
        self.toplevel.mainloop()

    def back(self):
        self.canvaspreview.delete("all")
        self.pageimage = self.pageimage -1
        self.canvaspreview.delete("all")
        if self.pageimage <=1:
            self.buttonback['state'] = tk.DISABLED
            self.buttonnext['state'] = tk.NORMAL
        if self.pageimage >= 2 < self.pageImagee:
            self.buttonnext['state'] = tk.NORMAL
            self.buttonback['state'] = tk.NORMAL
         #canvas
        self.canvaspreview = tk.Canvas(self.labelpreview)
        self.canvaspreview.place(relwidth=1, relheight=1)
        paperheigth = self.toplevel.winfo_fpixels('1m') * 297
        paperwidth = self.toplevel.winfo_fpixels('1m') * 210
        self.canvaspreview.create_rectangle(15, 10, 10+paperwidth, 20+paperheigth, outline='', fill='white')
        #self.canvaspreview.create_text(5, 5, text="self.pageimage", fill="gray", font=('Helvetica  '))
                
        filename = "image_{}.jpg".format(self.pageimage)
        filepath = f"./preview/{filename}"        
        
        # Load the original image, and get its size and color mode.
        image=Image.open(filepath)  
        # Resize the image in the given (width, height)
        img=image.resize((self.canvas_draw_width//2+100, self.canvas_draw_height//2+100))

        # Conver the image in TkImage
        my_img=ImageTk.PhotoImage(img)   
        self.canvaspreview.create_image(45,45,anchor=NW,image=my_img)
        self.canvaspreview.create_text(10, 10, text=self.pageimage, fill="gray", font=('Helvetica 10 '))
        print("pageimage",self.pageimage)
        self.toplevel.mainloop()

    def next1(self):
        
        self.pageimage = self.pageimage +1
        self.canvaspreview.delete("all")
        if self.pageimage == self.pageImagee:
            self.buttonnext['state'] = tk.DISABLED
            self.buttonback['state'] = tk.NORMAL
        if self.pageimage >= 2 < self.pageImagee:
            
            self.buttonback['state'] = tk.NORMAL
           #canvas
        self.canvaspreview = tk.Canvas(self.labelpreview1)
        self.canvaspreview.place(relwidth=1, relheight=1)
        paperheigth = self.toplevel2.winfo_fpixels('1m') * 297
        paperwidth = self.toplevel2.winfo_fpixels('1m') * 210
        self.canvaspreview.create_rectangle(15, 10, 10+paperwidth, 20+paperheigth, outline='', fill='white')
        #self.canvaspreview.create_text(5, 5, text="self.pageimage", fill="gray", font=('Helvetica  '))
                
        filename = "image_{}.jpg".format(self.pageimage)
        filepath = f"./preview1/{filename}"        
        
        # Load the original image, and get its size and color mode.
        image=Image.open(filepath)  
        # Resize the image in the given (width, height)
        img=image.resize((self.canvas_draw_width//2+100, self.canvas_draw_height//2+100))

        # Conver the image in TkImage
        my_img=ImageTk.PhotoImage(img)   
        self.canvaspreview.create_image(45,45,anchor=NW,image=my_img)
        self.canvaspreview.create_text(10, 10, text=self.pageimage, fill="gray", font=('Helvetica 10 ')) 
        print(filename)
        self.toplevel2.mainloop()

    def back1(self):
        self.canvaspreview.delete("all")
        self.pageimage = self.pageimage -1
        self.canvaspreview.delete("all")
        if self.pageimage <=1:
            self.buttonback['state'] = tk.DISABLED
            self.buttonnext['state'] = tk.NORMAL
        if self.pageimage >= 2 < self.pageImagee:
            self.buttonnext['state'] = tk.NORMAL
            self.buttonback['state'] = tk.NORMAL
           #canvas
        self.canvaspreview = tk.Canvas(self.labelpreview1)
        self.canvaspreview.place(relwidth=1, relheight=1)
        paperheigth = self.toplevel2.winfo_fpixels('1m') * 297
        paperwidth = self.toplevel2.winfo_fpixels('1m') * 210
        self.canvaspreview.create_rectangle(15, 10, 10+paperwidth, 20+paperheigth, outline='', fill='white')
        #self.canvaspreview.create_text(5, 5, text="self.pageimage", fill="gray", font=('Helvetica  '))        
        filename = "image_{}.jpg".format(self.pageimage)
        filepath = f"./preview1/{filename}"        
        
        # Load the original image, and get its size and color mode.
        image=Image.open(filepath)  
        # Resize the image in the given (width, height)
        img=image.resize((self.canvas_draw_width//2+100, self.canvas_draw_height//2+100))

        # Conver the image in TkImage
        my_img=ImageTk.PhotoImage(img)   
        self.canvaspreview.create_image(45,45,anchor=NW,image=my_img)
        self.canvaspreview.create_text(10, 10, text=self.pageimage, fill="gray", font=('Helvetica 10 '))
        print(filename)
        self.toplevel2.mainloop()  

    def exportpdf(self):
        self.toplevel.destroy()
        
        path = "./preview/" # get the path of images

        imagelist = listdir(path) # get list of all images

        pdf = FPDF('P','mm','A4') # create an A4-size pdf document 

        x,y,w,h = 10,15,self.canvas_draw_width//4,self.canvas_draw_height//4

        for image in imagelist:

            pdf.add_page()
            pdf.image(path+image,x,y,w,h)
      
        #pdf.output("outputPortrait.pdf","F")
        pdf.output(filedialog.asksaveasfilename(filetypes=[("PDF file", ".pdf")])+".pdf", "F")

    def exportpdflanscape(self):
        self.toplevel.destroy()
        path = "./preview1/" # get the path of images

        imagelist = listdir(path) # get list of all images

        pdf = FPDF('L','mm','A4') # create an A4-size pdf document 

        x,y,w,h = 10,15,self.canvas_draw_width//4,self.canvas_draw_height//4

        for image in imagelist:

            pdf.add_page()
            pdf.image(path+image,x,y,w,h)

        #pdf.output("outputLanscape.pdf","F")
        pdf.output(filedialog.asksaveasfilename(filetypes=[("PDF file", ".pdf")]), "F")


    # def installed_printer():
    #     printers = win32print.EnumPrinters(2)
    #     for p in printers:
    #         return(p)

    # printerdef = ''

    # def locprinter(self):
    #     pt = Toplevel()
    # ##    pt.geometry("250x250")
    #     pt.title("choose printer")
    #     var1 = StringVar()
    #     LABEL = Label(pt, text="Select Printer",bg='goldenrod2',fg='black').pack(fill=X)
    #     PRCOMBO = ttk.Combobox(pt, width=35)
    #     print_list = []
    #     printers = list(win32print.EnumPrinters(2))
    #     for i in printers:
    #         print_list.append(i[2])
    #     print(print_list)
    #     # Put printers in combobox
    #     PRCOMBO['values'] = print_list
    #     defprinter= win32print.GetDefaultPrinter()
    #     print('Default selected Printer:',defprinter)
    #     PRCOMBO.set(defprinter)
    #     PRCOMBO.pack(padx=5,pady=5)
            
    #     def select():
    #         global printerdef
    #         printerdef = PRCOMBO.get()
    #         printcommand()
    #         pt.destroy()
    #     BUTTON = ttk.Button(pt, text="Print",width=30,command=select).pack(pady=10)

    #     LAB = Canvas(self.GdataPointObj,self.canvas_draw_height,self.canvas_draw_width)
    #     LAB.pack()

   

    #     def printcommand():
    #         printPic = LAB.pack_configure()
    #         print(printPic)
    #         print(printerdef)
        
    #         win32print.SetDefaultPrinter(printerdef)
    #         filename = tempfile.mktemp(".txt")
    #         open(filename,"w").write(str(printPic))
    #         # Bellow is call to print text from T2 textbox
    #         win32api.ShellExecute(
    #             0,
    #             "printto",
    #             filename,
    #             '"%s"' % win32print.GetDefaultPrinter(),
    #             ".",
    #             0
    #         )
    #         showinfo(title='Success',message='Print Successful',detail='Printing is done . thank You!')

    



    def zoomin(self):
         
        self.scale = self.scale*2 
        self.canvas_draw_width = self.canvas_draw_width*2
        self.canvas_draw_height = self.canvas_draw_height * 2
        # self.newsheet()
        self.canvasMain.delete("all")
        self.canvasMain.config(scrollregion=(0,0,self.canvas_draw_width//2*self.scale,self.canvas_draw_height//2*self.scale))
        self.drawgrid()
        self.paintwithDataPoint()
        
        print(self.scale)
        print(self.canvas_draw_width, self.canvas_draw_height)
        
       
        
    def zoomout(self):   
        self.scale = self.scale//2 
        self.canvas_draw_width = self.canvas_draw_width// 2
        self.canvas_draw_height = self.canvas_draw_height//2
        # self.newsheet()
        self.canvasMain.delete("all")
        self.canvasMain.config(scrollregion=(0,0,self.canvas_draw_width//2*self.scale,self.canvas_draw_height//2*self.scale))
        self.drawgrid()
        self.paintwithDataPoint() 
        


        print(self.scale) 
       
        print(self.GdataPointObj.datapoint)
        

        
    def run(self):
        self.mainwindow.mainloop()
    

if __name__ == '__main__':
    app = GuiTestApp()
      
    app.run()
