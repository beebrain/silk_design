import os
import tkinter as tk
import tkinter.ttk as ttk
class ChildClass(tk.Toplevel):
    def __init__(self, parent):
        # tk.Toplevel.__init__(self, parent)
        self.parent = parent
        # build ui
        self.toplevel1 = tk.Tk()
        self.labelframe4 = tk.LabelFrame(self.toplevel1)
        self.label4 = tk.Label(self.labelframe4)
        self.label4.configure(text='สูง')
        self.label4.grid(column='0', row='0')
        self.label5 = tk.Label(self.labelframe4)
        self.label5.configure(text='กว้าง')
        self.label5.grid(column='0', row='1')
        self.entry3 = tk.Entry(self.labelframe4)
        _text_ = '''50'''
        self.entry3.delete('0', 'end')
        self.entry3.insert('0', _text_)
        self.entry3.grid(column='1', row='0')
        self.entry4 = tk.Entry(self.labelframe4)
        _text_ = '''50'''
        self.entry4.delete('0', 'end')
        self.entry4.insert('0', _text_)
        self.entry4.grid(column='1', row='1')
        self.label6 = tk.Label(self.labelframe4)
        self.label6.configure(text='ช่อง')
        self.label6.grid(column='3', row='0')
        self.label7 = tk.Label(self.labelframe4)
        self.label7.configure(text='ช่อง')
        self.label7.grid(column='3', row='1')
        self.labelframe4.configure(height='100', takefocus=False, text='ระบุขนาด', width='200')
        self.labelframe4.grid(column='0', row='0')
        self.frame4 = tk.Frame(self.toplevel1)
        self.button5 = tk.Button(self.frame4)
        self.button5.configure(cursor='arrow', text='สร้าง')
        self.button5.grid(column='0', row='0')
        self.button6 = tk.Button(self.frame4)
        self.button6.configure(text='ยกเลิก')
        self.button6.grid(column='1', row='0')
        self.frame4.configure(height='200', width='200')
        self.frame4.grid(column='0', row='1')
        self.toplevel1.configure(height='200', width='200')

        self.button5['command'] = self.create_window
        self.button6['command'] = self.dis
        self.scale = 8
        self.counter=0
    
    def create_window(self):
        print("xx")
        # self.destroy()
        w = int(self.entry4.get())
        h = int(self.entry3.get())
        # w,h = 1200-100, 1200-10

        self.parent.canvas_draw_width = w*self.scale
        self.parent.canvas_draw_height = h*self.scale
        # self.parent.canvasMain.config(width=w, height=h)
        self.parent.newsheet()
        self.parent.canvasMain.delete("all")
        self.parent.drawgrid()
        self.dis()

    
    def dis(self):
        self.toplevel1.destroy()


