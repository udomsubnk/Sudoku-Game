from tkinter import *

class Main:
      def __init__(self,master):
            frame = Frame(master)
            frame = Frame(master,background="white")
            frame.pack()
            master.title('SUDOKU')
            
            #DISPLAY
            self.entry=[]
            for i in range(9):
                  for j in range(9):
                        bigfont = ('TH Sarabun New',25)
                        display=Entry(frame,
                                   font=bigfont,width=3,
                                   fg="black",bg='white',
                                   bd=2,justify=CENTER)
                        display.grid(row=i, column=j,sticky="NWNESWSE")

                        self.entry.append(display) 
            
            Button(frame, text='CHECK!',
                             command='quit',width=10).grid(row=10,column=1,columnspan=3)

            Button(frame, text='CLEAR!',
                         command='quit',width=10).grid(row=10,column=3,columnspan=3)

            Button(frame, text='START!',
                         command='quit',width=10).grid(row=10,column=5,columnspan=3)
            
            
            
class Block:
      block_number=0 #block name 
      x=0 #position axis x
      y=0 #position axis y
      value=0 #input value
      group=0 #group each 3x3

      def __init__(self,block_number,x,y,group): #constructor init attribute
            self.block_number=block_number
            self.x=x
            self.y=y
            self.group=group

      def getX(self):
            return self.x
      
      def getY(self):
            return self.y

      def getName(self):
            return self.name

      def getGroup(self):
            return self.group
      
      def setValue(self,value):
            self.value=value

      def getValue(self):
            return self.value
      
                        
      
            

if __name__=='__main__':
      root=Tk()
      Main(root)
      root.mainloop()
      
      
                  
                  
