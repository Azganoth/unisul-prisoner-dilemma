import tkinter as tk
from tkinter.messagebox import askyesno
from xmlrpc.client import ServerProxy

tk.Tk().withdraw()

# Inicializar o servidor do cliente
client = ServerProxy('http://localhost:8000')

# Pedir o testemunho ao prisioneiro
testimony = askyesno('Testemunho', 'Você vai testemunhar?')

print(f'Você escolheu {"" if testimony else "não "}testemunhar, aguarde a decisão do juíz...')

# Enviar o testemunho e aguardar a sentença do juíz
sentence = client.testify(testimony)

# Mostrar a sentença recebida
print(f'Você foi julgado com pena de {sentence}.')
