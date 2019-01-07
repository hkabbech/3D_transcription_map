"""
.. module:: calculation
   :synopsis: This module implements the calculation part
"""

# Third-party modules
import numpy as np

def calculate_transcription_map(coordinates, correlations, nb_genes, gene):
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
    # NaN values are set instead of the coordinate values of the current gene
    # because the distance does not need to be calculated
    coordinates_copy = coordinates.copy()
    coordinates_copy.loc[gene] = np.NaN
    # Calculation of the distance of the current gene with all genes
    distances = np.sqrt((coordinates_copy['X'] - coordinates['X'][gene])**2 +\
                        (coordinates_copy['Y'] - coordinates['Y'][gene])**2 +\
                        (coordinates_copy['Z'] - coordinates['Z'][gene])**2)
    # The distances are sorted and the n smallest are selected
    # The corresponding genes represent the closest genes of the current gene
    distances = distances.sort_values(ascending=True, na_position='last')

    closest_genes = distances[:nb_genes].index
    correlations_closest_genes = correlations[gene][closest_genes]
    nb_nan = correlations_closest_genes.isna().sum()
    nb_genes_without_nan = nb_genes - nb_nan

    # All N closest genes have nan value
    if nb_genes_without_nan == 0:
        return np.nan
    # The transcription map is calculated for the N closest genes
    # All na values are replace by 0
    else:
        return sum(abs(correlations_closest_genes.fillna(0))) / nb_genes_without_nan
