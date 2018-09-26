from tkinter import *
import pandas as pd
import csv
from tkinter.messagebox import *
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from pylab import rcParams
import os
from sklearn.metrics import r2_score
#rcParams['figure.figsize'] = 10, 10



xlist = []#für die grafik
    
danzagrafik = []   #tage für die Grafik
ylist = []#für die grafik
Datumi = [] # Array für dir Datums 
danikojisustvarni = [] '
xi = []
KolY = []

        
def statistik():
   
   Mon = Monat.get()
   dan = [Tage.get()]
   art = Artikl.get()
   Datum1 = int(DatumOd.get())
   Datum2 = int(DatumDo.get())
   Aktion = akt.get()
    
   listsplit = []

   for dn in dan: #split zza unetu listudana

      splited = dn.split(",")

      listsplit.append(splited)


   with open("ABG_5J_OG.csv", "r") as baza:
         
            

      kol = []

      
   
      for i in baza:
	      

         v = i.strip().split(";")
         
         
         
         
         if v[0] == "DATC":
            continue
         
         if int(v[0]) >= Datum1 and int(v[0]) <= Datum2:
            mon = (v[0][4:6])
            if mon == Mon :

               Datumi.append(v) #filtrirana lista sa odredjenim datumima 
            elif len(Mon) == 0:
               
               Datumi.append(v)
               
      for v in Datumi:
         Art = v[2]
         Akt = v[4][:3]


         if art == Art:


            for dan in listsplit:

               for b in range(0,len(dan)):

                  
                  

                  if dan[b] in v:
                     if Aktion == "J":
                        if Akt == "SOG":
                           #print("Wen Aktion " + str(v))
 
                           if "," in v[3]:
                              vs = v[3].split(",")
                              xlist.append((v[0][2:]))#für grafik
                              ylist.append(int(vs[0]))#für grafik
                              danzagrafik.append(v[1])


                              danikojisustvarni.append(dan[b])

                              kol.append(int(vs[0]))
                           elif int(v[3]) < 0 :
                              continue
                           
                           else:
                              

                              xlist.append((v[0][2:]))#für grafik
                              ylist.append(int(v[3]))#für grafik
                              danzagrafik.append(v[1])
                              #print(v)


                              danikojisustvarni.append(dan[b])

                              kol.append(int(v[3]))
                              

                     if Aktion == "N":
                        if Akt == "" :
                           #print("Nicht Aktion " + str(v))
                           if "," in v[3]:
                              vs = v[3].split(",")
                              xlist.append((v[0][2:]))#für grafik
                              ylist.append(int(vs[0]))#für grafik
                              danzagrafik.append(v[1])


                              danikojisustvarni.append(dan[b])

                              kol.append(int(vs[0]))
                           elif int(v[3]) < 0 :
                              continue
                           
                           else:
                              

                              xlist.append((v[0][2:]))#für grafik
                              ylist.append(int(v[3]))#für grafik
                              danzagrafik.append(v[1])
                              #print(v)


                              danikojisustvarni.append(dan[b])

                              kol.append(int(v[3]))
                     elif Aktion != "N" and Aktion != "J":
                        #print("Wenn beide nicht zutreffen " + str(v))
                        
                        if "," in v[3]:
                           
                           
                              vs = v[3].split(",")
                              xlist.append((v[0][2:]))#für grafik
                              ylist.append(int(vs[0]))#für grafik
                              danzagrafik.append(v[1])


                              danikojisustvarni.append(dan[b])

                              kol.append(int(vs[0]))
                        elif int(v[3]) < 0 :
                           
                           continue
                           
                        else:
                           
                              

                           xlist.append((v[0][2:]))#für grafik
                           ylist.append(int(v[3]))#für grafik
                           danzagrafik.append(v[1])
                           #print(v)


                           danikojisustvarni.append(dan[b])

                           kol.append(int(v[3]))
                     
                  

                                                            
      try:
            
         kolicina = ( np.median(kol) * len(set(danikojisustvarni)))

         ###für Median Graph ##########
         for i in range (0,len(ylist)):

            KolY.append(np.median(kol))
         
         ##############################
 

         roundet = round(np.median(kol),2)
         blank.insert(0,roundet)
        
         

      except :
         
         if len(art) > 6 or len(art) < 6:
            
                
                
            v = "bei Artnmr. nur 6 zahlen eingeben  "

            
                
def ploting():
   sens = int(Sens.get())
   
   
   
   xs =xlist
   ys= ylist
   pred = np.polyfit(xi,ys,sens)
   

          
   plt.plot(xs,ys,label = "Mengen as 400")

   plt.plot(xi,(np.polyval(pred,xi)),label="Prognose")
   polyValue  = (np.polyval(pred,xi)[-1])
   plt.plot(xs,KolY,label="Mittelwert")
   
   
   plt.xticks(xs)
   plt.yticks(ys)
   plt.grid()
   plt.xlabel(" Datum ")
   plt.ylabel("Menge")
   plt.title("Mengen für tag " + str(set( danzagrafik))[2:4])
   
   plt.legend()


   plt.show()

   

