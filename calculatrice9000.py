from tkinter import *
 
formule = "" 
 
def click(num): 
 
    global formule 
    formule = formule + str(num) 
    equation.set(formule) 

# clique
 
def equalclick(): 
    try: 
        global formule 
 
        result = str(eval(formule)) 
        equation.set(result) 
        formule = result
 
    except: 
        equation.set(" ---Erreur--- ")
        formule = "" 

# essayez le calculs et voir si il y a une erreur

 
def effacer(): 
    global formule 
    formule = "" 
    equation.set("") 
 
if __name__ == "__main__": 
    block = Tk() 
    block.title("Calculatrice 9000") 
    block.geometry("515x415") 
    equation = StringVar() 
    formule_field = Entry(block, textvariable=equation) 
    formule_field.grid(columnspan=4,  pady= 30 , padx = 20 , ipadx = 100 , ipady = 10)
    btn_1 = Button(block, text=' 1 ', command=lambda: click(1), height=2, width=10) 
    btn_1.grid(row=2, column=0) 
 
    btn_2 = Button(block, text=' 2 ', command=lambda: click(2), height=2, width=10) 
    btn_2.grid(row=2, column=1) 
 
    btn_3 = Button(block, text=' 3 ', command=lambda: click(3), height=2, width=10) 
    btn_3.grid(row=2, column=2) 
 
    btn_4 = Button(block, text=' 4 ', command=lambda: click(4), height=2, width=10) 
    btn_4.grid(row=3, column=0) 
 
    btn_5 = Button(block, text=' 5 ', command=lambda: click(5), height=2, width=10) 
    btn_5.grid(row=3, column=1) 
 
    btn_6 = Button(block, text=' 6 ', command=lambda: click(6), height=2, width=10) 
    btn_6.grid(row=3, column=2) 
 
    btn_7 = Button(block, text=' 7 ', command=lambda: click(7), height=2, width=10) 
    btn_7.grid(row=4, column=0) 
 
    btn_8 = Button(block, text=' 8 ', command=lambda: click(8), height=2, width=10) 
    btn_8.grid(row=4, column=1) 
 
    btn_9 = Button(block, text=' 9 ', command=lambda: click(9), height=2, width=10) 
    btn_9.grid(row=4, column=2) 
 
    btn_0 = Button(block, text=' 0 ', command=lambda: click(0), height=2, width=10) 
    btn_0.grid(row=5, column=0) 
 
    plus = Button(block, text=' + ', command=lambda: click("+"), height=2, width=10) 
    plus.grid(row=2, column=3) 
 
    minus = Button(block, text=' - ', command=lambda: click("-"), height=2, width=10) 
    minus.grid(row=3, column=3) 
 
    multiply = Button(block, text=' * ', command=lambda: click("*"), height=2, width=10) 
    multiply.grid(row=4, column=3) 
 
    divide = Button(block, text=' / ', command=lambda: click("/"), height=2, width=10) 
    divide.grid(row=5, column=3) 
 
    equal = Button(block, text=' = ', command=equalclick, height=2, width=10) 
    equal.grid(row=5, column=2) 
 
    effacer = Button(block, text='Effacer', command=effacer, height=2, width=10) 
    effacer.grid(row=6, column=3) 
 
    Decimal = Button(block, text='.', command=lambda: click('.'), height=2, width=10) 
    Decimal.grid(row=5, column=1) 
    
    percent= Button(block, text='%', command=lambda: click('%'), height=2, width=10) 
    percent.grid(row=6, column=1)   

    racine_carree = Button(block, text="\U0000221A", command=lambda: click("**0.5"), height=2, width=10) 
    racine_carree.grid(row=6, column=1) 

    puissance_carree = Button(block, text="x\U000000B2", command=lambda: click("**2"), height=2, width=10) 
    puissance_carree.grid(row=6, column=0)   

    #créer les cases, les placées  et leurs donner leurs valeurs
    
    block.mainloop()

    #affiche 
