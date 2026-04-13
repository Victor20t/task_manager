import random

listaDeTarefas = []

def receber_tarefa():
    rodar = True

    while rodar: 
        tarefa = input("Tarefa: ")
        if not tarefa.strip():
            print("Digite algo válido!")
            continue
        
        return tarefa


def adicionar_tarefa(): 
    id = random.choice(range(10000, 19999))
    status = False 
    tarefa =  {"id": id, "tarefa":receber_tarefa(), "status": status}
    listaDeTarefas.append(tarefa)


def show_lista(): 
    for i in listaDeTarefas:
        print(f"- {i['id']}: {i['tarefa']} (Status: {'Concluída' if i['status'] else 'Pendente'})")
