from tkinter import *
import socket
import re
class Main:
      
      def __init__(self,master):
            frame = Frame(master)
            frame = Frame(master,background='#000000')
            frame.pack()
            master.title('SUDOKU') 
            #DISPLAY
            self.group=[[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],
                   [33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]
            self.entry=[] # Save block data
            block_number=0 #intitail
            self.allBlocks=[]
            self.checkStart = FALSE
            self.countBlankentry=81
            self.keepValueTrue = [FALSE]*81
          
                       
            for i in range(9):
                  for j in range(9):
                        self.allBlocks.append(self.createBlock(i,j,frame,block_number,self.group))
                        block_number+=1 #create block 81 block
            #print(len(self.allBlocks))
            
            Button(frame, text='CreateServer',
                             command=self.startServer,width=10).grid(row=10,column=1,columnspan=3)

            Button(frame, text='JoinServer',
                         command=self.joinServer,width=10).grid(row=10,column=5,columnspan=3)

            Button(frame, text='START!',
                         command=self.start,width=10).grid(row=10,column=3,columnspan=3)
            
            

            self.MyScore =Scale(orient='horizontal', from_=0, to=128,bg='#00FF7F',borderwidth=5,label='MY SCORE ',length=370,width='40')
            self.MyScore.pack()
            self.setMyScore(0)
            
            self.OppenentsScore =Scale(orient='horizontal', from_=0, to=128,bg='#FF6666',borderwidth=5,label='MY SCORE ',length=370,width='40')
            self.OppenentsScore.pack()
            self.setOppenentsScore(0)
            
      def setMyScore(self,n):
            self.MyScore.set(n)
           

      def setOppenentsScore(self,n):
            self.OppenentsScore.set(n)
            
      def createBlock(self,i,j,frame,block_number,group):
            bigfont = ('TH Sarabun New',25)
   
            def callback(sv,block_number):
                  #print (sv.get())
                  #print (block_number)
                  if self.checkStart:                        
                        print (len(sv.get()))
                        if sv.get()=="":
                               self.entry[block_number].configure(bg='white')
                               self.keepValueTrue[block_number]=FALSE
                        elif ((len(sv.get())>1) or not re.search(r'[1-9]',sv.get()[0])): #เอาแต่อาเรย์ช่อง0
                              self.entry[block_number].configure(bg='red')
                              self.keepValueTrue[block_number]=FALSE
                        elif self.check():
                              self.entry[block_number].configure(bg='green')
                              self.keepValueTrue[block_number]=TRUE
                              
                              print('True')
                        else:
                              self.entry[block_number].configure(bg='red')
                              self.keepValueTrue[block_number]=FALSE
                              print('False')
                        print (str(sum(self.keepValueTrue))+":"+str(self.countBlankentry)) #True:AllBlank
                        
 
            sv = StringVar()
            sv.trace("w", lambda name, index, mode, sv=sv: callback(sv,block_number))
            display=Entry(frame,
                                   font=bigfont,width=3,
                                   fg="black",bg='white',
                                   bd=2,justify=CENTER,textvariable=sv)
            display.grid(row=i, column=j,sticky="NWNESWSE")
            self.entry.append(display)
            for index in range(9):
                  if block_number in group[index]:
                       return  Block(block_number,i,j,index)
            
      def check_row(self):
            for i in range(0,81,9):
                  lis=[]
                  for j in range(i,i+9):
                       if self.allBlocks[j].getValue() != 0 :
                              if self.allBlocks[j].getValue() in lis:
                                    return False
                              else:
                                    lis.append(self.allBlocks[j].getValue())
            return True
      
      def check_column(self):
            for i in range(0,9,1):
                  lis=[]
                  for j in range(i,81,9):
                        if self.allBlocks[j].getValue()!=0:
                              if self.allBlocks[j].getValue() in lis:
                                    lis.append(self.allBlocks[j].getValue())
                                    return False
                              else:
                                    lis.append(self.allBlocks[j].getValue())
            return True

      def check_group(self):
            for i in range(9):
                  lis=[]
                  for j in range(9):
                        if self.allBlocks[self.group[i][j]].getValue() !=0:
                              if self.allBlocks[self.group[i][j]].getValue() in lis:
                                    return False
                              else:
                                    lis.append(self.allBlocks[self.group[i][j]].getValue())
            return True
      
            
      def startServer(self):
            serversocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            host=''
            port=9999
            serversocket.bind((host,port))
            #queue up to n request
            serversocket.listen(10)
            print("SERVER START!")
            clientsocket,addr=serversocket.accept()
            print("CLIENT CONNECT ALREADY!")
            clientsocket.send("KAOKAO")

      def joinServer(self):
             s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
             host=''
             port=9999
            #Connect to hostname on the part
             try:
                  s.connect((host,port))
                  print("YOU CONNECTED ALREADY!")
                  score=s.recv(1024)
                  self.setMyscore(5)
             except  socket.error as msg:
                   print (msg)
        
                  
            
      def blinding(self):
            for i in range(81):
                  if self.entry[i].get() != "":
                        self.allBlocks[i].setValue(self.entry[i].get())
                  else:
                        self.allBlocks[i].setValue(0)
                  #print(self.allBlocks[i].getValue())
                  
      def check(self):
            self.blinding()
            return self.check_row() and self.check_column() and self.check_group()             
                        

      def start(self):
            f=open("Text.txt")
            self.file=f.read()
            self.listsplit=[]
            self.file=self.file.replace("\n"," ").split(" ")
            
            for i in range(81):
                  if self.file[i]=="0":
                        self.entry[i].insert(1,"")
                        
                        
                  else:
                        self.entry[i].insert(1,self.file[i])
                        self.entry[i].configure(state='disabled')
                        self.allBlocks[i].setValue(self.file[i])
                        self.countBlankentry-=1
                        #print(self.allBlocks[i].getValue())
            
            print (self.countBlankentry)
            self.checkStart = TRUE
            
                 
              
            
            
class Block:
      block_number=0 #block name 
      value=0 #input value
      group=0 #group each 3x3

      def __init__(self,block_number,x,y,group): #constructor init attribute
            self.block_number=block_number
            self.x=x
            self.y=y
            self.group=group


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
      
      
                  
                  
