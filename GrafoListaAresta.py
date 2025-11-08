def criar_grafo():
    vertices = []
    arestas = []

    return vertices, arestas

def inserir_vertice(vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)
        print(f"Vértice '{vertice}' inserido.") 
    else:
        print(f"Vértice '{vertice}' já existe.")

def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(vertices, origem)
        
    if destino not in vertices:
        inserir_vertice(vertices, destino)

    lista_od = [origem, destino]

    if lista_od not in arestas:
        arestas.append(lista_od)
        print(f"Aresta {origem} -> {destino} inserida.")
    else:
        print(f"Aresta {origem} -> {destino} já existe.")

    if nao_direcionado and origem != destino:
        lista_od_reversa = [destino, origem]

        if lista_od_reversa not in arestas:
            arestas.append(lista_od_reversa)
            print(f"Aresta inversa {destino} -> {origem} inserida.")

def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    aresta_para_remover = [origem, destino]
    
    if aresta_para_remover in arestas:
        arestas.remove(aresta_para_remover)
        print(f"Aresta {origem} -> {destino} removida.")
    else:
        print(f"Aresta {origem} -> {destino} não foi encontrada.")

    if nao_direcionado:
        aresta_inversa = [destino, origem]
        
        if aresta_inversa in arestas:
            arestas.remove(aresta_inversa)
            print(f"Aresta inversa {destino} -> {origem} removida.")         
        
def remover_vertice(vertices, arestas, vertice):
    if vertice in vertices:
        vertices.remove(vertice)
        print(f"Vértice '{vertice}' removido.")
    else:
        print(f"Vértice '{vertice}' não encontrado.")
        return 

    novas_arestas = []
    for aresta in arestas:
        if vertice not in aresta:
            novas_arestas.append(aresta)
            
    arestas.clear()
    arestas.extend(novas_arestas)

def existe_aresta(arestas, origem, destino):
    aresta_procurada = [origem, destino]

    return aresta_procurada in arestas
    
def vizinhos(vertices, arestas, vertice):
    lista_de_vizinhos = [] 
 
    for origem_aresta, destino_aresta in arestas: 
        if origem_aresta == vertice: 
            
            lista_de_vizinhos.append(destino_aresta)
            
    return lista_de_vizinhos

def grau_vertices(vertices, arestas, nao_direcionado = False):
    graus = {}

    for vertice in vertices:
        if nao_direcionado:
            graus[vertice] = 0
        else:
            graus[vertice] = {"saida": 0, "entrada": 0, "total": 0}

    for origem, destino in arestas:
        if nao_direcionado:
            graus[origem] += 1

        else:
            graus[origem]["saida"] += 1
            graus[destino]["entrada"] += 1

    if not nao_direcionado:
        for vertice in vertices:
            graus[vertice]["total"] = graus[vertice]["saida"] + graus[vertice]["entrada"]

    return graus

def percurso_valido(arestas, caminho):
    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i+1]

        if not existe_aresta(arestas, u, v):
            print(f"Percurso inválido: Não há aresta de {u} para {v}.")
            return False 
    
    print("Percurso é válido.")
    return True

def listar_vizinhos(vertices, arestas, vertice):
    lista = vizinhos(vertices, arestas, vertice)

    print(f"Vizinhos de {vertice}: {lista}")

def exibir_grafo(vertices, arestas):
    print(f"Vértices: {vertices}")
    
    print("Arestas:")
    for origem, destino in arestas:
        print(f"  {origem} -> {destino}")

def main():
    vertices, arestas = criar_grafo()
    
    resposta = input("O grafo será Não-Direcionado? (s/n): ").strip().lower()
    if resposta == 's':
        eh_nao_direcionado = True
    else:
        eh_nao_direcionado = False

    while True:
        print("\nMenu do Grafo (Lista de Arestas)")
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
            exibir_grafo(vertices, arestas)
            
        elif escolha == '2':
            nome_do_vertice = input("Digite o nome do vértice: ").strip()
            inserir_vertice(vertices, nome_do_vertice) 
            
        elif escolha == '3':
            origem = input("Digite o vértice de origem: ").strip()
            destino = input("Digite o vértice de destino: ").strip()
            inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=eh_nao_direcionado)
            
        elif escolha == '4':
            vertice = input("Digite o nome do vértice a ser removido: ").strip()
            remover_vertice(vertices, arestas, vertice)

        elif escolha == '5':
            origem = input("Digite o vértice de origem: ").strip()
            destino = input("Digite o vértice de destino: ").strip()
            remover_aresta(arestas, origem, destino, nao_direcionado=eh_nao_direcionado)

        elif escolha == '6':
            vertice = input("Digite o nome do vértice para ver os vizinhos: ").strip()
            listar_vizinhos(vertices, arestas, vertice)

        elif escolha == '7':
            origem = input("Digite o vértice de origem: ").strip()
            destino = input("Digite o vértice de destino: ").strip()
            resultado = existe_aresta(arestas, origem, destino)
            if resultado:
                print(f"Sim, existe uma aresta de {origem} para {destino}.")
            else:
                print(f"Não, essa aresta não existe.")

        elif escolha == '8':
            texto_percurso = input("Digite o percurso (ex: A B C): ").strip()
            caminho = texto_percurso.split() 
            percurso_valido(arestas, caminho)

        elif escolha == '9':
            todos_os_graus = grau_vertices(vertices, arestas, nao_direcionado=eh_nao_direcionado)
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
