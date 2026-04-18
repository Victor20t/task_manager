import json
import os

CAMINHO_ARQUIVO = "tasks.json"

def salvando_lista(lista: list) -> None:
    try:
        with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(lista, f, ensure_ascii=False, indent=4)
    except OSError as e:
        raise OSError(f"Erro ao salvar tarefas: {e}")

def carregar_lista() -> list:
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []
    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
            conteudo = f.read().strip()
            if not conteudo:
                return []
            dados = json.loads(conteudo)
            if not isinstance(dados, list):
                raise ValueError("Formato inválido: esperado uma lista.")
            return dados
    except json.JSONDecodeError as e:
        raise ValueError(f"Arquivo corrompido: {e}")
    except OSError as e:
        raise OSError(f"Erro ao carregar tarefas: {e}")