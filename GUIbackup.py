
from Tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from Tkinter.ttk import Frame, Label, Entry
from Tkinter import Tk, RIGHT, BOTH, RAISED
from Tkinter.ttk import Button, Style
from Tkinter import messagebox
#import Tkinter
 
       #  1    2    3    4    5    6    7    8    9    10   11   12   13   
lZmaj = [ 3.2, 3.2, 3.7, 3.9, 4.2, 4.9, 4.9, 5.0, 5.2, 5.3, 6.0, 6.1, 6.1, 
#14   15   16   17   18   19   20   21   22   23   24   25   26   27   28
6.1, 6.3, 6.4, 6.5, 6.6, 6.6, 6.7, 6.7, 6.7, 6.8, 6.8, 6.8, 6.8, 6.8, 6.9, 
   #  29   30   31   32   33   34   35   36   37   38   39   40
     6.9, 6.9, 6.9, 6.9, 6.9, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0 ]

	#    1    2    3    4    5    6    7    8    9   10   11   12
lPersej = [ 2.9, 2.9, 3.1, 3.9, 3.9, 5.0, 5.1, 5.4, 5.4, 5.6, 5.7, 5.8, 
        #   13   14   15   16   17   18   19   20   21   22   23   24   25 
           6.0, 6.1, 6.2, 6.2, 6.3, 6.3, 6.3, 6.4, 6.4, 6.4, 6.6, 6.6, 6.6,
        #   26	 27   28   29   30   31
           6.7, 6.8, 6.8, 6.9, 6.9, 7.0 ]

	#      1    2    3    4    5    6    7    8    9   10   11   12
lVMedved = [ 2.4, 3.3, 3.7, 3.9, 4.5, 4.6, 4.8, 5.2, 5.4, 5.4, 5.7, 5.7,
        #     13   14   15   16   17   18   19   20   21   22   23   24
             5.8, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.6, 6.6, 6.7, 6.7,
	#     25   26   27   28   29
             6.8, 6.8, 6.9, 6.9, 7.0 ] 
	
	
	#	1    2    3    4    5    6    7	   8    9   10   11
lBlizanci = [ 1.2, 2.4, 3.2, 3.9, 4.3, 5.0, 5.1, 5.3, 5.6, 5.7, 5.9,
        #     12   13   14   15   16   17   18   19   20   21   22
             6.1, 6.2, 6.3, 6.4, 6.5, 6.5, 6.6, 6.6, 6.7, 6.7, 6.9,
	#     23
             7.0 ]

	#   1    2    3    4    5    6    7    8    9   10   11   12   13
lOrao = [ 2.8, 3.0, 3.4, 4.6, 5.1, 5.2, 5.4, 6.0, 6.0, 6.2, 6.4, 6.5, 6.6,
	#  14   15   16   17   18   19   20   21   22
          6.6, 6.6, 6.6, 6.6, 6.6, 6.9, 6.9, 6.9, 7.0 ] 

	#   1    2    3    4    5    6    7    8    9   10   11   12   13
lPegaz = [2.1, 2.6, 2.9, 4.7, 5.2, 5.4, 5.7, 5.8, 6.2, 6.2, 6.2, 6.3, 6.3,
        #  14   15   16   17   18   19   20   21   22   23   24   25  26
          6.4, 6.4, 6.4, 6.5, 6.5, 6.5, 6.6, 6.6, 6.6, 6.6, 6.6, 6.7,6.7,
	#  27   28   29   30   31   32   33
          6.7, 6.7, 6.8, 6.9, 6.9, 6.9, 7.0 ]

	#    1    2    3    4    5    6    7    8    9   10   10   12
lCefej = [ 2.6, 3.3, 4.0, 4.5, 4.6, 4.6, 4.9, 5.2, 5.2, 5.4, 5.4, 5.5,
	#   13   14   15   16   17   18   19   20   21   22   23   24
           5.9, 6.0, 6.1, 6.1, 6.2, 6.3, 6.3, 6.4, 6.4, 6.5, 6.8, 6.8,
	#   25   26   27   28   29   30   31   32   33
           6.8, 6.9, 6.9, 6.9, 6.9, 6.9, 6.9, 6.9, 7.0 ] 
	
	#  1    2    3    4    5    6	 7    8    9   10   11   12   13
