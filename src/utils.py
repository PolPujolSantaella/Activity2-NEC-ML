import os 
from src.loading_data import load_graph
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib.lines as mlines

def loading_graphs(path, size=""):
    if os.path.exists(path):
        graph = load_graph(path)
        print(f"{size} Graph Loaded")
        print(f"Nodes: {graph.number_of_nodes()}")
        print(f"Edges: {graph.number_of_edges()}")

    else:
        print(f"File {path} not found.")
    
    return graph


def plot_graph(graph, title="Graph"):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph, seed = 42)
    nx.draw(graph, pos,
            with_labels=True,
            node_color='lightblue',
            edge_color='gray',
            node_size=500,
            font_size=10)
    
    plt.title(title)
    plt.show()


def plot_colored_graph(G, individual, title="GCP Solution"):
    plt.figure(figsize = (8, 6))
    pos = nx.spring_layout(G, seed = 42)

    unique_genes = np.unique(individual.genes)
    cmap = plt.cm.rainbow
    norm = plt.Normalize(vmin=min(individual.genes), vmax=max(individual.genes))

    nx.draw(G, pos,
            with_labels=True,
            node_color=individual.genes,
            cmap=cmap,
            edge_color='black',
            node_size=600,
            font_size=12,
            width=1.5)
    
    legend_handles = []
    for gene in sorted(unique_genes):
        color = cmap(norm(gene))
        
        line = mlines.Line2D([], [], color=color, marker='o', linestyle='None',
                              markersize=10, label=f'Color ID: {gene}')
        legend_handles.append(line)

    plt.legend(handles=legend_handles, title="Colors", 
               bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.title(f"{title}\nConflicts: {individual.conflicts} | Total Colors: {len(unique_genes)}")
    plt.show()