
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Button, Style
from tkinter import messagebox
from tkinter import Toplevel

from PIL import ImageTk, Image

#lalal
       #  1    2    3    4    5    6    7    8    9    10   11   12   13   
lZmaj = [ 3.2, 3.2, 3.7, 3.9, 4.2, 4.9, 4.9, 5.0, 5.2, 5.3, 6.0, 6.1, 6.1, 
#14   15   16   17   18   19   20   21   22   23   24   25   26   27   28
6.1, 6.3, 6.4, 6.5, 6.6, 6.6, 6.7, 6.7, 6.7, 6.8, 6.8, 6.8, 6.8, 6.8, 6.9, 
   #  29   30   31   32   33   34   35   36   37   38   39   40   41   42
     6.9, 6.9, 6.9, 6.9, 6.9, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.1, 7.1,
   #  43   44   45   46   47   48   49   50   51   52   53   54   55   56
     7.1, 7.1, 7.1, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.3, 7.3,
   #  57   58   59   60   61   62   63   64   65   66   67   68   69   70
     7.3, 7.3, 7.3, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4,
   #  71   72   73
     7.4, 7.4, 7.5 ]

	#    1    2    3    4    5    6    7    8    9   10   11   12
lPersej = [ 2.9, 2.9, 3.1, 3.9, 3.9, 5.0, 5.1, 5.4, 5.4, 5.6, 5.7, 5.8, 
        #   13   14   15   16   17   18   19   20   21   22   23   24   25 
           6.0, 6.1, 6.2, 6.2, 6.3, 6.3, 6.3, 6.4, 6.4, 6.4, 6.6, 6.6, 6.6,
        #   26	 27   28   29   30   31   32   33   34   35   36   37   38
           6.7, 6.8, 6.8, 6.9, 6.9, 7.0, 7.0, 7.0, 7.0, 7.1, 7.1, 7.1, 7.1,
        #   39   40   41   42   43   44   45   46   47   48   49  50  51
           7.1, 7.1, 7.1, 7.2, 7.2, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3,7.3,7.3,
        #   52   53   54   55   56   57   58   59
           7.3, 7.3, 7.4, 7.4, 7.4, 7.4, 7.4, 7.5 ]  

         

	#      1    2    3    4    5    6    7    8    9   10   11   12
lVMedved = [ 2.4, 3.3, 3.7, 3.9, 4.5, 4.6, 4.8, 5.2, 5.4, 5.4, 5.7, 5.7,
        #     13   14   15   16   17   18   19   20   21   22   23   24
             5.8, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.6, 6.6, 6.7, 6.7,
	#     25   26   27   28   29   30   31   32   33   34   35   36
             6.8, 6.8, 6.9, 6.9, 7.0, 7.0, 7.0, 7.0, 7.1, 7.1, 7.1, 7.1,
        #     37   38   39   40   41   42   43   44   45   46   47   48
             7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.3, 7.3, 7.3, 7.3, 7.3,
        #     49   50   51   52   53   54
             7.4, 7.4, 7.4, 7.4, 7.4, 7.5 ] 
	 
	
	#	1    2    3    4    5    6    7	   8    9   10   11
lBlizanci = [ 1.2, 2.4, 3.2, 3.9, 4.3, 5.0, 5.1, 5.3, 5.6, 5.7, 5.9,
        #     12   13   14   15   16   17   18   19   20   21   22
             6.1, 6.2, 6.3, 6.4, 6.5, 6.5, 6.6, 6.6, 6.7, 6.7, 6.9,
	#     23   24   25   26   27   28   29   30
             7.0, 7.0, 7.2, 7.3, 7.3, 7.3, 7.3, 7.5 ]

	#   1    2    3    4    5    6    7    8    9   10   11   12   13
lOrao = [ 2.8, 3.0, 3.4, 4.6, 5.1, 5.2, 5.4, 6.0, 6.0, 6.2, 6.4, 6.5, 6.6,
	#  14   15   16   17   18   19   20   21   22   23   24   25   26
          6.6, 6.6, 6.6, 6.6, 6.6, 6.9, 6.9, 6.9, 7.0, 7.0, 7.1, 7.2, 7.3,
        #  27 
          7.4 ] 

	#   1    2    3    4    5    6    7    8    9   10   11   12   13