lBik = [ 1.1, 1.8, 3.0, 4.7, 4.8, 4.8, 5.1, 5.3, 5.5, 5.9, 6.0, 6.1, 6.1,
        # 14   15   16	 17   18   19   20   21   22   23   24   25   26
         6.1, 6.2, 6.3, 6.4, 6.4, 6.4, 6.5, 6.6, 6.6, 6.7, 6.7, 6.7, 6.8,
        # 27   28   29
         6.8, 6.9, 7.0 ]

	#  1    2    3    4    5    6    7    8    9   10   11   12
lLav = [ 1.3, 2.2, 2.2, 2.6, 3.4, 3.8, 4.4, 5.0, 5.0, 5.0, 5.6, 5.6,
	# 13   14   15   16   17   18   19   20   21   22   23   24
         5.7, 5.7, 6.0, 6.0, 6.0, 6.1, 6.1, 6.3, 6.4, 6.4, 6.4, 6.6,
	# 25   26   27   28   29   30   31   32
         6.7, 6.7, 6.7, 6.7, 6.9, 6.9, 6.9, 7.0 ] 

	#     1    2    3    4    5    6    7    8    9   10   11   12
lDevica = [ 1.2, 2.9, 3.4, 4.5, 5.8, 5.8, 5.9, 6.0, 6.0, 6.0, 6.1, 6.4,
	#    13   14   15   16   17   18   19
            6.4, 6.4, 6.5, 6.7, 6.8, 6.8, 7.0 ] 

	#     1    2    3    4    5    6    7    8    9   10   11   12
lVolar  = [ 0.2, 2.3, 2.7, 3.0, 3.8, 4.5, 4.7, 4.7, 4.9, 5.0, 5.3, 5.3, 
	#    13   14   15   16   17   18   19   20   21   22   23   24
            5.7, 5.8, 5.8, 5.8, 5.9, 5.9, 6.0, 6.0, 6.1, 6.1, 6.2, 6.2,
	#    25   26   27   28   29   30   31   32   33   34   35   36
            6.3, 6.3, 6.4, 6.4, 6.4, 6.5, 6.5, 6.6, 6.6, 6.6, 6.6, 6.7,
	#    37   38   39   40   41   42   43   44   45   46   47   48
            6.7, 6.7, 6.8, 6.8, 6.8, 6.8, 6.8, 6.8, 6.9, 6.9, 6.9, 6.9,
	#    49   50   51   52
            6.9, 6.9, 6.9, 7.0 ]

	#        1    2    3    4    5    6    7    8    9   10   11
lZmijonosa = [ 2.7, 2.7, 3.0, 3.6, 3.7, 5.2, 5.3, 5.3, 5.4, 5.4, 5.6,
	#       12   13   14   15   16   17   18   19   20   21   22
               5.6, 5.8, 6.4, 6.4, 6.4, 6.5, 6.5, 6.7, 6.8, 6.8, 6.9,
	#       23
               7.0 ]

	#         1    2    3    4    5    6    7    8    9   10   11
lHerkulLira = [ 2.3, 3.9, 4.2, 4.3, 4.5, 5.0, 5.5, 5.7, 5.7, 5.7, 5.7, 
	#        12   13   14   15   16   17   18   19   20   21   22
                5.9, 6.0, 6.0, 6.1, 6.2, 6.3, 6.5, 6.5, 6.8, 6.8, 6.8,
	#        23   24   25   26   27
                6.9, 6.9, 6.9, 6.9, 7.0 ]
 
	#    1    2    3    4    5    6    7    8    9   10   11   12 
lLabud = [ 2.3, 2.6, 4.0, 4.8, 4.8, 4.9, 5.0, 5.2, 5.2, 5.2, 5.5, 5.7,
        #   13   14   15   16   17   18   19   20   21   22   23   24
           5.9, 6.0, 6.1, 6.2, 6.2, 6.3, 6.3, 6.4, 6.4, 6.4, 6.4, 6.5,
	#   25   26   27   28   29   30   31   32   33   34   35   36
           6.5, 6.5, 6.5, 6.6, 6.6, 6.6, 6.6, 6.7, 6.7, 6.8, 6.8, 6.9,
	#   37   38   39   40   41
           6.9, 6.9, 6.9, 6.9, 7.0 ]      

	#         1    2    3    4    5    6    7    8    9   10   11
