
def adicionar_tarefas(tarefas):
    titulo = input('Digite o nome da tarefa: ').strip()

    tarefa = {
        "titulo": titulo,
        "status": False
    }

    tarefas.append(tarefa)

    print('Tarefa adicionada com sucesso!')
tarefas =[]



def listar_tarefas(tarefas):
    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
        return
    else:
        for indice, tarefa in enumerate(tarefas,    start=1):
            if tarefa['status']:
                simbolo = '✔'
            else:
                simbolo = '❌'
            
            print(f'{indice} - {tarefa["titulo"]} [{simbolo}]')
          


def concluir_tarefas(tarefas):
    if not tarefas:
        print('Nenhuma tarefa pra concluir')
        return
    else:
        listar_tarefas(tarefas)
        try:    
            num_tarefa= int(input('Digite o numero da tarefa! '))
        except ValueError:
         print('Digite um número válido!')
         return
        indice_real = num_tarefa -1
        if indice_real >= 0 and indice_real < len(tarefas):
            tarefas[indice_real]['status'] = True
            print('Tarefa concluida com sucesso!')
        else: 
            print('Número de tarefa inválido!')
        


def remover_tarefas(tarefas):
    if not tarefas:
        print('Nenhuma tarefa pra remover!')
        return
    else:
        listar_tarefas(tarefas)
        try:
            num_tarefa = int(input('Digite o número da tarefa que quer remover: '))
        except ValueError:
            print('Digite um número válido!')
            return
        indice_real = num_tarefa - 1
        if indice_real >= 0 and indice_real < len(tarefas):
            tarefas.pop(indice_real)
            print('Tarefa removida com sucesso!')
        else:
            print('Número de tarefa inválido!')




while True:
    print('\n ===== TO-DO LIST ======')
    print('1 - Adicionar Tarefa')
    print('2 - Listar tarefas')
    print('3 - Concluir Tarefa')
    print('4 - Remover Tarefa')
    print('5 - Sair')

    opcao =  input('Escolha uma opção: ').strip()

    if opcao == '1': 
        adicionar_tarefas(tarefas)

    elif opcao == '2':
        listar_tarefas(tarefas)

    elif opcao == '3':
        concluir_tarefas(tarefas)

    elif opcao == '4':
        remover_tarefas(tarefas)

    elif opcao == '5':
        print('Programa encerrado.')
        break

    else:
        print('Opção inválida!')