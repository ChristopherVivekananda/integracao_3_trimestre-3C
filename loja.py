import random

print("Bem-vindo à Loja de Instrumentos Musicais")

# Base de dados de produtos
produtos = [
    # Guitarras
    {"id": 1, "nome": "Fender Stratocaster American Professional", "categoria": "Guitarra", "marca": "Fender", "preco": 8999.99, "estoque": 5},
    {"id": 2, "nome": "Gibson Les Paul Standard 50s", "categoria": "Guitarra", "marca": "Gibson", "preco": 12999.99, "estoque": 3},
    {"id": 3, "nome": "Ibanez RG550 Genesis", "categoria": "Guitarra", "marca": "Ibanez", "preco": 4599.99, "estoque": 8},
    {"id": 4, "nome": "PRS Custom 24", "categoria": "Guitarra", "marca": "PRS", "preco": 14999.99, "estoque": 2},
    {"id": 5, "nome": "Music Man John Petrucci Majesty", "categoria": "Guitarra", "marca": "Music Man", "preco": 15999.99, "estoque": 1},
    {"id": 6, "nome": "Dean ML X", "categoria": "Guitarra", "marca": "Dean", "preco": 2999.99, "estoque": 6},
    {"id": 7, "nome": "Epiphone Les Paul Standard", "categoria": "Guitarra", "marca": "Epiphone", "preco": 2599.99, "estoque": 12},
    {"id": 8, "nome": "Jackson Soloist", "categoria": "Guitarra", "marca": "Jackson", "preco": 6899.99, "estoque": 4},
    
    # Baixos
    {"id": 9, "nome": "Fender Precision Bass American", "categoria": "Baixo", "marca": "Fender", "preco": 7999.99, "estoque": 6},
    {"id": 10, "nome": "Music Man StingRay Special", "categoria": "Baixo", "marca": "Music Man", "preco": 10999.99, "estoque": 2},
    {"id": 11, "nome": "Ibanez SR500", "categoria": "Baixo", "marca": "Ibanez", "preco": 3899.99, "estoque": 10},
    {"id": 12, "nome": "Fender Jazz Bass American", "categoria": "Baixo", "marca": "Fender", "preco": 8299.99, "estoque": 5},
    {"id": 13, "nome": "Gibson Thunderbird", "categoria": "Baixo", "marca": "Gibson", "preco": 8999.99, "estoque": 3},
    {"id": 14, "nome": "Dean Edge", "categoria": "Baixo", "marca": "Dean", "preco": 1899.99, "estoque": 8},
    
    # Amplificadores
    {"id": 15, "nome": "Fender Twin Reverb", "categoria": "Amplificador", "marca": "Fender", "preco": 6999.99, "estoque": 4},
    {"id": 16, "nome": "Marshall JCM800", "categoria": "Amplificador", "marca": "Marshall", "preco": 8999.99, "estoque": 3},
    {"id": 17, "nome": "Orange Rockerverb 50", "categoria": "Amplificador", "marca": "Orange", "preco": 11999.99, "estoque": 2},
    {"id": 18, "nome": "Boss Katana 100", "categoria": "Amplificador", "marca": "Boss", "preco": 2599.99, "estoque": 7},
    {"id": 19, "nome": "Ampeg SVT Classic", "categoria": "Amplificador", "marca": "Ampeg", "preco": 12999.99, "estoque": 2},
    {"id": 20, "nome": "Mesa Boogie Dual Rectifier", "categoria": "Amplificador", "marca": "Mesa Boogie", "preco": 14999.99, "estoque": 1}
]

carrinho = []

def exibir_produtos(lista_produtos):
    if not lista_produtos:
        print("Nenhum produto encontrado!")
        return
        
    print("\nLISTA DE PRODUTOS")
    print("ID | NOME | CATEGORIA | MARCA | PREÇO | ESTOQUE")
    print("-" * 80)
    for produto in lista_produtos:
        print(f"{produto['id']:2} | {produto['nome']:35} | {produto['categoria']:11} | {produto['marca']:12} | R${produto['preco']:8.2f} | {produto['estoque']:3}")

def filtrar_por_categoria():
    categorias = list(set([produto['categoria'] for produto in produtos]))
    print("\nCategorias disponíveis:")
    for i, categoria in enumerate(categorias, 1):
        print(f"({i}) {categoria}")
    
    try:
        escolha = int(input("Escolha uma categoria pelo número: ")) - 1
        if 0 <= escolha < len(categorias):
            categoria_escolhida = categorias[escolha]
            produtos_filtrados = [p for p in produtos if p['categoria'] == categoria_escolhida]
            return produtos_filtrados
        else:
            print("Opção inválida!")
            return produtos
    except ValueError:
        print("Digite um número válido!")
        return produtos

def filtrar_por_marca():
    marcas = list(set([produto['marca'] for produto in produtos]))
    print("\nMarcas disponíveis:")
    for i, marca in enumerate(marcas, 1):
        print(f"({i}) {marca}")
    
    try:
        escolha = int(input("Escolha uma marca pelo número: ")) - 1
        if 0 <= escolha < len(marcas):
            marca_escolhida = marcas[escolha]
            produtos_filtrados = [p for p in produtos if p['marca'] == marca_escolhida]
            return produtos_filtrados
        else:
            print("Opção inválida!")
            return produtos
    except ValueError:
        print("Digite um número válido!")
        return produtos

def buscar_por_nome():
    termo = input("Digite o nome do produto que deseja buscar: ").lower()
    produtos_encontrados = [p for p in produtos if termo in p['nome'].lower()]
    return produtos_encontrados

