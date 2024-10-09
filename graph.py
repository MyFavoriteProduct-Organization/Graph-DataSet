import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import random
from collections import defaultdict

# Cargar los datos desde el archivo CSV
def load_data():
    return pd.read_csv('BigBasket.csv')

# Procesar los datos para obtener productos
def get_products_from_dataset(dataset):
    products = set()
    for _, row in dataset.iterrows():
        products.add(row['ProductName'])
    return list(products)

# Simular transacciones
def simulate_transactions(products, num_transactions=500, max_products_per_transaction=10):
    transactions = []
    for _ in range(num_transactions):
        num_products = random.randint(2, max_products_per_transaction)
        transaction = random.sample(products, num_products)
        transactions.append(transaction)
    return transactions

# Crear y dibujar el grafo
def create_and_draw_graph(transactions):
    G = nx.Graph()
    product_pairs = defaultdict(int)

    # Contar las apariciones de pares de productos en las transacciones
    for transaction in transactions:
        for i in range(len(transaction)):
            for j in range(i + 1, len(transaction)):
                pair = tuple(sorted([transaction[i], transaction[j]]))
                product_pairs[pair] += 1

    # Añadir nodos y aristas al grafo
    for (product1, product2), weight in product_pairs.items():
        if not G.has_node(product1):
            G.add_node(product1, type='product')
        if not G.has_node(product2):
            G.add_node(product2, type='product')
        G.add_edge(product1, product2, weight=weight)

    # Dibujar el grafo
    pos = nx.spring_layout(G, seed=42, k=0.3, scale=2)
    plt.figure(figsize=(40, 25))  # Aumentar el ancho del canvas
    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=300)
    edges = G.edges(data=True)
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=[d['weight'] for (u, v, d) in edges])
    # nx.draw_networkx_labels(G, pos, font_size=10)
    edge_labels = {(u, v): d['weight'] for (u, v, d) in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.show()

# Cargar y procesar los datos
data = load_data()
products = get_products_from_dataset(data)
transactions = simulate_transactions(products)
create_and_draw_graph(transactions)