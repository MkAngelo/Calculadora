from tkinter import * #Elementos graficos
from  math import * #Libreria de mate

ventana = Tk()

ventana.title('CALCULADORA')
ventana.geometry("400x500")
ventana.resizable(False,False)
ventana.configure(background="gray42")

color_boton="gray99"
ancho_boton=10
alto_boton=3
operador = ""
texto_pantalla = StringVar()

def clear():
    global operador
    operador = ""
    texto_pantalla.set("0")

def click(b):
    global operador
    operador += str(b)
    texto_pantalla.set(operador)

def resultado():
    global operador
    try:
        r = str(eval(operador))
    except:
        r = "ERROR :("
    texto_pantalla.set(r)

clear()
#BOTONES DE LA PRIMERA FILA
BotonParIzq = Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("(")).grid(row=1,column=0,pady=10)
BotonParDer = Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(")")).grid(row=1,column=1,pady=10)
BotonClear = Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).grid(row=1,column=2,pady=10)
BotonMultiplicar = Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("*")).grid(row=1,column=3,pady=10)

#BOTONES DE LA SEGUNDA FILA}
Boton7 = Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(7)).grid(row=2,column=0,pady=10)
Boton8 = Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(8)).grid(row=2,column=1,pady=10)
Boton9 = Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(9)).grid(row=2,column=2,pady=10)
BotonDivision = Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("/")).grid(row=2,column=3,pady=10)

#BOTONES DE LA TERCERA FILA
Boton4 = Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(4)).grid(row=3,column=0,pady=10)
Boton5 = Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(5)).grid(row=3,column=1,pady=10)
Boton6 = Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(6)).grid(row=3,column=2,pady=10)
BotonResta = Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("-")).grid(row=3,column=3,pady=10)

#BOTONES DE LA CUARTA FILA
Boton1 = Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(1)).grid(row=4,column=0,pady=10)
Boton2 = Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(2)).grid(row=4,column=1,pady=10)
Boton3 = Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(3)).grid(row=4,column=2,pady=10)
BotonSuma = Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("+")).grid(row=4,column=3,pady=10)

#BOTONES DE LA QUINTA FILA
BotonExp = Button(ventana,text="Exp",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("**")).grid(row=5,column=0,pady=10)
Boton0 = Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(0)).grid(row=5,column=1,pady=10)
BotonPunto = Button(ventana,text=".",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(".")).grid(row=5,column=2,pady=10)
BotonResultado = Button(ventana,text="=",bg="orange",width=ancho_boton,height=alto_boton,command=resultado).grid(row=5,column=3,pady=10)

Pantalla = Entry(ventana,font=("arial",20,"bold"),width=22,borderwidth=10,background="CadetBlue1",textvariable=texto_pantalla)
Pantalla.grid(row=0,column=0,columnspan=4,padx=20,pady=20)

ventana.mainloop() #Siempre va al ultimo xd
