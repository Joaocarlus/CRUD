from cliente import Cliente
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
        print('-----Inserção de Clientes-----')
        print('Informe os Dados do Cliente: ')
        nome = input('Nome: ')
        endereco = input('Endereço: ')
        telefone = input('Telefone: ')
        nascimento = input('Nascimento: ')
        cliente1 = Cliente(nome,endereco, telefone, nascimento)
        controle1 = Controle()
        if controle1.insert(cliente1):
            print('Cliente Cadastrado com Sucesso: ')
        else:
            print('Erro no Cadastro do Cliente!')

    elif op == 2:
        print('-----Exclusão de Cliente-----')
        id = int(input('Informe o ID do Cliente que deseja excluir: '))
        controle2 = Controle()
        if controle2.delete(id):
            print('Exclusão realizada com sucesso!')
        else:
            print('Falha na Exclusão')
    elif op == 3:
        print('-----Alteração de Produto-----')
        id = int(input('Informe o ID do produto que deseja alterar: '))
        nome = input('Nome: ')
        endereco = input('Endereço: ')
        telefone = input('Telefone: ')
        nascimento = input('Data de Nascimento: ')
        cliente1 = Cliente(nome, endereco, telefone, nascimento)
        cliente1.set_id(id)
        controle3 = Controle()  
        controle3.update(cliente1)

    elif op == 4:
        print('-----Listar Produtos-----')
        controle = Controle()
        cliente = Cliente("","","","")
        cliente.set_id("")
        clientes = controle.select(cliente)
        for cliente in clientes:
            print(cliente[1])
            print(cliente[2])
            print(cliente[3])
            print(cliente[4])
            print('-----------------------------')
    elif op == 0:
        break