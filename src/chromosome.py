import numpy as np

class Individual:
    def __init__(self, num_nodes, max_colors, genes=None):
        """
        num_nodes: Total nodes in the graph
        max_colors: Max number of colors allowed
        genes: Optional, predefined gene sequence
        """

        self.num_nodes = num_nodes
        self.max_colors = max_colors

        self.fitness = None
        self.conflicts = None

        if genes is None:
            # Genes = Random Integer (Color) for each node (0 to max_colors - 1)
            self.genes = np.random.randint(0, max_colors, size=num_nodes)
        else:
            self.genes = np.array(genes, dtype=int)

    def __len__(self):
        return self.num_nodes
    
    def copy(self):
        new_ind = Individual(
            num_nodes=self.num_nodes,
            max_colors=self.max_colors,
            genes=np.copy(self.genes)
        )
        new_ind.fitness = self.fitness
        new_ind.conflicts = self.conflicts
        return new_ind
    
    def num_colors_used(self):
        return len(np.unique(self.genes))