def filtrar_por_preco():
    print("\nFiltrar por preço:")
    print("(1) Até R$ 3.000,00")
    print("(2) R$ 3.000,00 - R$ 6.000,00")
    print("(3) R$ 6.000,00 - R$ 10.000,00")
    print("(4) Acima de R$ 10.000,00")
    
    try:
        opcao = int(input("Escolha uma faixa de preço: "))
        
        if opcao == 1:
            return [p for p in produtos if p['preco'] <= 3000]
        elif opcao == 2:
            return [p for p in produtos if 3000 < p['preco'] <= 6000]
        elif opcao == 3:
            return [p for p in produtos if 6000 < p['preco'] <= 10000]
        elif opcao == 4:
            return [p for p in produtos if p['preco'] > 10000]
        else:
            print("Opção inválida!")
            return produtos
    except ValueError:
        print("Digite um número válido!")
        return produtos

def adicionar_ao_carrinho():
    exibir_produtos(produtos)
    try:
        id_produto = int(input("Digite o ID do produto que deseja adicionar ao carrinho: "))
        produto = next((p for p in produtos if p['id'] == id_produto), None)
        
        if produto:
            if produto['estoque'] > 0:
                quantidade = int(input(f"Quantidade de '{produto['nome']}' (estoque: {produto['estoque']}): "))
                
                if quantidade <= produto['estoque']:
                    item_existente = next((item for item in carrinho if item['id'] == id_produto), None)
                    
                    if item_existente:
                        item_existente['quantidade'] += quantidade
                    else:
                        item_carrinho = {
                            'id': produto['id'],
                            'nome': produto['nome'],
                            'preco': produto['preco'],
                            'quantidade': quantidade
                        }
                        carrinho.append(item_carrinho)
                    
                    produto['estoque'] -= quantidade
                    print(f"{quantidade}x {produto['nome']} adicionado(s) ao carrinho!")
                else:
                    print("Quantidade indisponível em estoque!")
            else:
                print("Produto esgotado!")
        else:
            print("Produto não encontrado!")
    except ValueError:
        print("Digite um ID válido!")

def ver_carrinho():
    if not carrinho:
        print("Seu carrinho está vazio!")
        return
    
    print("\nSEU CARRINHO DE COMPRAS")
    total = 0
    for item in carrinho:
        subtotal = item['preco'] * item['quantidade']
        total += subtotal
        print(f"{item['quantidade']}x {item['nome']} - R${item['preco']:.2f} cada = R${subtotal:.2f}")
    print(f"TOTAL: R${total:.2f}")

def remover_do_carrinho():
    if not carrinho:
        print("Seu carrinho está vazio!")
        return
    
    ver_carrinho()
    try:
        id_produto = int(input("Digite o ID do produto que deseja remover: "))
        
        item_carrinho = next((item for item in carrinho if item['id'] == id_produto), None)
        produto_estoque = next((p for p in produtos if p['id'] == id_produto), None)
        
        if item_carrinho and produto_estoque:
            quantidade_remover = int(input(f"Quantidade a remover (atual: {item_carrinho['quantidade']}): "))
            
            if quantidade_remover <= item_carrinho['quantidade']:
                produto_estoque['estoque'] += quantidade_remover
                item_carrinho['quantidade'] -= quantidade_remover
                
                if item_carrinho['quantidade'] <= 0:
                    carrinho.remove(item_carrinho)
                    print("Produto removido do carrinho!")
                else:
                    print(f"Quantidade reduzida para {item_carrinho['quantidade']}!")
            else:
                print("Quantidade inválida!")
        else:
            print("Produto não encontrado no carrinho!")
    except ValueError:
        print("Digite um valor válido!")

def finalizar_compra():
    if not carrinho:
        print("Seu carrinho está vazio!")
        return
    
    ver_carrinho()
    confirmacao = input("Deseja finalizar a compra? (S/N): ").lower()
    
    if confirmacao == 's':
        print("COMPRA FINALIZADA COM SUCESSO!")
        print("Obrigado pela preferência!")
        carrinho.clear()
    else:
        print("Compra cancelada.")

def menu_loja():
    produtos_exibidos = produtos.copy()
    
    while True:
        print("\nMENU PRINCIPAL - LOJA DE INSTRUMENTOS")
        print("(1) Ver todos os produtos")
        print("(2) Filtrar por categoria")
        print("(3) Filtrar por marca")
        print("(4) Buscar por nome")
        print("(5) Filtrar por preço")
        print("(6) Adicionar ao carrinho")
        print("(7) Ver carrinho")
        print("(8) Remover do carrinho")
        print("(9) Finalizar compra")
        print("(0) Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            produtos_exibidos = produtos.copy()
            exibir_produtos(produtos_exibidos)
        
        elif opcao == "2":
            produtos_exibidos = filtrar_por_categoria()
            exibir_produtos(produtos_exibidos)
        
        elif opcao == "3":
            produtos_exibidos = filtrar_por_marca()
            exibir_produtos(produtos_exibidos)
        
        elif opcao == "4":
            produtos_exibidos = buscar_por_nome()
            if produtos_exibidos:
                exibir_produtos(produtos_exibidos)
            else:
                print("Nenhum produto encontrado!")
        
        elif opcao == "5":
            produtos_exibidos = filtrar_por_preco()
            exibir_produtos(produtos_exibidos)
        
        elif opcao == "6":
            adicionar_ao_carrinho()
        
        elif opcao == "7":
            ver_carrinho()
        
        elif opcao == "8":
            remover_do_carrinho()
        
        elif opcao == "9":
            finalizar_compra()
        
        elif opcao == "0":
            print("Obrigado por visitar nossa loja!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_loja()