def predict():
   sens = int(Sens.get())
   
   xs =xlist
   
   ys= ylist
   ########################## für die vorhersage im feld von gui
   for i in range(0,len(xs)):
      
      xi.append(i+1)

   pred = np.poly1d(np.polyfit(xi,ys,sens))
   polyValue  = (np.polyval(pred,xi)[-1])
   x  = np.array(xi)
   y = np.array(ys)
   
   r3 = r2_score(ys,pred(xi)*len(set(danikojisustvarni)))
   R2.insert(0,round(r3,2))
 

   Predict.insert(0, round(polyValue ,2)* len(set(danikojisustvarni)) )
   
   

def zajedno():
   statistik()
   predict()

   
def delete_entries():
   
  for field in fields:
     
      field.delete(0,END)

def nuliranje():
   del xlist[:]
   del ylist[:]
   del danzagrafik[:]   
   
   del Datumi[:]
   del danikojisustvarni[:]
   del xi[:]
   del KolY [:]
def brisanje():
   delete_entries()
   nuliranje()
   
#GUI####
###########################################################################
   
main = Tk()
main.configure(background='white')

bild=PhotoImage(file=r"einfache-Statistik.png")

bildLabel = Label(image=bild,bg ="white").grid(column = 2,rowspan=7)
     


main.title("Dalibor's Programm")
Label(main, text = "Welchen Artikel suchen wir? :",bg ="white",fg = "red",font = "Verdana 10 bold").grid(row=0)

Label(main, text = "Für welche Tage brauchen wir die Menge ? ZB.(MO,DI...)" ,bg ="white",font = "Verdana 10 bold").grid(row=1)
Label(main, text = "Datum von : (JJJJMMTT)",bg ="white",font = "Verdana 10 bold").grid(row=2)
Label(main, text = "Datum bis : (JJJJMMTT)",bg ="white",font = "Verdana 10 bold").grid(row=3)
Label(main, text = "Empfindlichkeit : (DEFAULT IST 3)" ,bg ="white",font = "Verdana 10 bold").grid(row=4)
Label(main, text = "Für welchen Monat :  ZB.(01,02..)",bg ="white",font = "Verdana 10 bold").grid(row=5)
Label(main, text = "Aktions Artikel  (J/N) " ,bg ="white",font = "Verdana 10 bold").grid(row=6)
Label(main, text = "Gebrauchte Summe Median:",bg ="white",font = "Verdana 10 bold").grid(row=7)
Label(main, text = "PredictSum:",bg ="white",font = "Verdana 10 bold").grid(row=8)
Label(main, text = "Determinationskoeffizient(R2):",bg ="white",font = "Verdana 10 bold").grid(row=9)


Artikl = Entry(main,font = "Helvetica 12 bold",width=10,fg="yellow",bg="gray")
Tage = Entry(main,font = "Helvetica 12 bold",width=10,fg="yellow",bg="gray")
DatumOd = Entry(main,font = "Helvetica 12 bold",width=10,fg="yellow",bg="gray")
DatumDo= Entry(main,font = "Helvetica 12 bold",width=10,fg="yellow",bg="gray")
Sens = Entry(main,font = "Helvetica 12 bold",width=10,fg="yellow",bg="gray")
Monat= Entry(main,font = "Helvetica 12 bold",width=10,fg="yellow",bg="gray")
akt= Entry(main,font = "Helvetica 12 bold",width=10,fg="yellow",bg="gray")

blank = Entry(main,font = "Helvetica 12 bold",width=10,fg="yellow",bg="gray")
Predict = Entry(main,font = "Helvetica 12 bold",width=10,fg="yellow",bg="gray")
R2 = Entry(main,font = "Helvetica 12 bold",width=10,fg="yellow",bg="gray")



Artikl.grid(row=0, column=1)
Tage.grid(row=1, column=1)
DatumOd.grid(row=2, column=1)
DatumDo.grid(row=3, column=1)
Sens.grid(row=4, column=1)

Monat.grid(row=5, column=1)
akt.grid(row=6, column=1)
blank.grid(row=7, column=1)
Predict.grid(row=8, column=1)
R2.grid(row=9, column=1)



fields = blank, Predict,R2#,DatumOd,DatumDo,Monat,Artikl,Tage


Button(main, text='Schliesen', command=main.destroy).grid(row=10, column=0, sticky=W, pady=4)
Button(main, text='Berechnen', command=zajedno).grid(row=10, column=1, sticky=W, pady=4)
Button(main, text='Graphik Anzeigen', command=ploting).grid(row=10, column=2, sticky=W, pady=4)
Button(main, text='Reset', command=brisanje).grid(row=10, column=3, sticky=W, pady=4)

    
mainloop()

   

