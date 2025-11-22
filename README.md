# Atividade - Implementação de Grafos

Este projeto, desenvolvido para fins acadêmicos, contém implementações de estruturas de dados de Grafos em Python, permitindo a manipulação de grafos direcionados e não-direcionados.

## 📜 Descrição do Projeto

O objetivo deste trabalho é demonstrar o funcionamento e as diferenças entre três representações clássicas de grafos:
* Matriz de Adjacência
* Lista de Adjacência
* Lista de Arestas

Cada implementação é fornecida em seu próprio arquivo Python e inclui um menu interativo para testar as funcionalidades.

## 🚀 Implementações

O repositório contém os seguintes scripts:

* **`GrafoMatrizAdjacência.py`**: Implementação de um grafo utilizando Matriz de Adjacência.
* **`GrafoListaAdjacência.py`**: Implementação de um grafo utilizando Lista de Adjacência (com dicionários).
* **`GrafoListaAresta.py`**: Implementação de um grafo utilizando uma Lista de Arestas e uma Lista de Vértices.

## ✨ Funcionalidades Comuns

Cada script permite ao usuário:
* Escolher entre um grafo Direcionado ou Não-Direcionado.
* Exibir o grafo.
* Inserir e remover Vértices.
* Inserir e remover Arestas.
* Listar os vizinhos de um vértice.
* Verificar a existência de uma aresta.
* Verificar se um percurso (caminho) é válido.
* Calcular os graus (entrada, saída e total) dos vértices.

## 🔍 Algoritmos de Busca e Travessia


Além das funcionalidades básicas, foram implementados algoritmos de busca para percorrer e analisar os grafos:

### Busca em Largura (BFS)
* **`BFS_Padrao(grafo, vertice)`**: Realiza a travessia do grafo em largura, utilizando uma fila para visitar todos os vértices alcançáveis a partir de um nó inicial.
* **`BFS_menor_caminho(grafo, origem, destino)`**: Utiliza a lógica da BFS para encontrar e retornar o caminho mais curto (menor número de arestas) entre um vértice de origem e um de destino.

### Busca em Profundidade (DFS)
* **`DFS_Padrao(grafo, vertice)`**: Realiza a travessia do grafo em profundidade, utilizando uma pilha para explorar cada ramo o máximo possível antes de retroceder.
* **`DFS_Ciclos(grafo, vertice)`**: Uma variação da DFS que verifica a integridade estrutural do grafo, detectando se existem ciclos (caminhos fechados) através da identificação de arestas de retorno.

## 🧑‍💻 Integrantes

* **Jean Lucas Felix da Conceição** - RA 2012388
* **Maria Elisa Proença Coqueiro** - RA 2013350
* **Guilherme Viana Morrone** - RA 1991991
