import tkinter as tk
from tkinter import messagebox


usuarios = {"usuario1": "senha1", "usuario2": "senha2"}


def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario in usuarios and usuarios[usuario] == senha:
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos")


def registrar_usuario():
    usuario = entry_novo_usuario.get()
    senha = entry_nova_senha.get()

    if usuario in usuarios:
        messagebox.showerror("Erro", "Usuário já existe")
    else:
        usuarios[usuario] = senha
        messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
        entry_novo_usuario.delete(0, tk.END)
        entry_nova_senha.delete(0, tk.END)


def mostrar_registro():
    login_frame.pack_forget()
    registro_frame.pack()


def mostrar_login():
    registro_frame.pack_forget()
    login_frame.pack()


root = tk.Tk()
root.title("Sistema de Login e Registro")


login_frame = tk.Frame(root)
login_frame.pack()

label_usuario = tk.Label(login_frame, text="Usuário:")
label_usuario.pack()
entry_usuario = tk.Entry(login_frame)
entry_usuario.pack()

label_senha = tk.Label(login_frame, text="Senha:")
label_senha.pack()
entry_senha = tk.Entry(login_frame, show="*") 
entry_senha.pack()

botao_login = tk.Button(login_frame, text="Login", command=verificar_login)
botao_login.pack()

botao_ir_registro = tk.Button(login_frame, text="Registrar", command=mostrar_registro)
botao_ir_registro.pack()

registro_frame = tk.Frame(root)

label_novo_usuario = tk.Label(registro_frame, text="Novo Usuário:")
label_novo_usuario.pack()
entry_novo_usuario = tk.Entry(registro_frame)
entry_novo_usuario.pack()

label_nova_senha = tk.Label(registro_frame, text="Nova Senha:")
label_nova_senha.pack()
entry_nova_senha = tk.Entry(registro_frame, show="*")  
entry_nova_senha.pack()

botao_registrar = tk.Button(registro_frame, text="Registrar", command=registrar_usuario)
botao_registrar.pack()

botao_ir_login = tk.Button(registro_frame, text="Voltar ao Login", command=mostrar_login)
botao_ir_login.pack()


login_frame.pack()


root.mainloop()