lZmajHerkul = [ 3.0, 3.4, 3.9, 4.9, 5.1, 5.5, 5.9, 5.9, 5.9, 6.0, 6.0, 
	#        12   13   14   15   16   17   18   19   20   21   22
                6.1, 6.1, 6.1, 6.1, 6.1, 6.1, 6.3, 6.3, 6.3, 6.4, 6.6,
	#        23   24   25   26   27   28   29   30   31   32   33
                6.6, 6.6, 6.6, 6.7, 6.7, 6.7, 6.7, 6.7, 6.7, 6.9, 7.0 ] 
               
	#         1    2    3    4    5    6    7    8    9   10   11
lLovackiPsi = [ 1.7, 1.9, 2.9, 4.6, 5.1, 5.7, 5.7, 5.9, 6.0, 6.0, 6.2, 
	#        12   13   14   15   16   17   18   19   20   21   22 
                6.2, 6.2, 6.4, 6.4, 6.4, 6.6, 6.6, 6.8, 6.8, 6.8, 6.9, 		#	 23   24	 	
                6.9, 7.0 ]                  
        #      1    2    3    4    5    6    7    8    9   10   11   12
lKocijas = [ 0.2, 2.1, 2.7, 3.5, 3.9, 4.2, 4.2, 4.6, 5.1, 5.5, 5.9, 6.0,
        #     13   14   15   16   17   18   19   20   21   22   23   24
             6.0, 6.1, 6.1, 6.2, 6.3, 6.3, 6.3, 6.4, 6.4, 6.4, 6.4, 6.4,
        #     25   26   27   28   29   30   31   32   33   34   35   36 
             6.4, 6.5, 6.5, 6.5, 6.5, 6.6, 6.6, 6.6, 6.6, 6.6, 6.7, 6.7,
        #     37   38   39   40   41   42   43   44
             6.7, 6.8, 6.8, 6.8, 6.9, 6.9, 6.9, 7.0 ] 
        #        1    2    3    4    5    6    7    8    9   10   11
lAndromeda = [ 2.3, 3.9, 4.2, 4.3, 4.3, 5.0, 5.1, 5.1, 5.2, 5.5, 5.7, 
        #       12   13   14   15   16   17   18   19   20   21   22
               5.9, 6.1, 6.3, 6.3, 6.3, 6.4, 6.5, 6.5, 6.5, 6.5, 6.5, 
        #       23   24   25   26   27   28   29   30   31   32   33
               6.5, 6.6, 6.6, 6.6, 6.7, 6.7, 6.7, 6.7, 6.9, 6.9, 7.0 ]

        #         1    2    3    4    5    6    7    8    9   10   11
lMaliMedved = [ 2.2, 3.6, 3.9, 5.2, 5.4, 5.7, 5.7, 6.1, 6.1, 6.1, 6.4,
        #        12   13   14   15   16
                6.6, 6.6, 6.7, 6.8, 7.0 ]

poligoni = [ lZmaj, lPersej, lVMedved, lBlizanci, lOrao, lPegaz, lCefej, lBik, lLav, lDevica, lVolar, lZmijonosa, lHerkulLira, lLabud, lZmajHerkul, lLovackiPsi, lKocijas, lAndromeda, lMaliMedved ]    



entries = []

