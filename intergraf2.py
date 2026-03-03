import customtkinter as ctk

def clicar():
    print("Botão clicado!")

janela = ctk.CTk()
janela.geometry("400x300")

botao = ctk.CTkButton(janela, text="Clique aqui", command=clicar, width=200, heigth=40)

botao.pack(pady=50)
janela.mainloop()