import networkx as nx

def load_graph(file_path):
    """
    Loading data from a file .col.txt and returns a NetworkX graph.
    Comment Lines (c), Problem Lines (p), and edges lines (e) 
    """

    G = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            # Skip comments
            if line.startswith('c') or not line.strip():
                continue

            parts = line.split()

            # Problem Line
            if parts[0] == 'p':
                num_nodes = int(parts[2])
                
                # Add nodes 1 to N
                G.add_nodes_from(range(1, num_nodes + 1))
            
            # Edge Lines
            elif parts[0] == 'e':
                u, v = int(parts[1]), int(parts[2])
                G.add_edge(u, v)
    return G