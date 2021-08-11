import requests
import json
import time
import threading
import tkinter
from tkinter import font

from os import system
from time import sleep
from _operator import pos, le


    
class WTapp(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        self.grid()
        
        
        self.req = None 
        self.parametr_lotu = None
        self.lista_parametrow = []
        self.dane = None   
        self.tablica_danych = []
        self.przeksztalcone_ciagi = []
        self.licznik = 0
        self.licz_do_odswiezenia = 0
        
        self.font = tkinter.font.Font(self, family = 'Arial', size = 16, weight = 'bold', slant = 'roman', overstrike = 0, underline = 0)

        self.lbl = None
        
        self.pobierz()
        self.gui()
        
        
        
        
        if self.dane != None:     
            self.tablica_danych = self.konwertuj_ciagi(self.dane)
        
        
        
        
    def gui(self):
        
        if self.pobierz() == False:
            if self.lbl:
                
                self.lbl.config(text = 'Brak połączenia')
            elif self.lbl == None:
                self.lbl = tkinter.Label()
                self.lbl.config(font = self.font)
                self.lbl.config(text = 'Brak połączenia')
                self.lbl.grid()
                
       
        #print(str(type(self.parametr_lotu)))
        
        if self.tablica_danych:
            r1 = 1
            r2 = 1
            r3 = 1
            r4 = 1
            r5 = 1
            r6 = 1
            rr = 0
            c = 0
            
            
            if self.przeksztalcone_ciagi:
                
                if self.lista_parametrow:
                    for i in self.lista_parametrow:
                        i.destroy()
                
                for i in self.przeksztalcone_ciagi:
                              
                
                    self.parametr_lotu = tkinter.Label(self, text = str(i), font = self.font, padx = 10)
                
                
                #if i[0:8] == 'throttle':
                    if '1:' in i:    
                    #r = 1
                    #c = int(i[9:10])
                        c = 1
                        self.parametr_lotu.grid(column =  c, row = r1)
                        r1 += 1
                    elif '2:' in i:    
                            c = 2
                            self.parametr_lotu.grid(column =  c, row = r2)
                            r2 += 1
                    elif '3:' in i:    
                        c = 3
                        self.parametr_lotu.grid(column =  c, row = r3)
                        r3 += 1
                    elif '4:' in i:    
                        c = 4
                        self.parametr_lotu.grid(column =  c, row = r4)
                        r4 += 1
                    elif '5:' in i:    
                        c = 5
                        self.parametr_lotu.grid(column =  c, row = r5)
                        r5 += 1
                    elif '6:' in i:    
                        c = 6
                        self.parametr_lotu.grid(column =  c, row = r6)
                        r6 += 1
                    else:
                        c = 0
                        self.parametr_lotu.grid(column =  c, row = rr)
                        rr += 1
                        
                    self.lista_parametrow.append(self.parametr_lotu)
            else:
                pass
                
                    
                
                #self.gui()
                
    
    def polacz(self):    
        try:
            self.req = requests.get('http://127.0.0.1:8111/state')
        except:
            print('Brak połączenia')
            self.gui()
            self.lbl.config(text = 'Brak połączenia')
            return False
        
        return True
        
   
        
         
    def pobierz(self):
        try:
            #if self.lbl == None:
            #    self.lbl = tkinter.Label(self, text = 'X', font = self.font)
            #    self.lbl.grid(column = 0, row = 0)
            #else:
                #self.lbl.config(text = 'X', font = self.font)
            
            self.req = requests.get('http://127.0.0.1:8111/state')
        except:
            self.licznik += 1
            print('Brak połączenia ' + str(self.licznik))
            return False
            #self.lbl.config(text = 'Brak połączenia - oczekiwanie...')
            #sleep(5)
            #self.pobierz()
            #self.after(5000, self.pobierz)
        else:
            self.dane = self.req.json()
        
        
        
        if self.dane != None:
            self.tablica_danych = self.konwertuj_ciagi(self.dane)
            return self.tablica_danych
        else:
            return False
       
        ##rozkodowane = json.loads(self.req.content)
        
        
        
    def przerysuj(self):
        for i in self.lista_parametrow:
            pass
           # i.config(text)    
        

        
       
    
    def pobieraj(self):
        dlugosc = len(self.tablica_danych)
        self.pobierz()
        if dlugosc != len(self.tablica_danych):
            self.gui()
        else:
            for i in self.tablica_danych:
                for j in self.lista_parametrow:
                    if type(j) == tkinter.Label:
                        j.config(text = 'a')
       # j = 0
        #if self.przeksztalcone_ciagi != []:
         #   for i in self.lista_parametrow:
#        #    i.config(text='a') 
         #       i.destroy()
         #       print(str(type(i)))
           
        
        self.licz_do_odswiezenia += 1
        if self.licz_do_odswiezenia >= 4:
            print('odswiezam')
            self.licz_do_odswiezenia = 0
            for i in self.lista_parametrow:
                print(str(type(i)))
            self.gui()
        
        self.after(500, self.pobieraj)
            
    def konwertuj_ciagi(self, slownik):
        lista = list()
        self.przeksztalcone_ciagi.clear()
        for i in slownik.items():
            rozdziel = i[0].split(', ')
            parametr = rozdziel[0]
            if len(rozdziel) > 1:
                jednostka = rozdziel[1]
            else:
                jednostka = None
            wartosc = i[1]
              
            ciag = parametr + ': '# + wartosc
            if wartosc != None:
                ciag += str(wartosc) 
            if jednostka != None:
                ciag += jednostka  
                
               
            # ciag[0] = str(ciag[0]).upper()
            self.przeksztalcone_ciagi.append(ciag)
             
            #  print(i[0])
        #print(self.przeksztalcone_ciagi)
        return self.przeksztalcone_ciagi
    
    def nasluch(self):
        system('cls')
        if self.pobierz() != None:
            for i in self.pobierz():
                print(i)
        #sleep(0.25)
        

if __name__ == '__main__':
    root = tkinter.Tk()
    root.resizable(width = True, height = True)
    root.title('WTapp')
    frm = WTapp(root)
    
    ##t = threading.Thread(target = frm.pobieraj)
    ##t.daemon = False
    ##t.start()
    root.after(100, frm.pobieraj)
    root.mainloop()
    
    
    
    
    
    
    
    
