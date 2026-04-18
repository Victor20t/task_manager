import random
import storage

listaDeTarefas = storage.carregar_lista()

def gerar_id_unico() -> int:
    ids_existentes = {t["id"] for t in listaDeTarefas}
    while True:
        novo_id = random.randint(10000, 19999)
        if novo_id not in ids_existentes:
            return novo_id


def salvar() -> bool:
    try:
        storage.salvando_lista(listaDeTarefas)
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao salvar: {e}")
        return False


def buscar_tarefa_por_id(id_c: int) -> dict | None:
    return next((t for t in listaDeTarefas if t["id"] == id_c), None)


def pedir_id(operacao: str) -> int | None:
    try:
        return int(input(f"ID da tarefa para {operacao}: ").strip())
    except ValueError:
        print("[ERRO] ID inválido! Digite apenas números.")
        return None

def receber_tarefa() -> str:
    while True:
        tarefa = input("Descrição da tarefa: ").strip()
        if not tarefa:
            print("[AVISO] A descrição não pode ser vazia. Tente novamente.")
            continue
        if len(tarefa) > 200:
            print("[AVISO] Descrição muito longa (máx. 200 caracteres).")
            continue
        return tarefa


def adicionar_tarefa() -> None:
    print("---- ADICIONAR TAREFA ----")
    descricao = receber_tarefa()
    nova_tarefa = {
        "id": gerar_id_unico(),
        "tarefa": descricao,
        "status": False,
    }
    listaDeTarefas.append(nova_tarefa)
    if salvar():
        print(f"Tarefa adicionada com sucesso! (ID: {nova_tarefa['id']})")
    else:
        listaDeTarefas.remove(nova_tarefa)
        print("[ERRO] Tarefa não foi adicionada pois o salvamento falhou.")


def show_lista() -> None:
    print("---- LISTA DE TAREFAS ----")
    if not listaDeTarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    pendentes = [t for t in listaDeTarefas if not t["status"]]
    concluidas = [t for t in listaDeTarefas if t["status"]]

    if pendentes:
        print("\n📋 Pendentes:")
        for t in pendentes:
            print(f"  [{t['id']}] {t['tarefa']}")
    if concluidas:
        print("\n✅ Concluídas:")
        for t in concluidas:
            print(f"  [{t['id']}] {t['tarefa']}")


def remover_tarefa() -> None:
    print("---- REMOVER TAREFA ----")
    id_c = pedir_id("remover")
    if id_c is None:
        return

    tarefa = buscar_tarefa_por_id(id_c)
    if tarefa is None:
        print(f"[AVISO] Nenhuma tarefa encontrada com ID {id_c}.")
        return

    confirmacao = input(f"Confirma remoção de '{tarefa['tarefa']}'? (s/n): ").strip().lower()
    if confirmacao != "s":
        print("Operação cancelada.")
        return

    listaDeTarefas.remove(tarefa)
    if salvar():
        print("Tarefa removida com sucesso!")
    else:
        listaDeTarefas.append(tarefa) 
        print("[ERRO] Não foi possível remover. Tente novamente.")


def concluir_tarefa() -> None:
    print("---- CONCLUIR TAREFA ----")
    id_c = pedir_id("concluir")
    if id_c is None:
        return

    tarefa = buscar_tarefa_por_id(id_c)
    if tarefa is None:
        print(f"[AVISO] Nenhuma tarefa encontrada com ID {id_c}.")
        return

    if tarefa["status"]:
        print("[AVISO] Esta tarefa já está concluída.")
        return

    tarefa["status"] = True
    if salvar():
        print("Tarefa marcada como concluída!")
    else:
        tarefa["status"] = False  
        print("[ERRO] Falha ao salvar. Status não foi alterado.")