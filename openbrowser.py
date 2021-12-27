import webbrowser  # Importa biblioteca
from tkinter import * # Importa biblioteca

root = Tk( )  # Representa o Tkinter e sem nome do sistema

root.title('Abrir Browser')  # Título
root.geometry('300x200')  # Tamanho da tela gráfica


# Função que abre o navegador na página do google
def google():
    webbrowser.open('www.google.com')


# Chama a função
mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)


# Executa root
root.mainloop()