lPegaz = [2.1, 2.6, 2.9, 4.7, 5.2, 5.4, 5.7, 5.8, 6.2, 6.2, 6.2, 6.3, 6.3,
        #  14   15   16   17   18   19   20   21   22   23   24   25  26
          6.4, 6.4, 6.4, 6.5, 6.5, 6.5, 6.6, 6.6, 6.6, 6.6, 6.6, 6.7,6.7,
	#  27   28   29   30   31   32   33   34   35   36   37   38  39
          6.7, 6.7, 6.8, 6.9, 6.9, 6.9, 7.0, 7.0, 7.1, 7.1, 7.1, 7.1, 7.1,
        #  40   41   42   43   44   45   46   47   48   49
          7.2, 7.2, 7.2, 7.3, 7.3, 7.3, 7.4, 7.4, 7.4, 7.5 ]

	#    1    2    3    4    5    6    7    8    9   10   10   12
lCefej = [ 2.6, 3.3, 4.0, 4.5, 4.6, 4.6, 4.9, 5.2, 5.2, 5.4, 5.4, 5.5,
	#   13   14   15   16   17   18   19   20   21   22   23   24
           5.9, 6.0, 6.1, 6.1, 6.2, 6.3, 6.3, 6.4, 6.4, 6.5, 6.8, 6.8,
	#   25   26   27   28   29   30   31   32   33   34   35   36
           6.8, 6.9, 6.9, 6.9, 6.9, 6.9, 6.9, 6.9, 7.0, 7.0, 7.0, 7.0,
        #   37   38   39   40   41   42   43   44   45   46   47   48
           7.0, 7.0, 7.0, 7.0, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.2,
        #   49   50   51   52   53   54   55   56   57   58   59   60
           7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.4, 7.4, 7.4, 7.4,
        #   61   62   63   64   65
           7.4, 7.4, 7.4, 7.4, 7.5  ] 
	
	#  1    2    3    4    5    6	 7    8    9   10   11   12   13
lBik = [ 1.1, 1.8, 3.0, 4.7, 4.8, 4.8, 5.1, 5.3, 5.5, 5.9, 6.0, 6.1, 6.1,
        # 14   15   16	 17   18   19   20   21   22   23   24   25   26
         6.1, 6.2, 6.3, 6.4, 6.4, 6.4, 6.5, 6.6, 6.6, 6.7, 6.7, 6.7, 6.8,
        # 27   28   29   30   31   32
         6.8, 6.9, 7.0, 7.0, 7.4, 7.5 ]

	#  1    2    3    4    5    6    7    8    9   10   11   12
lLav = [ 1.3, 2.2, 2.2, 2.6, 3.4, 3.8, 4.4, 5.0, 5.0, 5.0, 5.6, 5.6,
	# 13   14   15   16   17   18   19   20   21   22   23   24
         5.7, 5.7, 6.0, 6.0, 6.0, 6.1, 6.1, 6.3, 6.4, 6.4, 6.4, 6.6,
	# 25   26   27   28   29   30   31   32   33   34   35   36
         6.7, 6.7, 6.7, 6.7, 6.9, 6.9, 6.9, 7.0, 7.0, 7.1, 7.1, 7.1,
        # 37   38   39   40   41   42   43   44   45
         7.1, 7.2, 7.2, 7.3, 7.3, 7.3, 7.3, 7.4, 7.5 ] 

	#     1    2    3    4    5    6    7    8    9   10   11   12
lDevica = [ 1.2, 2.9, 3.4, 4.5, 5.8, 5.8, 5.9, 6.0, 6.0, 6.0, 6.1, 6.4,
	#    13   14   15   16   17   18   19   20   21   22   23   24
            6.4, 6.4, 6.5, 6.7, 6.8, 6.8, 7.0, 7.0, 7.0, 7.1, 7.2, 7.2, 
        #    25   26   27   28   29   30   31
            7.3, 7.4, 7.4, 7.4, 7.4, 7.4, 7.5 ]     

	#     1    2    3    4    5    6    7    8    9   10   11   12
