import numpy as np

class Individual:
    def __init__(self, num_nodes, max_colors):
        """
        num_nodes: Total nodes in the graph
        max_colors: Initial range of colors
        """
        # Genes = Random Integer (Color) for each node (0 to max_colors - 1)
        self.genes = np.random.randint(0, max_colors, size=num_nodes)
        self.fitness = 0
        self.conflicts = 0

    def __len__(self):
        return len(self.genes)
    
    def copy(self):
        new_ind = Individual(len(self.genes), 0)
        new_ind.genes = np.copy(self.genes)
        new_ind.fitness = self.fitness
        new_ind.conflicts = self.conflicts
        return new_ind
    