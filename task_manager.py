import random
import storage

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
    storage.salvando_lista(listaDeTarefas)


def show_lista(): 
    listaDeTarefas  = storage.carregar_lista()
    for i in listaDeTarefas:
        print(f"- {i['id']}: {i['tarefa']} (Status: {'Concluída' if i['status'] else 'Pendente'})")


def remover_tarefa():
    print("----REMOVER TAREFA----")
    id_con = int(input("digite aqui o id da tarefa: "))

    remover = True 

    while remover: 
        listaDeTarefas.pop(id_con)
        remover = input("deseja continua? ")
        if remover.lower() != "sim":
            remover = False
    storage.salvando_lista(listaDeTarefas)
        
def concluir_tarefa():
    print("----CONCLUIR TAREFA----")
    id_c = int(input("digite o id da tarefa: "))

    for i in listaDeTarefas:
        if i["id"] == id_c:
            i["status"] = True
            print("Tarefa marcada como concluída!")
            return
    print("Tarefa não encontrada!") 
    storage.salvando_lista(listaDeTarefas)