lVolar  = [ 0.2, 2.3, 2.7, 3.0, 3.8, 4.5, 4.7, 4.7, 4.9, 5.0, 5.3, 5.3, 
	#    13   14   15   16   17   18   19   20   21   22   23   24
            5.7, 5.8, 5.8, 5.8, 5.9, 5.9, 6.0, 6.0, 6.1, 6.1, 6.2, 6.2,
	#    25   26   27   28   29   30   31   32   33   34   35   36
            6.3, 6.3, 6.4, 6.4, 6.4, 6.5, 6.5, 6.6, 6.6, 6.6, 6.6, 6.7,
	#    37   38   39   40   41   42   43   44   45   46   47   48
            6.7, 6.7, 6.8, 6.8, 6.8, 6.8, 6.8, 6.8, 6.9, 6.9, 6.9, 6.9,
	#    49   50   51   52   53   54   55   56   57   58   59   60
            6.9, 6.9, 6.9, 7.0, 7.0, 7.0, 7.1, 7.1, 7.1, 7.1, 7.1, 7.2,
        #    61   62   63   64   65   66   67   68   69   70   71   72
            7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.3, 7.3, 7.3, 7.3,
        #    73   74   75   76   77   78   79   80   81   82   83   84
            7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4,
        #    85   86    
            8.4, 7.5 ]

	#        1    2    3    4    5    6    7    8    9   10   11
lZmijonosa = [ 2.7, 2.7, 3.0, 3.6, 3.7, 5.2, 5.3, 5.3, 5.4, 5.4, 5.6,
	#       12   13   14   15   16   17   18   19   20   21   22
               5.6, 5.8, 6.4, 6.4, 6.4, 6.5, 6.5, 6.7, 6.8, 6.8, 6.9,
	#       23   24   25   26   27   28   29   30
               7.0, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.2 ]

	#         1    2    3    4    5    6    7    8    9   10   11
lHerkulLira = [ 2.3, 3.9, 4.2, 4.3, 4.5, 5.0, 5.5, 5.7, 5.7, 5.7, 5.7, 
	#        12   13   14   15   16   17   18   19   20   21   22
                5.9, 6.0, 6.0, 6.1, 6.2, 6.3, 6.5, 6.5, 6.8, 6.8, 6.8,
	#        23   24   25   26   27   28   29   30   31   32   33
                6.9, 6.9, 6.9, 6.9, 7.0, 7.0, 7.0, 7.0, 7.0, 7.1, 7.1,
        #        34   35   36   37   38   39   40   41   42   43   44
                7.1, 7.1, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.3, 7.4, 7.4,
        #        45   46   47   48   49   50   51   52
                7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.5 ]
 
	#    1    2    3    4    5    6    7    8    9   10   11   12 
lLabud = [ 2.3, 2.6, 4.0, 4.8, 4.8, 4.9, 5.0, 5.2, 5.2, 5.2, 5.5, 5.7,
        #   13   14   15   16   17   18   19   20   21   22   23   24
           5.9, 6.0, 6.1, 6.2, 6.2, 6.3, 6.3, 6.4, 6.4, 6.4, 6.4, 6.5,
	#   25   26   27   28   29   30   31   32   33   34   35   36
           6.5, 6.5, 6.5, 6.6, 6.6, 6.6, 6.6, 6.7, 6.7, 6.8, 6.8, 6.9,
	#   37   38   39   40   41   42   43   44   45   46   47   48
           6.9, 6.9, 6.9, 6.9, 7.0, 7.0, 7.0, 7.0, 7.0, 7.1, 7.1, 7.1,
        #   49   50   51   52   53   54   55   56   57   58   59   60 
           7.2, 7.2, 7.2, 7.2, 7.2, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3,
        #   61   62   63   64   65
           7.4, 7.4, 7.4, 7.4, 7.5 ]      

	#         1    2    3    4    5    6    7    8    9   10   11
