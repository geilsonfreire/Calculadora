# Importando as bibliotecas necessárias
from tkinter import *  # Importando a biblioteca Tkinter
from tkinter import ttk  # Importando a biblioteca ttk


# Criando a janela
win = Tk()  # Criando a janela principal
win.title("Calculadora")  # Definindo o título da janela
win.geometry("300x400")  # Definindo o tamanho da janela
win.resizable(False, False) # Definindo que a janela não pode ser redimensionada
win.config(bg="#ffffff")  # Definindo a cor de fundo da janela
win.iconbitmap('assets/icon/cal.ico')

# Criando os frames
frame_display = Frame(
    win,
    width = 290,
    height = 45,
    bg = "#000"
)  # Criando um frame para a tela display

frame_display.place(
    x = 5,
    y = 2
)  # Adicionando o frame na janela display

frame_body = Frame(
    win,
    width = 290,
    height = 340,
    bg = "#000"
)  # Criando um frame para a tela body

frame_body.place(
    x = 5,
    y = 55
)   # Adicionando o frame na janela body 


# Criando a btns de números
btn_c = Button(
    frame_body,
    text = "C",
    fg = "#ffffff",
    bg = "#b54a07",
    width = 15,
    height = 2
)  # Criando o botão de limpar
btn_c.place(
    x = 5,
    y = 5
)  # Adicionando o botão na janela

btn_porc = Button(
    frame_body,
    text = "%",
    fg = "#ffffff",
    bg = "#036e10",
    width = 10,
    height = 2
)  # Criando o botão de limpar
btn_porc.place(
    x = 123,
    y = 5
)  # Adicionando o botão na janela

btn_div = Button(
    frame_body,
    text = "/",
    fg = "#ffffff",
    bg = "#036e10",
    width = 10,
    height = 2
)  # Criando o botão de limpar
btn_div.place(
    x = 205,
    y = 5
)  # Adicionando o botão na janela




win.mainloop()  # Iniciando o loop principal
