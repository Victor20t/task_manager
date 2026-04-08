import random 
import storage
from datetime import datetime

id_lista = list(range(1, 1001))

def adicionar_task():
    dia_task = datetime.now().isoformat()
    id_task = random.choice(id_lista)
    tarefa = input("Nova tarefa: ")
    concluida = False

    print(dia_task)

    tarefa = { 
        "dia":dia_task,
        "id":id_task,
        "tarefa":tarefa,
        "satatus":concluida
        }


    storage.salvar_tarefa(tarefa)

    print("tarefa salva")

