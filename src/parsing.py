"""
.. module:: parsing
   :synopsis: This module implements all the functions to parse either input
                or additional necessary files.
"""

# Third-party modules
import numpy as np
from src.chromosome import Chromosome
from src.gene import Gene

def parse_gene_coordinates(gene_coordinates_file):
    chromosomes_list = []
    current_chr = None
    with open(gene_coordinates_file, "r") as file:
        # The header is skipped
        file.readline()
        for line in file:
            # Elements of the current line are stored into a list
            ele = line[:-1].split("\t")
            # If we encountered a new chromosome :
            if current_chr != ele[1]:
                current_chr = ele[1]
                # The dictionary of genes is setted to the last
                # chromosome object of the list
                if chromosomes_list != []:
                    chromosomes_list[-1].set_genes(gene_list)
                # Then, a chromosome object is created with the
                # corresponding dictionary of genes
                chromosomes_list.append(Chromosome(current_chr))
                gene_list = []
            # A gene is added into the dictionary of genes for the current chromosome
            gene_name = ele[0]
            gene_coords = np.array([float(ele[2]), float(ele[3]), float(ele[4])])
            gene_list.append(Gene(gene_name, gene_coords))
    # Before returning the list of chromosome, we do not forget to set the dictionary
    # of genes of the last chromosome
    chromosomes_list[-1].set_genes(gene_list)
    return chromosomes_list
