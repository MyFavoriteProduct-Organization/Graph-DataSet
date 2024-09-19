import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
def load_data():
    return pd.read_csv('/Users/lordmathi2741/Downloads/BigBasket.csv')

def get_data_from_dataset(dataset):
       purchase = {}
       for _, row in dataset.iterrows():
           category = row['Category']
           product = row['ProductName']
           if category not in purchase:
               purchase[category] = []
           purchase[category].append(product)
       return purchase

def load_graph(graph):
    G = nx.DiGraph()

    for category, products in graph.items():
        G.add_node(category, type='category')
        for product in products:
            G.add_node(product, type='product')
            G.add_edge(category, product)
    figsize = (12, 12)
    node_size = 50
    title = 'Graph of Purchase'

    plt.figure(figsize=figsize)
    position = nx.spring_layout(G, seed=42)  
    category_nodes = [n for n, attr in G.nodes(data=True) if attr['type'] == 'category']
    product_nodes = [n for n, attr in G.nodes(data=True) if attr['type'] == 'product']
    nx.draw_networkx_nodes(G, position, nodelist=category_nodes, node_color='r', node_size=node_size, label='Category')
    nx.draw_networkx_nodes(G, position, nodelist=product_nodes, node_color='b', node_size=node_size, label='Product')

    nx.draw_networkx_edges(G, position, alpha=0.5, edge_color='gray')

    
    plt.title(title)
    plt.legend()
    plt.show()
   
data = load_data()
graph = get_data_from_dataset(data)
load_graph(graph)

   
   
     
     
          
           

           
        

