"""
Modulo que implementa um gerenciador de tarefas
"""


lista_de_tarefas: list[dict[str]] = [
    {"prioridade": True, "tarefa": "Estudar Python"},
    {"prioridade": False, "tarefa": "Tomar banho"},
    {"prioridade": False, "tarefa": "Assistir série"},
]


def adicionar_tarefa(prioridade: bool, tarefa: str):
    
    nova_tarefa = {"prioridade": prioridade, "tarefa": tarefa}


    # isinstanceof(prioridade, bool)
    if prioridade is not True and prioridade is not False:
        raise ValueError('Prioridade inválida')
    
    if encontra_tarefa(tarefa) is True:
        raise ValueError('Tarefa já existe')
    else:
        lista_de_tarefas.append(nova_tarefa)


            


def remove_tarefas(índices: tuple[int]):

    if len(índices) > len(lista_de_tarefas) - 1:
        raise ValueError('indice fora da lista')
    else:
        if len(lista_de_tarefas) > 0:
            for i in range(len(índices)-1, -1, -1):
                lista_de_tarefas.pop(índices[i])
        else: 
            raise ValueError('tarefa não encontrada')
    


def encontra_tarefa(dicionario: str) -> int:

    for tarefa in lista_de_tarefas:
        if tarefa["tarefa"] == dicionario:
            return True
    return False    


def ordena_por_prioridade():
    com_prioridade = []
    sem_prioridade = []
    global lista_de_tarefas
    for i in lista_de_tarefas:
        if i['prioridade'] == 0:
            sem_prioridade.append(i)
        else:
            com_prioridade.append(i)
    com_prioridade = sorted(com_prioridade, key=lambda d: d['tarefa']) 
    sem_prioridade = sorted(sem_prioridade, key=lambda d: d['tarefa']) 
    lista_de_tarefas = []
    for i in com_prioridade:
        lista_de_tarefas.append(i)
    for i in sem_prioridade:
        lista_de_tarefas.append(i)

def get_lista_de_tarefas():
    """
    Retorna somente o texto das tarefas da lista de tarefas
    """
    texts = []
    for tarefa in lista_de_tarefas:
        texto = tarefa["tarefa"]
        prioridade = tarefa["prioridade"]
        texts.append(f"{'*' if prioridade else ''} {texto}")
    return tuple(texts)
