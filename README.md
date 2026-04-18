# task_manager

# ✅ Gerenciador de Tarefas CLI

Um gerenciador de tarefas simples e funcional rodando direto no terminal, com persistência de dados em JSON.

---

## 📁 Estrutura do Projeto

```
.
├── main.py           # Ponto de entrada — interface CLI e loop principal
├── task_manager.py   # Lógica das operações (adicionar, remover, concluir, listar)
├── storage.py        # Persistência de dados em JSON
└── tasks.json        # Arquivo gerado automaticamente ao adicionar tarefas
```

---

## ▶️ Como usar

**Pré-requisito:** Python 3.10 ou superior.

```bash
python main.py
```

Nenhuma dependência externa é necessária — o projeto usa apenas bibliotecas padrão do Python (`json`, `os`, `random`, `time`, `sys`).

---

## 🧭 Menu de opções

```
  1 │ Adicionar tarefa
  2 │ Exibir lista
  3 │ Remover tarefa
  4 │ Concluir tarefa
  0 │ Sair
```

---

## ⚙️ Funcionalidades

- **Adicionar tarefa** — Cadastra uma nova tarefa com ID único gerado automaticamente e status inicial *Pendente*.
- **Exibir lista** — Mostra as tarefas separadas por *Pendentes* e *Concluídas*.
- **Remover tarefa** — Remove uma tarefa pelo ID, com confirmação antes de apagar.
- **Concluir tarefa** — Marca uma tarefa como concluída pelo ID. Avisa caso já esteja concluída.
- **Persistência automática** — Toda alteração é salva imediatamente no arquivo `tasks.json`.

---

## 🛡️ Tratamento de erros

| Situação | Comportamento |
|---|---|
| Entrada inválida (não numérica) | Aviso e nova tentativa |
| ID não encontrado | Mensagem de aviso |
| Tarefa já concluída | Aviso sem sobrescrever |
| Falha ao salvar no disco | Operação revertida em memória |
| Arquivo `tasks.json` ausente | Lista iniciada vazia automaticamente |
| Arquivo `tasks.json` corrompido | Exceção descritiva é lançada |
| `Ctrl+C` durante execução | Saída limpa sem traceback |

---

## 📄 Formato do `tasks.json`

```json
[
    {
        "id": 14823,
        "tarefa": "Estudar Python",
        "status": false
    },
    {
        "id": 11047,
        "tarefa": "Fazer compras",
        "status": true
    }
]
```

---

## 🗂️ Módulos

### `main.py`
Responsável pela interface com o usuário: animação de carregamento, exibição do menu, leitura de opções e loop principal. Captura `KeyboardInterrupt` globalmente para saída limpa.

### `task_manager.py`
Contém as funções `adicionar_tarefa`, `show_lista`, `remover_tarefa` e `concluir_tarefa`. Garante integridade dos dados revertendo operações em memória caso o salvamento falhe.

### `storage.py`
Responsável exclusivamente por ler e escrever o arquivo `tasks.json`. Valida o conteúdo do arquivo na leitura e lança exceções descritivas em caso de falha.