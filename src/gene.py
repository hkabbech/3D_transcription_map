"""
.. module:: Gene
   :synopsis: This module implements the Gene class.
"""

# Third-party modules
import numpy as np

class Gene:
    """
    .. class:: Gene

      This class groups informations about a gene.

    Attributes:
        name: Name of the gene
        coords: X, Y, Z coordinates
    """
    __slots__ = ("name", "coords")

    def __init__(self, name, coords):
        self.name = name
        self.coords = coords

    def __str__(self):
        return self.name + " " + str(self.coords)

    def calculate_distance(self, gene):
        """
            Calculate Euclidian distance between two genes.
            Formula: distance = sqrt((xa-xb)**2 + (ya-yb)**2 + (za-zb)**2)

            Args:
                gene (object): An object of the Gene class.

            Returns:
                dist (float): The calculated distance.
        """
        a_min_b = self.coords - gene.coords
        distance = np.sqrt(np.einsum('i,i->', a_min_b, a_min_b))
        return distance
