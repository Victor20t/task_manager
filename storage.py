import json

def salvando_lista(x):
    with open("tasks.json", "w", encoding='utf-8') as f: 
        json.dump(x, f ,ensure_ascii=False, indent=4)
        print("salvando dados...")

def carregar_lista():
    with open("tasks.json", "r") as ler:
        return json.load(ler)