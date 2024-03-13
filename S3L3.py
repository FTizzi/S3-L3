run = True
while run == True:
         print("Calcolo Del Perimetro")
         print("""
         - Quadrato   >> 1
         - Cerchio    >> 2
         - Rettangolo >> 3
         - EXIT       >> 4
    
        """)
   
         print('Scelgliere Figura:')
         scelta = int(input(">>"))
         if scelta == 1:
                 print ("Quadrato")
                 lato = float(input('Valore Lato '))
                 print("Perimetro = Lato",lato," x 4 = ",lato *4)
   
         elif scelta == 2:
                 print ("Cerchio")
                 r = float(input('Valore Raggio'))
                 print("Perimetro = Raggio",r,"2 x r x 3.14 = ",2* r* 3.14) 
    
         elif scelta == 3:
                 print ("Rettangolo")
                 base = float(input('Valore Base '))
                 altezza = float(input('Valore altezza '))
                 print("Perimetro = Base",base,"x 2 + " "Altezza",altezza, "x 2" " = ",base *2 + altezza *2)
   
         elif scelta == 4:
              break
         else:
                 print ("""
                 Scelta Non Valida
                 """)
              