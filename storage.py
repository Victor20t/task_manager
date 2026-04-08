import json

lista_tarefas = []

def salvar_tarefa(tarefa):
    lista_tarefas.append(tarefa)
    print(lista_tarefas)


def salvar_json():
    with open("tasks.json", 'a') as f: 
        json.dump(lista_tarefas, f)

def ler_json():
  with open('tasks.json', 'r') as arquivo:
    conteudo = json.load(arquivo)
    print(conteudo)
