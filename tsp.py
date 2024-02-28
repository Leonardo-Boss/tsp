import random
import networkx as nx
import matplotlib.pyplot as plt
import csv

class Propriedade:
    def __init__(self, name, parcelas, area, apoio) -> None:
        self.name = name
        self.hours = parcelas * 2
        self.area = area
        self.apoio = apoio

class Edge:
    def __init__(self, a, b, weight) -> None:
        self.a = a
        self.b = b
        self.weight = weight

def read_propriedades(path):
    with open(path) as f:
        reader = csv.reader(f)
        next(reader)
        return {p[1]:Propriedade(p[1],p[2],p[0], False) for p in reader}

def read_edges(path):
    path = 'rotas_entre_apoios.csv'
    with open(path) as f:
        reader = csv.reader(f)
        next(reader)
        edges = [Edge(i[0],i[1],i[2]) for i in reader]
    return edges

def test(edges:list[Edge]):
    new = list(set(map(lambda x: x.a, edges)))
    lenght = len(new)
    apoios = {n:Propriedade(n,0,0,True) for n in new[:lenght]}
    prop = {n:Propriedade(n,random.randint(1,5),random.randint(1,5),False) for n in new[lenght:]}
    return (apoios,prop)

def generate_graph(apoios:dict, propriedades:dict, edges:list):
    G = nx.Graph()
    for i in apoios.values():
        G.add_node(i)
    for i in propriedades.values():
        G.add_node(i)
    for i in edges:
        G.add_edge(i.a, i.b, weight=i.weight)
    return G

def plot_graph_step(G, tour, current_node, pos):
    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color = 'lightblue', node_size=200)
    path_edges = list(zip(tour, tour[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='green', node_size = 200)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.pause(0.3)

def calculate_tour_cost():
    pass

def nearestneighbour():
    pass

if __name__ == "__main__":
    # propriedades = read_propriedades('parcelas por propriedade total.csv')
    edges = read_edges('rotas_entre_apoios.csv')
    apoios, propriedades = test(edges)
    G = generate_graph(apoios, propriedades, edges)
