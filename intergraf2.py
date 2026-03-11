'''import customtkinter as ctk

def clicar():
    print("Botão clicado!")

janela = ctk.CTk()
janela.geometry("400x300")

botao = ctk.CTkButton(janela, text="Clique aqui", command=clicar, width=200, height=40)

botao.pack(pady=50)
janela.mainloop()'''

#ex5.1
'''
import customtkinter as ctk

def saudar():
    resposta = "Olá, seja bem vindo ao Phyton"

janela = ctk.CTk
janela.geometry("400x300")

botao = ctk.CTkbutton(janela, text="Fechar", command=clicar , width=200, height=40 )

botao.pack(pady=50)
janela.mainloop()'''

#ex5.2

import customtkinter as ctk
def calcularIMC():
    altura = float(entrada1.get()) 
    peso = float(entrada2.get())
    imc = peso/(altura**2)
    resposta = "IMC = "+str(imc)
    saida.configure(text=resposta)

#janelas
janela=ctk.CTk()
janela.title("Calcular IMC")
janela.geometry("400x300")


#inputs
entrada1 = ctk.CTkEntry(janela, placeholder_text='Altura', width= 200, height=40,)
entrada1.pack(pady=20)

entrada2 = ctk.CTkEntry(janela, placeholder_text='Peso', width=200, height=40)
entrada2.pack(pady=20)


#botao
botao = ctk.CTkButton(janela, text="Calcular", command=calcularIMC, width=200, height=40)
botao.pack(pady=20)

saida = ctk.CTkLabel(janela, text="", font=("Arial",20))
saida.pack(pady=20)
#Label
#ValorIMC

janela.mainloop()