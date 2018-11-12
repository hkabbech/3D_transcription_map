"""
.. module:: calculation
   :synopsis: This module implements the calculation part
"""

# Third-party modules
import numpy as np

def calculate_correlation_matrix(expressions, path):
    correlations = expressions.transpose().corr(method="spearman")
    correlations.to_csv(path)


def calculate_distance_matrix(coordinates, path):
    for gene in coordinates.index:
        coordinates_copy = coordinates.copy()
        coordinates_copy.loc[gene] = np.NaN
        # Calculation of the distance of the current gene with all genes
        new_dist = np.sqrt((coordinates_copy['X'] - coordinates['X'][gene])**2 +\
                           (coordinates_copy['Y'] - coordinates['Y'][gene])**2 +\
                           (coordinates_copy['Z'] - coordinates['Z'][gene])**2)
        new_dist.name = gene
        try:
            dist =  pd.concat([dist, new_dist], axis=1, join_axes=[dist.index])
        except:
            dist = new_dist
        correlations.to_csv(path)


def calculate_transcription_map(distances, correlations, nb_genes, gene):
    """
    Finds the n closest genes of a current gene and calcules the transcription map corresponding.

    Args:
        coordinates (Pandas Dataframe): X, Y, Z Coordinates of the genes
        correlations (Pandas Dataframe): Correlations of the genes
        nb_genes (int): Closest gene to take into account
        gene (str): The studied gene

    Returns:
        float: The transcription map of the studied gene
    """
    distances_gene = distances[gene]
    # The distances are sorted and the n smallest are selected
    # The corresponding genes represent the closest genes of the current gene
    distances_gene = distances_gene.sort_values(ascending=True, na_position='last')
    closest_genes = distances_gene[:nb_genes].index
    # The transcription map is calculated for the closest genes
    transcription_map = sum(abs(correlations[gene][closest_genes]))
    return transcription_map
