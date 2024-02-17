from tkinter import *   
from tkinter import ttk 

# variáveis como cores
cor1 = "#000000" # preto
cor2 = "#727272" # cinza 
cor3 = "#ffffff" # branco 
cor4 = "#fff000" # amarelo

# criar um construtor chamado janela que recebe tk do pacote tkinter
janela = Tk()
janela.title("Calculadora")
janela.geometry("390x350") 
janela.config(bg=cor2)


# frames, divisões da janela
frame_tela = Frame(janela, width=400, height=75)
frame_tela.grid(row=0, column=0)
frame_tela.config(bg=cor4)

frame_corpo = Frame(janela, width=400, height=325)
frame_corpo.grid(row=1, column=0)

# funcao de calculo
def input_values(event):
    resultado =eval('9/9')
    valor_texto.set(resultado)





# label
    
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=29, height=3, padx=9, relief=FLAT, anchor="e", justify=RIGHT, font=('Arial', 18, 'bold'))
app_label.place(x=0,y=0)


#botoes de comando

# primeira fileira
b_1 = Button(frame_corpo, text="c", width="12", height=3)
b_1.place(x=0,y=0) 
b_2 = Button(frame_corpo, text="%", width="12", height=3, command=lambda: input_values('%'))
b_2.place(x=130,y=0) 
b_3 = Button(frame_corpo, text="/", width="12", height=3)
b_3.place(x=260,y=0)


# segunda fileira
b_8 = Button(frame_corpo, text="7", width="8", height=3)
b_8.place(x=0,y=55) 
b_9 = Button(frame_corpo, text="8", width="8", height=3)
b_9.place(x=100,y=55) 
b_10 = Button(frame_corpo, text="9", width="8", height=3)
b_10.place(x=200 ,y=55) 
b_11 = Button(frame_corpo, text="x", width="8", height=3)
b_11.place(x=300 ,y=55)

# terceira fileira
b_12 = Button(frame_corpo, text="4", width="8", height=3)
b_12.place(x=0, y=110)
b_13 = Button(frame_corpo, text="5", width="8", height=3)
b_13.place(x=100, y=110)
b_14 = Button(frame_corpo, text="6", width="8", height=3)
b_14.place(x=200, y=110)
b_15 = Button(frame_corpo, text="-", width="8", height=3)
b_15.place(x=300, y=110)

# quarta fileira
b_16 = Button(frame_corpo, text="1", width="8", height=3)
b_16.place(x=0, y=165)
b_17 = Button(frame_corpo, text="2", width="8", height=3)
b_17.place(x=100, y=165)
b_18 = Button(frame_corpo, text="3", width="8", height=3)
b_18.place(x=200, y=165)
b_19 = Button(frame_corpo, text="+", width="8", height=3)
b_19.place(x=300, y=165)

# quinta fileira
b_20 = Button(frame_corpo, text="0", width="8", height=2)
b_20.place(x=0, y=220)
b_21 = Button(frame_corpo, text=",", width="8", height=2)
b_21.place(x=100, y=220)
b_22 = Button(frame_corpo, text="=", width="18", height=2) 
b_22.place(x=200, y=220)



# 1:01:27 / 1:30:28



# ajuste de layout
for widget in frame_corpo.winfo_children():
    widget.configure(bg=cor1, fg=cor3, activebackground=cor3, activeforeground=cor1, font=('Arial', 13, 'bold'))



janela.mainloop()

