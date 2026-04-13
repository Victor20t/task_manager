import task_manager

print("LISTA DE TAREFAS SUPREMA")

def receber_opcao():
    opcao = int(input("Digite uma opção: "))
    return opcao

def exibir_menu():
    print("Opções: ")
    print("1. Adicionar tarefa")
    print("2. Exibir lista de tarefas")
    print("0. Sair")

def executar_menu(opcao):
    if opcao == 1:
        task_manager.adicionar_tarefa()
    elif opcao == 2:
        task_manager.show_lista()
    elif opcao == 0:
        return False
    else:
        print("Opção inválida!")
    return True

def main():
    rodando = True
    while rodando:    
        exibir_menu()
        opcao = receber_opcao()
        rodando = executar_menu(opcao)

if __name__ == "__main__":
    main()

