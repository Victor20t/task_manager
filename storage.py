import json

lista = []

def salvar_tarefa(tarefa):
    lista.append(tarefa)
    with open("tasks.json", "w") as f:
        json.dump(lista, f)

def listar():
    with open("tasks.json", "r") as f:
        tarefas = json.load(f)
        print(tarefas)










