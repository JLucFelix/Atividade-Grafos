def criar_grafo():
    matriz = []
    vertices = []
    return (matriz, vertices)

def inserir_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)

        for linha in matriz:
            linha.append(0)

        tamanho_atualizado = len(vertices)
        nova_linha = [0] * tamanho_atualizado
        matriz.append(nova_linha)

        print(f"Vértice '{vertice}' inserido.")

    else:
        print(f"Vértice '{vertice}' já existe.")

def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)
        
    i = vertices.index(origem)
    j = vertices.index(destino)

    if matriz[i][j] == 0:
        matriz[i][j] = 1
        print(f"Aresta {origem} -> {destino} inserida.")
    else:
        print(f"Aresta {origem} -> {destino} já existe.") 

    if nao_direcionado:
        if matriz[j][i] == 0: 
            matriz[j][i] = 1
            print(f"Aresta {destino} -> {origem} (não-direcionada) inserida.")

def remover_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        i = vertices.index(vertice)
    
        del matriz[i]
    
        for linha in matriz:
            del linha[i]
        
        del vertices[i]

        print(f"Vértice '{vertice}' removido.")
    
    else:
        print(f"Vértice '{vertice}' não encontrado.")

def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem in vertices and destino in vertices:

        i = vertices.index(origem)
        j = vertices.index(destino)

        if matriz[i][j] == 1:
            matriz[i][j] = 0
            print(f"Aresta {origem} -> {destino} removida.")
        else:
            print(f"Aresta {origem} -> {destino} não existia.")

        if nao_direcionado:
            if matriz[j][i] == 1: 
                matriz[j][i] = 0
                print(f"Aresta {destino} -> {origem} (não-direcionada) removida.")
                
    else:
        print(f"Erro: Vértice '{origem}' ou '{destino}' não encontrado.")

def existe_aresta(matriz, vertices, origem, destino):
    if origem not in vertices or destino not in vertices:
        return False

    i = vertices.index(origem)
    j = vertices.index(destino)

    return matriz[i][j] == 1

def vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"Vértice '{vertice}' não encontrado.")
        return []

    i = vertices.index(vertice)

    lista_de_vizinhos = []

    for j, valor in enumerate(matriz[i]):
        if valor == 1:
            lista_de_vizinhos.append(vertices[j])

    return lista_de_vizinhos

def grau_vertices(matriz, vertices, nao_direcionado=False):
    graus = {}

    for i in range(len(vertices)):
        nome_vertice = vertices[i]
        linha_matriz = matriz[i]

        if nao_direcionado:
            graus[nome_vertice] = sum(linha_matriz)
        
        else:
            grau_saida = sum(linha_matriz)
            
            grau_entrada = 0
            for linha in matriz:
                grau_entrada = grau_entrada + linha[i]
            
            grau_total = grau_saida + grau_entrada

            graus[nome_vertice] = {"saida": grau_saida, "entrada": grau_entrada, "total": grau_total}

    return graus

def percurso_valido(matriz, vertices, caminho):
    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i+1]

        if not existe_aresta(matriz, vertices, u, v):
            print(f"Percurso inválido: Não há aresta de {u} para {v}.")
            return False
    
    print("Percurso é válido.")
    return True

def listar_vizinhos(matriz, vertices, vertice):
    lista = vizinhos(matriz, vertices, vertice)

    print(f"Vizinhos de {vertice}: {lista}")

def exibir_grafo(matriz, vertices):
    print("  ", *vertices)

    for i in range(len(vertices)):
        nome_vertice = vertices[i]
        linha_matriz = matriz[i]

        print(nome_vertice, *linha_matriz)

def main():
    matriz, vertices = criar_grafo()
    
    resposta = input("O grafo será Não-Direcionado? (s/n): ").strip().lower()
    if resposta == 's':
        eh_nao_direcionado = True
    else:
        eh_nao_direcionado = False

    while True:
        print("\nMenu do Grafo (Matriz)")
        print("1: Exibir Grafo")
        print("2: Inserir Vértice")
        print("3: Inserir Aresta")
        print("4: Remover Vértice")
        print("5: Remover Aresta")
        print("6: Listar Vizinhos")
        print("7: Verificar Aresta")
        print("8: Verificar Percurso")
        print("9: Calcular Graus")
        print("0: Sair")
        
        escolha = input("Digite sua escolha: ").strip()
        
        if escolha == '1':
            exibir_grafo(matriz, vertices)
            
        elif escolha == '2':
            nome_do_vertice = input("Digite o nome do vértice: ").strip()
            inserir_vertice(matriz, vertices, nome_do_vertice)
            
        elif escolha == '3':
            origem = input("Digite o vértice de origem: ").strip()
            destino = input("Digite o vértice de destino: ").strip()
            inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=eh_nao_direcionado)
            
        elif escolha == '4':
            vertice = input("Digite o nome do vértice a ser removido: ").strip()
            remover_vertice(matriz, vertices, vertice)

        elif escolha == '5':
            origem = input("Digite o vértice de origem: ").strip()
            destino = input("Digite o vértice de destino: ").strip()
            remover_aresta(matriz, vertices, origem, destino, nao_direcionado=eh_nao_direcionado)

        elif escolha == '6':
            vertice = input("Digite o nome do vértice para ver os vizinhos: ").strip()
            listar_vizinhos(matriz, vertices, vertice)

        elif escolha == '7':
            origem = input("Digite o vértice de origem: ").strip()
            destino = input("Digite o vértice de destino: ").strip()
            resultado = existe_aresta(matriz, vertices, origem, destino)
            if resultado:
                print(f"Sim, existe uma aresta de {origem} para {destino}.")
            else:
                print(f"Não, essa aresta não existe.")

        elif escolha == '8':
            texto_percurso = input("Digite o percurso (ex: A B C): ").strip()
            caminho = texto_percurso.split() 
            percurso_valido(matriz, vertices, caminho)

        elif escolha == '9':
            todos_os_graus = grau_vertices(matriz, vertices, nao_direcionado=eh_nao_direcionado)
            print("Graus dos Vértices")
            for vertice, graus in todos_os_graus.items():
                print(f"{vertice}: {graus}")

        elif escolha == '0':
            print("Saindo...")
            break 
            
        else:
            print("Escolha inválida! Tente novamente.")

if __name__ == "__main__":
    main()
