from fornecedor import Fornecedor
from controle import Controle

while True:
    print('-----Menu-----')
    print('1.Inserir')
    print('2.Excluir')
    print('3.Alterar')
    print('4.Listar')
    print('0.Sair')
    op = int(input('Informe sua opção: '))
    if op == 1:
        print('-----Inserção de Fornecedores-----')
        print('Informe os Dados do Fornecedor: ')
        nome = input('Nome Empresa: ')
        telefone = input('Telefone Empresa: ')
        endereço = input('Endereço: ')
        produtos_fornecidos = input('Produtos Fornecidos: ')

        fornecedor = Fornecedor(nome, telefone, endereço, produtos_fornecidos)
        controle = Controle()
        if controle.insert(fornecedor):
            print('Fornecedor Cadastrado com Sucesso: ')
        else:
            print('Erro no Cadastro do Fornecedor!')

    elif op == 2:
        print('-----Exclusão de Fornecedores-----')
        id = int(input('Informe o ID do Fornecedor que deseja excluir: '))
        controle2 = Controle()
        if controle2.delete(id):
            print('Exclusão realizada com sucesso!')
        else:
            print('Falha na Exclusão')
    elif op == 3:
        print('-----Alteração de Fornecedores-----')
        id = int(input('Informe o ID do Fornecedor que deseja alterar: '))
        nome = input('Nome: ')
        telefone = input('Telefone: ')
        endereco = input('Endereço da Empresa: ')
        produtos_fornecidos = input('Produtos Fornecidos: ')
        fornecedor2 = Fornecedor(nome, telefone, endereco, produtos_fornecidos)
        fornecedor2.set_id(id)
        controle3 = Controle()
        controle3.update(fornecedor2)

    elif op == 4:
        print('-----Listar Produtos-----')
        controle = Controle()
        fornecedor = Fornecedor("","","","")
        fornecedor.set_id("")
        fornecedores = controle.select(fornecedor)
        for fornecedor in fornecedores:
            print(fornecedor[1])
            print(fornecedor[2])
            print(fornecedor[3])
            print(fornecedor[4])
            print('-----------------------------')
    elif op == 0:
        break