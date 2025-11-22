Atividade - Implementação de Grafos

Este projeto, desenvolvido para fins acadêmicos, contém implementações de estruturas de dados de Grafos em Python, permitindo a manipulação de grafos direcionados e não-direcionados.

📜 Descrição do Projeto

O objetivo deste trabalho é demonstrar o funcionamento e as diferenças entre três representações clássicas de grafos:

Matriz de Adjacência

Lista de Adjacência

Lista de Arestas

Cada implementação é fornecida em seu próprio arquivo Python e inclui um menu interativo para testar as funcionalidades.

🚀 Implementações

O repositório contém os seguintes scripts:

GrafoMatrizAdjacência.py: Implementação de um grafo utilizando Matriz de Adjacência.

GrafoListaAdjacência.py: Implementação de um grafo utilizando Lista de Adjacência (com dicionários).

GrafoListaAresta.py: Implementação de um grafo utilizando uma Lista de Arestas e uma Lista de Vértices.

✨ Funcionalidades Comuns

Cada script permite ao usuário:

Escolher entre um grafo Direcionado ou Não-Direcionado.

Exibir o grafo.

Inserir e remover Vértices.

Inserir e remover Arestas.

Listar os vizinhos de um vértice.

Verificar a existência de uma aresta.

Verificar se um percurso (caminho) é válido.

Calcular os graus (entrada, saída e total) dos vértices.

🧠 Algoritmos de Busca e Travessia

Além das estruturas básicas, o projeto implementa algoritmos fundamentais de percurso em grafos:

1. Busca em Largura (BFS - Breadth-First Search)

Utiliza uma estrutura de Fila (Queue) para explorar o grafo nível por nível.

BFS_Padrao(grafo, vertice): Realiza a travessia completa do grafo a partir de um vértice inicial, visitando todos os vizinhos diretos antes de avançar para o próximo nível. Retorna a lista de vértices visitados na ordem de descoberta.

BFS_menor_caminho(grafo, origem, destino): Uma adaptação da BFS utilizada para encontrar o caminho mais curto (menor número de arestas) entre uma origem e um destino em grafos não-ponderados. Retorna a lista contendo o caminho exato ou uma lista vazia caso não haja conexão.

2. Busca em Profundidade (DFS - Depth-First Search)

Utiliza uma estrutura de Pilha (Stack) (ou recursão) para explorar o grafo, indo o mais fundo possível em um ramo antes de retroceder (backtracking).

DFS_Padrao(grafo, vertice): Realiza a travessia priorizando a profundidade. O algoritmo segue um caminho até não haver mais vizinhos não visitados, desempilha e explora novos ramos.

DFS_Ciclos(grafo, vertice): Uma variação da DFS projetada para detecção de ciclos. Durante a travessia, verifica se um vértice vizinho já foi visitado e se ele não é o "pai" (o vértice anterior imediato). Se essa condição for atendida, confirma-se a existência de um ciclo (aresta de retorno).

🧑‍💻 Integrantes

Jean Lucas Felix da Conceição - RA 2012388

Maria Elisa Proença Coqueiro - RA 2013350

Guilherme Viana Morrone - RA 1991991
