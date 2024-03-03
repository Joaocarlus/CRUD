from produto import Produto
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
        print('-----Inserção de Produtos-----')
        print('Informe os Dados do Produto: ')
        nome = input('Nome: ')
        preco = float(input('Preço: '))
        descricao = input('Descrição: ')
        quantidade_estoque = int(input('Quantidade em Estoque: '))
        categoria = input('Categoria: ')
        fornecedor = input('Fornecedor: ')
        produto1 = Produto(nome, preco, descricao, quantidade_estoque, categoria, fornecedor)
        controle1 = Controle()
        if controle1.insert(produto1):
            print('Produto Cadastrado com Sucesso: ')
        else:
            print('Erro no Cadastro do Produto!')

    elif op == 2:
        print('-----Exclusão de Produtos-----')
        id = int(input('Informe o ID do produto que deseja excluir: '))
        controle2 = Controle()
        if controle2.delete(id):
            print('Exclusão realizada com sucesso!')
        else:
            print('Falha na Exclusão')
    elif op == 3:
        print('-----Alteração de Produto-----')
        id = int(input('Informe o ID do produto que deseja alterar: '))
        nome = input('Nome: ')
        preco = float(input('Preço: '))
        descricao = input('Descrição: ')
        quantidade_estoque = int(input('Quantidade em Estoque: '))
        categoria = input('Categoria: ')
        fornecedor = input('Fornecedor: ')
        produto = Produto(nome, preco, descricao, quantidade_estoque, categoria, fornecedor)
        produto.set_id(id)
        controle3 = Controle()
        controle3.update(produto)
    elif op == 4:
        print('-----Listar Produtos-----')
        controle = Controle()
        produto = Produto("","","","","","")
        produto.set_id("")
        produtos = controle.select(produto)
        for produto in produtos:
            print(produto[1])
            print(produto[2])
            print(produto[3])
            print(produto[4])
            print('-----------------------------')
    elif op == 0:
        break