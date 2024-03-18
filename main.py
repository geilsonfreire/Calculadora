# Importando as bibliotecas necessárias
from tkinter import *  # Importando a biblioteca Tkinter
from tkinter import ttk  # Importando a biblioteca ttk

# Criando a janela
win = Tk()  # Criando a janela principal
win.title("Calculadora")  # Definindo o título da janela
win.geometry("305x400")  # Definindo o tamanho da janela
win.resizable(False, False) # Definindo que a janela não pode ser redimensionada
win.config(bg="#ffffff")  # Definindo a cor de fundo da janela
win.iconbitmap('assets/icon/cal.ico')

# Criando os frames display
frame_display = Frame(win, width = 295, height = 45, bg = "#000")  # Criando um frame para a tela display
frame_display.place(x = 5, y = 2)  # Adicionando o frame na janela display

# Criando o frame body
frame_body = Frame(win, width = 295, height = 340, bg = "#000")  # Criando um frame para a tela body
frame_body.place(x = 5, y = 55)   # Adicionando o frame na janela body 


# Criando label da tela display
app_display = Label(frame_display, width = 16, text = "0", font = ("Ivy 20 bold"), bg = "#000", fg = "#ffffff", justify = RIGHT, padx = 7, relief = FLAT, anchor = "e")  # Criando a label da tela display
app_display.place(x = 5, y = 5)  # Adicionando a label na janela display

# Criando a btns de números
btn_c = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE,  text = "C", fg = "#ffffff", bg = "#8b008b", width = 13, height = 3)  # Criando o botão de limpar
btn_c.place(x = 5, y = 5)  

btn_x = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "< X", fg = "#ffffff", bg = "#8b008b", width = 7, height = 3)  # Criando o botão de limpar
btn_x.place(x = 109, y = 5)  

btn_porc = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "%", fg = "#000", bg = "#00ff00", width = 7, height = 3)  # Criando o botão de limpar
btn_porc.place(x = 170, y = 5) 

btn_div = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "/", fg = "#000", bg = "#00ff00", width = 7, height = 3)  # Criando o botão de limpar
btn_div.place(x = 231, y = 5)

btn_7 = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "7", fg = "#ffffff", bg = "#1C1C1C", width = 9, height = 4)  # Criando o botão de limpar
btn_7.place(x = 5, y = 63)  
btn_8 = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "8", fg = "#ffffff", bg = "#1C1C1C", width = 9, height = 4)  # Criando o botão de limpar
btn_8.place(x = 80, y = 63)  
btn_9 = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "9", fg = "#ffffff", bg = "#1C1C1C", width = 9, height = 4)  # Criando o botão de limpar
btn_9.place(x = 156, y = 63)  
btn_Ast = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "*", fg = "#000", bg = "#00ff00", width = 7, height = 4)  # Criando o botão de limpar
btn_Ast.place(x = 231, y = 63)  

btn_4 = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "4", fg = "#ffffff", bg = "#1C1C1C", width = 9, height = 4)  # Criando o botão de limpar
btn_4.place(x = 5, y = 131)  
btn_5 = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "5", fg = "#ffffff", bg = "#1C1C1C", width = 9, height = 4)  # Criando o botão de limpar
btn_5.place(x = 80, y = 131)  
btn_6 = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "6", fg = "#ffffff", bg = "#1C1C1C", width = 9, height = 4)  # Criando o botão de limpar
btn_6.place(x = 156, y = 131)  
btn_sub = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "-", fg = "#000", bg = "#00ff00", width = 7, height = 4)  # Criando o botão de limpar
btn_sub.place(x = 231, y = 131)  

btn_3 = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "3", fg = "#ffffff", bg = "#1C1C1C", width = 9, height = 4)  # Criando o botão de limpar
btn_3.place(x = 5, y = 198)  
btn_2 = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "2", fg = "#ffffff", bg = "#1C1C1C", width = 9, height = 4)  # Criando o botão de limpar
btn_2.place(x = 80, y = 198)  
btn_1 = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "1", fg = "#ffffff", bg = "#1C1C1C", width = 9, height = 4)  # Criando o botão de limpar
btn_1.place(x = 156, y = 198)  
btn_Ad = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "+", fg = "#000", bg = "#00ff00", width = 7, height = 4)  # Criando o botão de limpar
btn_Ad.place(x = 231, y = 198) 

btn_0 = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "0", fg = "#ffffff", bg = "#1C1C1C", width = 20, height = 4)  # Criando o botão de limpar
btn_0.place(x = 5, y = 270)  
btn_virg = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = ",", fg = "#ffffff", bg = "#1C1C1C", width = 9, height = 4)  # Criando o botão de limpar
btn_virg.place(x = 156, y = 270)   
btn_Igual = Button(frame_body, font = ("Ivy 8 bold"), relief = RAISED, overrelief = RIDGE, text = "=", fg = "#000", bg = "#00ff00", width = 7, height = 4)  # Criando o botão de limpar
btn_Igual.place(x = 231, y = 270) 


win.mainloop()  # Iniciando o loop principal