class Row:
	def __init__(self, parent, text):
		self.frame = Frame(parent)
		self.frame.pack(fill=X)
		
		self.lbl = Label(self.frame, text=text, width=25)
		self.lbl.pack(side=LEFT, padx=10, pady=5)           
	       
		self.entry = Entry(self.frame)
		self.entry.pack(fill=X, padx=10, expand=True)

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()

        
    def initUI(self):
      
        self.master.title("Poligon Poligon")
        self.pack(fill=BOTH, expand=True)
	
        frames = []
        frame1 = Frame(self)
        
	####################
        frame1 = Frame(self)
        frame1.pack(fill=X)
        
        lbl1 = Label(frame1, text="Zmaj (Draco)", width=25)
        lbl1.pack(side=LEFT, padx=10, pady=5)           
       
        global entry1
        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=10, expand=True)
        entries.append(entry1)
	####################
        
        frame2 = Frame(self)
        frame2.pack(fill=X)
        
        lbl2 = Label(frame2, text="Persej (Perseus)", width=25)
        lbl2.pack(side=LEFT, padx=10, pady=5)        
	
        global entry2
        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=10, expand=True)
        entries.append(entry2)
	####################
        
        frame3 = Frame(self)
        frame3.pack(fill=X)
        
        lbl3 = Label(frame3, text="Veliki Medved (Ursa Major)", width=25)
        lbl3.pack(side=LEFT, padx=10, pady=5)        

        global entry3
        entry3 = Entry(frame3)
        entry3.pack(fill=X, padx=10, expand=True)
        entries.append(entry3)
	#####################
	
        frame4 = Frame(self)
        frame4.pack(fill=X)
        
        lbl4 = Label(frame4, text="Blizanci (Gemini)", width=25)
        lbl4.pack(side=LEFT, padx=10, pady=5)        

        global entry4
        entry4 = Entry(frame4)
        entry4.pack(fill=X, padx=10, expand=True)
        entries.append(entry4)
	#####################
	
        frame5 = Frame(self)
        frame5.pack(fill=X)
        
        lbl5 = Label(frame5, text="Orao (Aquila)", width=25)
        lbl5.pack(side=LEFT, padx=10, pady=5)        

        global entry5
        entry5 = Entry(frame5)
        entry5.pack(fill=X, padx=10, expand=True)
        entries.append(entry5)
	#####################
	
        frame6 = Frame(self)
        frame6.pack(fill=X)
        
        lbl6 = Label(frame6, text="Pegaz (Pegasus)", width=25)
        lbl6.pack(side=LEFT, padx=10, pady=5)        
        
        global entry6
        entry6 = Entry(frame6)
        entry6.pack(fill=X, padx=10, expand=True)
        entries.append(entry6)
	#####################
	
        frame7 = Frame(self)
        frame7.pack(fill=X)
        
        lbl7 = Label(frame7, text="Cefaj (Cepheus)", width=25)
        lbl7.pack(side=LEFT, padx=10, pady=5)        

        global entry7
        entry7 = Entry(frame7)
        entry7.pack(fill=X, padx=10, expand=True)
        entries.append(entry7)

	####################
	
        frame8 = Frame(self)
        frame8.pack(fill=X)
        
        lbl8 = Label(frame8, text="Bik (Taurus)", width=25)
        lbl8.pack(side=LEFT, padx=10, pady=5)        

        global entry8
        entry8 = Entry(frame8)
        entry8.pack(fill=X, padx=10, expand=True)
        entries.append(entry8)
	####################
	
        frame9 = Frame(self)
        frame9.pack(fill=X)
        
        lbl9 = Label(frame9, text="Lav (Leo)", width=25)
        lbl9.pack(side=LEFT, padx=10, pady=5)        

        global entry9
        entry9 = Entry(frame9)
        entry9.pack(fill=X, padx=10, expand=True)
        entries.append(entry9)
	####################
	
        frame10 = Frame(self)
        frame10.pack(fill=X)
        
        lbl10 = Label(frame10, text="Devica (Virgo)", width=25)
        lbl10.pack(side=LEFT, padx=10, pady=5)        

        global entry10
        entry10 = Entry(frame10)
        entry10.pack(fill=X, padx=10, expand=True)
        entries.append(entry10)

	####################
	
        frame11 = Frame(self)
        frame11.pack(fill=X)
        
        lbl11 = Label(frame11, text="Volar (Botes)", width=25)
        lbl11.pack(side=LEFT, padx=10, pady=5)        

        global entry11
        entry11 = Entry(frame11)
        entry11.pack(fill=X, padx=10, expand=True)
        entries.append(entry11)
	####################
	
        frame12 = Frame(self)
        frame12.pack(fill=X)
        
        lbl12 = Label(frame12, text="Vaga (Libra)", width=25)
        lbl12.pack(side=LEFT, padx=10, pady=5)        

        global entry12
        entry12 = Entry(frame12)
        entry12.pack(fill=X, padx=10, expand=True)
        entries.append(entry12)

	####################
	
        frame13 = Frame(self)
        frame13.pack(fill=X)
        
        lbl13 = Label(frame13, text="Herkul/Lira (Hercules/Lyra)", width=25)
        lbl13.pack(side=LEFT, padx=10, pady=5)        

        global entry13
        entry13 = Entry(frame13)
        entry13.pack(fill=X, padx=10, expand=True)
        entries.append(entry13)
	
	####################
	
        frame14 = Frame(self)
        frame14.pack(fill=X)
        
        lbl14 = Label(frame14, text="Labud (Cygnus)", width=25)
        lbl14.pack(side=LEFT, padx=10, pady=5)        

        global entry14
        entry14 = Entry(frame14)
        entry14.pack(fill=X, padx=10, expand=True)
        entries.append(entry14)
	####################
	
        frame15 = Frame(self)
        frame15.pack(fill=X)
        
        lbl15 = Label(frame15, text="Herkul/Zmaj (Hercules/Draco)", width=25)
        lbl15.pack(side=LEFT, padx=10, pady=5)        

        global entry15
        entry15 = Entry(frame15)
        entry15.pack(fill=X, padx=10, expand=True)
        entries.append(entry15)	
	####################
	
        frame16 = Frame(self)
        frame16.pack(fill=X)
        
        lbl16 = Label(frame16, text="Veliki Medved (Ursa Major)", width=25)
        lbl16.pack(side=LEFT, padx=10, pady=5)        

        global entry16
        entry16 = Entry(frame16)
        entry16.pack(fill=X, padx=10, expand=True)
        entries.append(entry16)

	####################
	
        frame17 = Frame(self)
        frame17.pack(fill=X)
        
        lbl17 = Label(frame17, text="Kocijas (Auriga)", width=25)
        lbl17.pack(side=LEFT, padx=10, pady=5)        

        global entry17
        entry17 = Entry(frame17)
        entry17.pack(fill=X, padx=10, expand=True)
        entries.append(entry17)
	
	####################
	
        frame18 = Frame(self)
        frame18.pack(fill=X)
        
        lbl18 = Label(frame18, text="Andromeda (Andromeda)", width=25)
        lbl18.pack(side=LEFT, padx=10, pady=5)        

        global entry18
        entry18 = Entry(frame18)
        entry18.pack(fill=X, padx=10, expand=True)
        entries.append(entry18)

	####################
	
        frame19 = Frame(self)
        frame19.pack(fill=X)
        
        lbl19 = Button(frame19,text="Mali Medved (Ursa Minor)", width=25)
        lbl19.pack(side="left", padx=10, pady=7.5)        

        global entry19
        entry19 = Entry(frame19)
        entry19.pack(fill=X, padx=10, expand=True)
        entries.append(entry19)	
	####################
        self.entry1 = entry1

        frame20 = Frame(self)
        frame20.pack(fill=X)
            
        clearButton = Button(frame20, text="Clear", command=clearButtonClick)
        clearButton.pack(side="left", padx=10, pady=7.5, expand=1)
        

        calculateButton = Button(frame20, text="Calculate", command=calculateButtonClick)
        calculateButton.pack(side="right", padx=10, pady=7.5, expand=0.5)
       
        
def findLMG(poligon, index, value):
        help = 0
        while(help < index):
                help = help + 1
        value = poligon[help]
        return value

def sayLMG(value):
        messagebox.showinfo("Porukica", value)

def premaloPoligona():
        messagebox.showinfo("Porukica", "Uneti vise od jednog poligona")

def clearButtonClick():
        number = 0
        for entry in entries:
                entry.delete(0, "end")                
                
def calculateButtonClick():
        popunjeni = []
        number = 0
        br = 0.0
        pomocBr = 0.0
        im = 0.0
        string = "poligon"
        while (number < len(entries)):
                if (len(entries[number].get()) != 0):
                        valueOfEntry =  float(entries[number].get())
                        pomocBr = findLMG(poligoni[number], valueOfEntry, pomocBr)
                        br = br + pomocBr
                        im = im + 1              
                number = number + 1
        
        if (im > 1):
                LMG = br/im
                message = "Vrednost LMG-a je :" + str(round(LMG, 2))
                sayLMG(message)
        else:
                premaloPoligona()
       

def main():
  
    root = Tk()
    root.geometry("300x550+300+70")
    app = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()  
