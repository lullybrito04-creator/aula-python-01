import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulario")
janela.geometry("300x300")
#entrada de texto 
tk.Label(janela, text= "Nome:", font=("Arial")).grid(row=0, column=0)
entrada_nome = tk.Entry(janela, font=("Arial"))
entrada_nome.grid(row=0, column=1)

#radiobtton
opc = tk.IntVar()
tk.Label(janela, text= "Sexo" , font= ("Arial")).grid(row=2,column=0)
tk.Radiobutton(janela, text="Masculino", font= ("Arial"),value=1 , Variable=opc)\
.grid(row=3,column=1)
tk.Radiobutton(janela, text="Feminino", font=("Arial"), value=2, variable=opc)\
.grid(row=4,column=1)


janela.mainloop()