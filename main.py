import task_manager 
import storage


print("\nTask Manager ")

def exibir_menu():
    print("1 - adiconar tarefa")
    print("2 - listar tarrefas")
    print("3 - concluir tarefa ")
    print("4 - remover tarefa")
    print("0 - sair ")

def receber_opcao():
    opcao = int(input("digite a opção: "))
    return opcao 

def executar_menu(opcao):
        if opcao == 1: 
            print("Executando adicionar_task")
            task_manager.adicionar_task()
        elif opcao == 2: 
            print("Executando listar tarefas")
            storage.listar()
        elif opcao ==3:
            print("Executado")
        elif opcao == 4:
            print("executado")
        elif opcao == 0:
            return False
        return True
            

def main():
    rodando = True
    while rodando:    
        exibir_menu()
        opcao = receber_opcao()
        rodando = executar_menu(opcao)

if __name__ == "__main__":
    main()