lZmajHerkul = [ 3.0, 3.4, 3.9, 4.9, 5.1, 5.5, 5.9, 5.9, 5.9, 6.0, 6.0, 
	#        12   13   14   15   16   17   18   19   20   21   22
                6.1, 6.1, 6.1, 6.1, 6.1, 6.1, 6.3, 6.3, 6.3, 6.4, 6.6,
	#        23   24   25   26   27   28   29   30   31   32   33
                6.6, 6.6, 6.6, 6.7, 6.7, 6.7, 6.7, 6.7, 6.7, 6.9, 7.0,
        #        34   35   36   37   38   39   40   41   42   43   44
                7.0, 7.1, 7.1, 7.1, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2,
        #        45   46   47   48   49   50   51   52   53   54   55
                7.2, 7.2, 7.2, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.4, 7.4,
        #        56   57   58   59   60   61
                7.4, 7.4, 7.4, 7.4, 7.4, 7.5 ] 
               
	#         1    2    3    4    5    6    7    8    9   10   11
lLovackiPsi = [ 1.7, 1.9, 2.9, 4.6, 5.1, 5.7, 5.7, 5.9, 6.0, 6.0, 6.2, 
	#        12   13   14   15   16   17   18   19   20   21   22 
                6.2, 6.2, 6.4, 6.4, 6.4, 6.6, 6.6, 6.8, 6.8, 6.8, 6.9, 		#	 23   24   25   26   27   28   29   30   31   32   33
                6.9, 7.0, 7.0, 7.1, 7.2, 7.3, 7.3, 7.3, 7.3, 7.3, 7.4,
        #        34   35   36 
                7.4, 7.4, 7.5 ]     


             
        #      1    2    3    4    5    6    7    8    9   10   11   12
lKocijas = [ 0.2, 2.1, 2.7, 3.5, 3.9, 4.2, 4.2, 4.6, 5.1, 5.5, 5.9, 6.0,
        #     13   14   15   16   17   18   19   20   21   22   23   24
             6.0, 6.1, 6.1, 6.2, 6.3, 6.3, 6.3, 6.4, 6.4, 6.4, 6.4, 6.4,
        #     25   26   27   28   29   30   31   32   33   34   35   36 
             6.4, 6.5, 6.5, 6.5, 6.5, 6.6, 6.6, 6.6, 6.6, 6.6, 6.7, 6.7,
        #     37   38   39   40   41   42   43   44   45   46   47   48
             6.7, 6.8, 6.8, 6.8, 6.9, 6.9, 6.9, 7.0, 7.0, 7.0, 7.0, 7.0,
        #     49   50   51   52   53   54   55   56   57   58   59   60
             7.0, 7.1, 7.1, 7.1, 7.1, 7.1, 7.2, 7.2, 7.2, 7.2, 7.2, 7.3,
        #     61   62   63   64   65   66   67   68   69   70   71   72 
             7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.4, 7.4, 7.4, 7.4, 7.4,
        #     73   74   75   76   77   78   78   79   80   81  
             7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.5 ]  




        #        1    2    3    4    5    6    7    8    9   10   11
lAndromeda = [ 2.3, 3.9, 4.2, 4.3, 4.3, 5.0, 5.1, 5.1, 5.2, 5.5, 5.7, 
        #       12   13   14   15   16   17   18   19   20   21   22
               5.9, 6.1, 6.3, 6.3, 6.3, 6.4, 6.5, 6.5, 6.5, 6.5, 6.5, 
        #       23   24   25   26   27   28   29   30   31   32   33
               6.5, 6.6, 6.6, 6.6, 6.7, 6.7, 6.7, 6.7, 6.9, 6.9, 7.0,
        #       34   35   36   37   38   39   40   41   42   43   44
               7.0, 7.0, 7.0, 7.2, 7.2, 7.2, 7.2, 7.3, 7.3, 7.3, 7.3,
        #       45   46   47   48   49   50   51   52
               7.3, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.5 ]   



        #         1    2    3    4    5    6    7    8    9   10   11
lMaliMedved = [ 2.2, 3.6, 3.9, 5.2, 5.4, 5.7, 5.7, 6.1, 6.1, 6.1, 6.4,
        #        12   13   14   15   16   17   18   19   20   21   22
                6.6, 6.6, 6.7, 6.8, 7.0, 7.1, 7.2, 7.2, 7.2, 7.3, 7.3,
        #        23   24   25   26   27   28   29   30   31   32
                7.3, 7.3, 7.3, 7.3, 7.3, 7.4, 7.4, 7.4, 7.4, 7.5 ]
   
