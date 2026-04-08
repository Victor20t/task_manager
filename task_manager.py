import random 
import storage
from datetime import datetime

id_lista = list(range(1, 1001))

def adicionar_task():
    dia_task = datetime.now()
    id_task = random.choice(id_lista)
    tarefa = input("Nova tarefa: ")
    concluida = False

    print(dia_task)

    nova_tarefa = { 
        "dia":dia_task,
        "id":id_task,
        "tarefa":tarefa,
        "satatus":concluida
    }

    storage.salvar_tarefa(nova_tarefa)
    
    print("tarefa salva")
