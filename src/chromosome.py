"""
.. module:: Chromosome
   :synopsis: This module implements the Chromosome class.
"""

# Third-party modules
import numpy as np

def process(chromosome):
    distances_matrix = chromosome.calculate_distances_matrix()
    return distances_matrix, chromosome.name

class Chromosome:
    """
    .. class:: Chromosome

      This class groups informations about a chromosome.

    Attributes:
        name: Name of the chromosome
        genes: List of genes
    """
    __slots__ = ("name", "genes")

    def __init__(self, name):
        self.name = name
        self.genes = None

    def __str__(self):
        line = self.name + "\n"
        for gene in self.genes:
            line += "  " + gene.__str__() + "\n"
        return line

    def set_genes(self, genes):
        self.genes = genes


    def calculate_distances_matrix(self):
        nb_genes = len(self.genes)
        # This sets a numpy matrix of shape query * query which will contain all
        # distances between all pairs of genes coordinates
        distances = np.empty((nb_genes, nb_genes), dtype=object)
        # Filling the matrix afterwards with "NaN" is faster
        distances.fill(np.nan)

        for i in range(nb_genes):
            for j in range(i+1, nb_genes):
                # Calculate distance between two genes
                distances[i, j] = self.genes[i].calculate_distance(self.genes[j])
        return distances
