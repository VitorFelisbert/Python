import customtkinter as ctk

janela = ctk.CTk()
janela.title("minha janela")
janela.geometry("400x300")

texto = ctk.CTkLabel(janela, text="Olá! Interface Moderna", font=("Arial", 20))
texto.pack(pady=20)
janela.mainloop()