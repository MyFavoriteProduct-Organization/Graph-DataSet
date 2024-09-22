import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import random

# Cargar los datos desde el archivo CSV
def load_data():
    return pd.read_csv('BigBasket.csv')

# Procesar los datos para obtener productos y categorías
def get_data_from_dataset(dataset):
    purchase = {}
    for _, row in dataset.iterrows():
        category = row['Category']
        product = row['ProductName']
        if category not in purchase:
            purchase[category] = []
        purchase[category].append(product)
    return purchase

# Crear y dibujar el grafo
def load_graph(graph):
    users = ['U1', 'U2', 'U3', 'U4', 'U5']
    all_products = list({product for products in graph.values() for product in products})

    # Crear una figura con subplots
    fig, axes = plt.subplots(1, len(users), figsize=(20, 5), sharex=True, sharey=True)

    for i, user in enumerate(users):
        G = nx.Graph()
        G.add_node(user, type='user')

        # Asignar aleatoriamente 10 productos a cada usuario con pesos aleatorios de hasta 4
        sampled_products = random.sample(all_products, 10)
        for product in sampled_products:
            weight = random.randint(1, 6)
            G.add_edge(user, product, weight=weight)
            G.add_node(product, type='product')

        # Dibujar el subgrafo
        pos = nx.spring_layout(G, seed=42, k=3)
        ax = axes[i]
        nx.draw_networkx_nodes(G, pos, nodelist=[user], node_color='r', node_size=500, ax=ax, label='Usuario')
        nx.draw_networkx_nodes(G, pos, nodelist=sampled_products, node_color='b', node_size=500, ax=ax, label='Productos')
        edges = G.edges(data=True)
        nx.draw_networkx_edges(G, pos, edgelist=edges, width=[d['weight'] for (u, v, d) in edges], ax=ax)
        nx.draw_networkx_labels(G, pos, font_size=8, ax=ax)
        edge_labels = {(u, v): d['weight'] for (u, v, d) in edges}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, ax=ax)
        ax.set_title(f'Subgrafo de {user}')

    plt.tight_layout()
    plt.show()

# Cargar y procesar los datos
data = load_data()
graph = get_data_from_dataset(data)
load_graph(graph)