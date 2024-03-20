# Importando as bibliotecas necessárias
from tkinter import *  # Importando a biblioteca Tkinter
from tkinter import ttk  # Importando a biblioteca ttk
import os  # Importando a biblioteca os


# Obtém o diretório do script Python
script_dir = os.path.dirname(os.path.realpath(__file__))

# Constrói o caminho para o arquivo de ícone
icon_path = os.path.join(script_dir, 'assets/icon/cal.ico')

# Criando a janela
win = Tk()  # Criando a janela principal
win.title("Calculadora")  # Definindo o título da janela
win.geometry("305x400")  # Definindo o tamanho da janela
win.resizable(False, False) # Definindo que a janela não pode ser redimensionada
win.config(bg="#ffffff")  # Definindo a cor de fundo da janela
win.iconbitmap(icon_path)

# Criando os frames display
frame_display = Frame(win, width = 295, height = 45, bg = "#000")  # Criando um frame para a tela display
frame_display.place(x = 5, y = 2)  # Adicionando o frame na janela display

# Criando o frame body
frame_body = Frame(win, width = 295, height = 340, bg = "#000")  # Criando um frame para a tela body
frame_body.place(x = 5, y = 55)   # Adicionando o frame na janela body 


# Aplicando a função logica dos botões
valores = ""  # Criando uma variável para armazenar os valores
def Entrada_valores(e):
    global valores # Definindo a variável como global
    valores = valores + str(e) # Adicionando os valores na variável
    texto_função.set(valores) # Adicionando o resultado na tela display

# Criando a função para calcular os valores
def Calcular():
    global valores # Definindo a variável como global
    resultado = eval(valores) # Calculando os valores   
    texto_função.set(resultado)  # Adicionando o resultado na tela display

# Criando a função para limpar a tela display
def Limpar_display():
    global valores # Definindo a variável como global
    valores = "" # Limpando a variável
    texto_função.set(valores) # Adicionando o resultado na tela display

# Criando a função para limpar caracteres do display
def Limpar_caracteres():
    global valores # Definindo a variável como global
    valores = valores[:-1] # Limpando a variável
    texto_função.set(valores) # Adicionando o resultado na tela display
    

# Criando label da tela display
texto_função = StringVar()  # Criando uma variável para a label
app_display = Label(
    frame_display, 
    width = 16, textvariable = texto_função, 
    font = ("Ivy 20 bold"), bg = "#000", fg = "#ffffff", 
    justify = RIGHT, padx = 7, relief = FLAT, anchor = "e"
)  # Criando a label da tela display
app_display.place(x = 5, y = 5)  # Adicionando e ajustando a label na janela display

# Criando a btns de números
btn_c = Button(
    frame_body, command = Limpar_display,
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE,  
    text = "C", fg = "#ffffff", bg = "#8b008b", 
    width = 13, height = 3
) 
btn_c.place(x = 5, y = 5)  # Adicionando e ajustando o botão na janela body    

btn_x = Button(
    frame_body, command = Limpar_caracteres, 
    font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, 
    text = "< X", fg = "#ffffff", bg = "#8b008b", 
    width = 7, height = 3
)  
btn_x.place(x = 109, y = 5) # Adicionando e ajustando o botão na janela body  

btn_porc = Button(
    frame_body, command = lambda: Entrada_valores("%"),
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE,
    text = "%", fg = "#000", bg = "#00ff00", 
    width = 7, height = 3
)
btn_porc.place(x = 170, y = 5) # Adicionando e ajustando o botão na janela body 

btn_div = Button(
    frame_body, command=lambda: Entrada_valores("/"),
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE, 
    text = "/", fg = "#000", bg = "#00ff00", 
    width = 7, height = 3
)  
btn_div.place(x = 231, y = 5) # Adicionando e ajustando o botão na janela body

btn_7 = Button(
    frame_body, command=lambda: Entrada_valores("7"),
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE, 
    text = "7", fg = "#ffffff", bg = "#1C1C1C", 
    width = 9, height = 4
) 
btn_7.place(x = 5, y = 63) # Adicionando e ajustando o botão na janela body  

btn_8 = Button(
    frame_body, command=lambda: Entrada_valores("8"),
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE, 
    text = "8", fg = "#ffffff", bg = "#1C1C1C", 
    width = 9, height = 4
)  
btn_8.place(x = 80, y = 63) # Adicionando e ajustando o botão na janela body

