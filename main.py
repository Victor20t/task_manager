import task_manager
import time
import sys

def animacao_carregamento():
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for i in range(20):
        print(f"\r  {frames[i % len(frames)]} Carregando tarefas...", end="", flush=True)
        time.sleep(0.05)
    print("\r  ✔ Pronto!                    ")

def limpar_linha():
    print()

def separador(char="─", largura=40):
    print(char * largura)

def cabecalho():
    separador("═")
    print("       ✅  GERENCIADOR DE TAREFAS")
    separador("═")
    print()

def exibir_menu():
    time.sleep(0.2)
    separador()
    print("  1 │ Adicionar tarefa")
    print("  2 │ Exibir lista")
    print("  3 │ Remover tarefa")
    print("  4 │ Concluir tarefa")
    print("  0 │ Sair")
    separador()

def receber_opcao():
    try:
        opcao = int(input("  → Opção: ").strip())
        return opcao
    except ValueError:
        print("  ⚠ Digite um número válido!")
        return -1
    except (EOFError, KeyboardInterrupt):
        return 0

def executar_menu(opcao):
    limpar_linha()
    if opcao == 1:
        task_manager.adicionar_tarefa()
    elif opcao == 2:
        task_manager.show_lista()
    elif opcao == 3:
        task_manager.remover_tarefa()
    elif opcao == 4:
        task_manager.concluir_tarefa()
    elif opcao == 0:
        separador("═")
        print("  Até logo! 👋")
        separador("═")
        time.sleep(0.5)
        return False
    else:
        print("  ⚠ Opção inválida! Escolha entre 0 e 4.")
    return True

def main():
    cabecalho()
    animacao_carregamento()
    limpar_linha()
    task_manager.show_lista()

    rodando = True
    while rodando:
        exibir_menu()
        opcao = receber_opcao()
        rodando = executar_menu(opcao)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Saindo... Até logo! 👋\n")
        sys.exit(0)