poligoni = [ lZmaj, lPersej, lVMedved, lBlizanci, lOrao, lPegaz, lCefej, lBik, lLav, lDevica, lVolar, lZmijonosa, lHerkulLira, lLabud, lZmajHerkul, lLovackiPsi, lKocijas, lAndromeda, lMaliMedved ]    



rows = []

polygonNames = ["Zmaj (Draco)", "Persej (Perseus)", "Veliki Medved (Ursa Major)", "Blizanci (Gemini)", "Orao (Aquila)", "Pegaz (Pegasus)", "Cefaj (Cepheus)", "Bik (Taurus)", "Lav(Leo)", "Devica (Virgo)", "Volar (Botes)",  "Vaga(Libra)", "Herkul/Lira (Hercules/Lyra)", "Labud (Cygnus)", "Herkul/Zmaj (Hercules/Draco)", "Lovacki Psi (Canes Veratici)", "Kocijas (Auriga)", "Andromeda (Andromeda)", "Mali Medved (Ursa Minor)"]


imageNames = ["poligon1.jpg", "poligon2.jpg", "poligon3.jpg", "poligon4.jpg","poligon5.jpg", "poligon6.jpg", "poligon7.jpg", "poligon8.jpg", "poligon9", "poligon10.jpg", "poligon11.jpg", "poligon12.jpg","poligon13.jpg", "poligon14.jpg", "poligon15.jpg", "poligon16.jpg", "poligon17.jpg", "poligon18.jpg", "poligon19.jpg" ]

	
limits = [ 73, 59, 54, 30, 27, 49, 65, 32, 45, 31, 86, 30, 52, 65, 61, 36, 
           81, 52, 32 ]     
                                                                        
class Row:
        def __init__(self, parent, text, imgPath, limit):
                
                self.frame = Frame(parent)
                self.frame.pack(fill=X)
                self.text = text
                self.lbl = Button(self.frame, text=text, width=25, command=self.display)
                self.lbl.pack(side=LEFT, padx=10, pady=3)
                self.imgPath = imgPath
                self.limit = limit
                self.entry = Entry(self.frame)
                self.entry.pack(fill=X, padx=10, expand=True)

        def display(self):
                root = Toplevel()
                root.wm_title(self.text)

                path = "New/" + self.imgPath
                pomoc = Image.open(path)

                basewidth = 600
                wpercent = (basewidth/float(pomoc.size[0]))
                hsize = int((float(pomoc.size[1])*float(wpercent)))

                pomoc = pomoc.resize((basewidth, hsize), Image.LANCZOS)
                img = ImageTk.PhotoImage(pomoc)

                panel = Label(root, image = img)
                panel.image = img
                panel.pack()

                root.mainloop()      
                

                
class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()

        
    def initUI(self):
      
        self.master.title("Poligon Poligon")
        self.pack(fill=BOTH, expand=True, pady=5)
	
        frames = []
        
        
        for i, polygonName in enumerate(polygonNames):
                rows.append(Row(self, polygonName, imageNames[i], limits[i]))                    
	               
	####################
        
        
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
def losUnos():
        messagebox.showinfo("Porukica", "Los unos")
def clearButtonClick():
        for row in rows:
                row.entry.delete(0, "end")                
def isNumber(s):
        try:
                float(s)        
                return True
        except ValueError:
                return False
           
def isOkay(number):
        for row in rows:
                if (row.limit < number):
                        return False
                else:
                        return True

def calculateButtonClick():
        br = 0.0
        pomocBr = 0.0
        im = 0.0
        allGood = True
        for i, row in enumerate(rows):
                entry = row.entry
                if (len(entry.get()) != 0):
                        if (isNumber(entry.get()) == False):
                                losUnos()
                                clearButtonClick()
                                return
                        else:
                                valueOfEntry =  float(entry.get())
                                if isOkay(valueOfEntry) == False:
                                        losUnos()
                                        clearButtonClick()
                                        return
                                else:
                                        pomocBr = findLMG(poligoni[i], valueOfEntry, pomocBr)
                                        br = br + pomocBr
                                        im = im + 1              
                
        if (im > 1):
                LMG = br/im
                message = "Vrednost LMG-a je :" + str(round(LMG, 2))
                sayLMG(message)
        else:
                premaloPoligona()
       

def main():
  
    root = Tk()
    root.geometry("300x640+300+50")
    app = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()  