btn_9 = Button(
    frame_body, command=lambda: Entrada_valores("9"), 
    font=("Ivy 8 bold"), 
    relief=RAISED, overrelief=RIDGE, 
    text="9", fg="#ffffff", bg="#1C1C1C", 
    width=9, height=4
)
btn_9.place(x = 156, y = 63) # Adicionando e ajustando o botão na janela body

btn_Ast = Button(
    frame_body, command=lambda: Entrada_valores("*"), 
    font=("Ivy 8 bold"), 
    relief=RAISED, overrelief=RIDGE, 
    text="*", fg="#000", bg="#00ff00", 
    width=7, height=4
)
btn_Ast.place(x = 231, y = 63) # Adicionando e ajustando o botão na janela body  

btn_4 = Button(
    frame_body, command = lambda: Entrada_valores("4"), 
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE, 
    text = "4", fg = "#ffffff", bg = "#1C1C1C", 
    width = 9, height = 4
) 
btn_4.place(x = 5, y = 131) # Adicionando e ajustando o botão na janela body

btn_5 = Button(
    frame_body, command = lambda: Entrada_valores("5"), 
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE, 
    text = "5", fg = "#ffffff", bg = "#1C1C1C", 
    width = 9, height = 4
) 
btn_5.place(x = 80, y = 131) # Adicionando e ajustando o botão na janela body

btn_6 = Button(
    frame_body, command = lambda: Entrada_valores("6"), 
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE, 
    text = "6", fg = "#ffffff", bg = "#1C1C1C", 
    width = 9, height = 4
) 
btn_6.place(x = 156, y = 131)  # Adicionando e ajustando o botão na janela body

btn_sub = Button(
    frame_body, command = lambda: Entrada_valores("-"), 
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE, 
    text = "-", fg = "#000", bg = "#00ff00", 
    width = 7, height = 4
) 
btn_sub.place(x = 231, y = 131) # Adicionando e ajustando o botão na janela body  

btn_3 = Button(
    frame_body, command = lambda: Entrada_valores("3"), 
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE, 
    text = "3", fg = "#ffffff", bg = "#1C1C1C", 
    width = 9, height = 4
)  
btn_3.place(x = 5, y = 198) # Adicionando e ajustando o botão na janela body

btn_2 = Button(
    frame_body, command = lambda: Entrada_valores("2"), 
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE, 
    text = "2", fg = "#ffffff", bg = "#1C1C1C", 
    width = 9, height = 4
)  
btn_2.place(x = 80, y = 198) # Adicionando e ajustando o botão na janela body

btn_1 = Button(
    frame_body, command = lambda: Entrada_valores("1"), 
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE, 
    text = "1", fg = "#ffffff", bg = "#1C1C1C", 
    width = 9, height = 4
)  
btn_1.place(x = 156, y = 198) # Adicionando e ajustando o botão na janela body

btn_Ad = Button(
    frame_body, command = lambda: Entrada_valores("+"), 
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE, 
    text = "+", fg = "#000", bg = "#00ff00", 
    width = 7, height = 4
) 
btn_Ad.place(x = 231, y = 198) # Adicionando e ajustando o botão na janela body 

btn_0 = Button(
    frame_body, command = lambda: Entrada_valores("0"), 
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE, 
    text = "0", fg = "#ffffff", bg = "#1C1C1C", 
    width = 20, height = 4
)  
btn_0.place(x = 5, y = 270) # Adicionando e ajustando o botão na janela body

btn_virg = Button(
    frame_body, command = lambda: Entrada_valores(","), 
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE, 
    text = ",", fg = "#ffffff", bg = "#1C1C1C", 
    width = 9, height = 4
)  
btn_virg.place(x = 156, y = 270) # Adicionando e ajustando o botão na janela body

btn_Igual = Button(
    frame_body, command = Calcular,
    font = ("Ivy 8 bold"), 
    relief = RAISED, overrelief = RIDGE, 
    text = "=", fg = "#000", bg = "#00ff00", 
    width = 7, height = 4
)  
btn_Igual.place(x = 231, y = 270) # Adicionando e ajustando o botão na janela body 
    

win.mainloop()  # Iniciando o loop principal
