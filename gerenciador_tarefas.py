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
    
    if encontra_tarefa(tarefa) == True:
        raise ValueError('Tarefa já existe')
    else:
        lista_de_tarefas.append(nova_tarefa)


            


def remove_tarefas(índices: tuple[int]):

    if len(índices) > len(lista_de_tarefas) - 1:
        raise ValueError('indice fora da lista')
    else:
        if len(lista_de_tarefas) > 0:
            for indice in índices:
                lista_de_tarefas.remove(lista_de_tarefas[indice])
        else: 
            raise ValueError('tarefa não encontrada')
    # TODO: coloque o código aqui para remover um tarefa na lista
    # Caso a tarefa não exista na lista, levante uma exceção do tipo ValueError
    # com a mensagem "Tarefa não existe"


def encontra_tarefa(dicionario: str) -> int:

    for tarefa in lista_de_tarefas:
        if tarefa["tarefa"] == dicionario:
            return True
    return False    


def ordena_por_prioridade():
    """
    Ordena a lista de tarefas por prioridade com as tarefas prioritárias no
    início da lista, seguidas pelas tarefas não prioritárias.
    As tarefas prioritárias devem ser ordenadas por ordem alfabética e as
    tarefas não prioritárias devem ser ordenadas por ordem alfabética.
    """
    # TODO: coloque o código aqui para ordenar a lista de tarefas por prioridade
    # com as tarefas prioritárias no início da lista, seguidas pelas tarefas
    # não prioritárias.
    # As tarefas prioritárias devem ser ordenadas por ordem alfabética e as
    # tarefas não prioritárias devem ser ordenadas por ordem alfabética.
    raise NotImplementedError("Ordenar tarefas não implementado")


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
