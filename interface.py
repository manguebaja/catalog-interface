from tkinter import  *
import sys, os
from pandas import DataFrame
import pandas as pd

# Inicializa o Tkinter, seta o título, o tamanho da tela e desabilita o redimensionamento da tela
root = Tk()
root.title("Catálogo Baja")
root.geometry('500x300')
root.resizable(False, False)

# Criar frame e barra de escrolagem
my_frame = Frame(root)
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

# Permite o sistema procurar pelo path do icone e o seleciona
program_directory = sys.path[0]
root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "icon.png")))

# Atualiza a listbox 
def update(data):
    my_list.delete(0, END) ## Limpa a listbox quando o usuário deleta o que ele previamente postou, permitindo que a lista volte ao padrão 
    for item in data:
        my_list.insert(END, item) ## Adiciona itens da lista à Listbox

# Preenche a entrybox com o item que o usuário clica
def fillout(event):
    my_entry.delete(0, END)
    my_entry.insert(0, my_list.get(ANCHOR))

# Checa o que foi digitado com o que está na lista e mostra ao usuário
def check(event):
    typed = my_entry.get()
    if typed == '':
        data = excelToList
    else:
        data = []
        for item in excelToList:
            if typed.lower() in item.lower():
                data.append(item)
    update(data)


# Criando uma lista que será utilizada no widget Listbox. Esta será feita pela conversão de um arquivo no excel para uma python list 
def excelToList():
    filename = r'teste.xlsx'
    df = pd.read_excel(filename)
    components = []
    components = list(df['A'])
    return components

excelToList = excelToList()

# Criando um label
my_label = Label(root, text="Comece a digitar", font=("Helvetica", 14), fg="grey")
my_label.pack(pady=20)

# Criando uma caixa de input
my_entry = Entry(root, width=53)
my_entry.pack()

# Criando uma listbox (ver documentação)
my_list = Listbox(my_frame, width=50, yscrollcommand=my_scrollbar.set)

# Configurando barra de escrolagem e plottando ela e a listbox na tela
my_scrollbar.config(command=my_list.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_frame.pack(pady=15)
my_list.pack(pady=15)

# Atualiza a lista à listbox 
update(excelToList)

# Cria um keybiding, de modo a toda vez que o usuário clicar em um item da lista este será introduzido na caixa de input
my_list.bind("<<ListboxSelect>>", fillout)

# Cria um keybiding, de modo a toda vez que o usuário pressionar uma tecla uma função será chamada
my_entry.bind("<KeyRelease>", check)

root.mainloop()
