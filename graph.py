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
    G = nx.Graph()

    # Agregar nodos de usuarios de ejemplo
    users = ['U1']
    for user in users:
        G.add_node(user, type='user')

    # Obtener todos los productos del dataset
    all_products = list({product for products in graph.values() for product in products})

    # Asignar aleatoriamente 10 productos a cada usuario con pesos aleatorios de hasta 4
    interactions = []
    for user in users:
        sampled_products = random.sample(all_products, 25)
        for product in sampled_products:
            weight = random.randint(1, 6)
            interactions.append((user, product, weight))

    # Agregar aristas de interacción entre usuarios y productos
    for user, product, weight in interactions:
        G.add_edge(user, product, weight=weight)

    # Filtrar productos que los usuarios han comprado
    purchased_products = {product for _, product, _ in interactions}

    # Agregar nodos de productos comprados
    for product in purchased_products:
        G.add_node(product, type='product')

    # Dibujar el grafo
    pos = nx.spring_layout(G, seed=42, k=3)  # Ajustar el parámetro k para más espacio entre nodos

    # Ajustar el tamaño del canvas
    plt.figure(figsize=(12, 8))  # Ancho y alto en pulgadas

    # Dibujar nodos
    nx.draw_networkx_nodes(G, pos, nodelist=purchased_products, node_color='b', node_size=500, label='Productos')
    nx.draw_networkx_nodes(G, pos, nodelist=users, node_color='r', node_size=500, label='Usuarios')

    # Dibujar aristas con pesos
    edges = G.edges(data=True)
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=[d['weight'] for (u, v, d) in edges])

    # Dibujar etiquetas de nodos con tamaño de letra reducido
    nx.draw_networkx_labels(G, pos, font_size=8)

    # Dibujar etiquetas de pesos en las aristas con tamaño de letra reducido
    edge_labels = {(u, v): d['weight'] for (u, v, d) in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # Mostrar leyenda y grafo
    plt.legend(scatterpoints=1)
    plt.title('Grafo de Usuarios y Productos con Pesos')
    plt.show()

# Cargar y procesar los datos
data = load_data()
graph = get_data_from_dataset(data)
load_graph(graph)