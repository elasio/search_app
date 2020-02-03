from tkinter import *
from tkinter import filedialog
from PIL import  Image,ImageTk
import sa
import os
import torch
class GUI():
    def __init__(self):
        self.root = Tk()
        w,h = 620, 620
        self.root.minsize(width=w, height=h)
        self.root.maxsize(width=w, height=h)
        
        self.query_path = None
        self.data_path = os.path.join(sa.ROOT_DIR, 'data', 'test', 'oxford5k')
        self.file = Button(self.root, text='Choose Query', padx =10, pady =10, command = self.choose)
        self.file.grid(row = 1, column = 2)
        
        self.search = Button(self.root, text='Search', padx =10, pady =10, command = self.search_image)
        self.image = None
        self.query_image = Label(self.root)
#        self.query_image.configure(image = self.image )
        
        self.res_1 = Label(self.root, padx = 10, pady = 10)
        self.res_2 = Label(self.root, padx = 10, pady = 10)
        self.res_3 = Label(self.root, padx = 10, pady = 10)
        self.res_4 = Label(self.root, padx = 10, pady = 10)
        self.res_5 = Label(self.root, padx = 10, pady = 10)
        self.res_6 = Label(self.root, padx = 10, pady = 10)
        self.res_7 = Label(self.root, padx = 10, pady = 10)
        self.res_8 = Label(self.root, padx = 10, pady = 10)
        self.res_9 = Label(self.root, padx = 10, pady = 10)
        self.res_0 = Label(self.root, padx = 10, pady = 10)
        
        self.MAP = Label (self.root, padx = 10, pady = 10)
        
        self.list = [self.res_1,
                     self.res_2,
                     self.res_3,
                     self.res_4,
                     self.res_5,
                     self.res_6,
                     self.res_7,
                     self.res_8,
                     self.res_9,
                     self.res_0]
        
#        self.image = PhotoImage(file='C:\\Users\\NGUYỄNMINHTUẤN\\Desktop\\download (16).png')
#        self.label = Label(image=self.image)
        
        self.query_image.grid(row = 2, column = 2)
        
#        for img in self.list
        self.res_1.grid(row = 4, column = 0)
        self.res_2.grid(row = 4, column = 1)
        self.res_3.grid(row = 4, column = 2)
        self.res_4.grid(row = 4, column = 3)
        self.res_5.grid(row = 4, column = 4)
        self.res_6.grid(row = 5, column = 0)
        self.res_7.grid(row = 5, column = 1)
        self.res_8.grid(row = 5, column = 2)
        self.res_9.grid(row = 5, column = 3)
        self.res_0.grid(row = 5, column = 4)
        
        
        self.root.mainloop()
#        
    def choose(self):
        ifile = filedialog.askopenfile(parent=self.root,mode='rb',title='Choose a file')
        self.query_path = ifile.name
        path = Image.open(ifile)
        path = path.resize ((120, 120),Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(path)
        self.query_image.configure(image=self.image)
        self.query_image.image=self.image
        self.search.grid(row = 3, column = 2 )
        
    def search_image(self):
        print(self.query_path)
        ranks, list_image = sa.query(self.query_path)
        for index, image in enumerate(self.list):
#            path = os.path.join(self.data_path, list_image[index])
            path = 'D:\\New folder\\' + list_image[index]
            img = Image.open(path)
            img_resize = img.resize((120, 120),Image.ANTIALIAS)
            temp = ImageTk.PhotoImage(img_resize)
            image.configure(image = temp)
            image.image = temp
        self.MAP.grid(row = 6, column = 0)
        self.MAP.config(text='MAP: ')

#root = Tk()
app = GUI()
#app.mainloop()
#root.destroy()