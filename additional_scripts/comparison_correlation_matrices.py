#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Usage:
        ./3d_transcription_map COORDINATES EXPRESSIONS

    Arguments:
        COORDINATES                     Path to the file containing informations
                                        about 3D coordinates of the genes.
        EXPRESSIONS                     Path to the file containing the gene expression
                                        values in different conditions.
"""

# Third-party modules
from datetime import datetime
from docopt import docopt
from schema import Schema, Use, SchemaError
import pandas as pd
import numpy as np


def check_args():
    """
        Checks and validates the types of inputs parsed by docopt from command line.
    """
    schema = Schema({
        'COORDINATES': Use(open, error='Gene coordinate file should be readable.'),
        'EXPRESSIONS': Use(open, error='Gene expression file should be readable.'),
        object: object})
    try:
        schema.validate(ARGUMENTS)
    except SchemaError as err:
        exit(err)

if __name__ == "__main__":


    ### Parse command line
    ######################

    ARGUMENTS = docopt(__doc__, version='3d_transcription_map 1.0')

    # Check the types and ranges of the command line arguments parsed by docopt
    check_args()

    COORDINATES_FILE = ARGUMENTS["COORDINATES"]
    EXPRESSIONS_FILE = ARGUMENTS["EXPRESSIONS"]

    ### Data frames
    ###############
    COORDINATES = pd.read_csv(COORDINATES_FILE, sep='\t')
    EXPRESSIONS = pd.read_csv(EXPRESSIONS_FILE, sep='\t')


    print("\n\nTime comparison between two methods to calculate a correlation matrix", end=" ")
    print("using pearson method.")

    print("\n\nCalculation of the correlation matrix using pandas functions.")
    print("(transpose() and corr() functions).")
    START_TIME = datetime.now()
    CORRELATIONS_PANDAS = EXPRESSIONS.transpose().corr(method="pearson")
    print("\nTotal runtime: {} seconds".format(str(datetime.now() - START_TIME)))

    print("\n\nCalculation of the correlation matrix using a numpy function.")
    print("(corrcoeff() function)")
    print("followed by the transformation of the numpy array into a pandas DataFrame.")

    START_TIME = datetime.now()
    CORRELATIONS_NUMPY = pd.DataFrame(data=np.corrcoef(EXPRESSIONS),
                                      index=EXPRESSIONS.index,
                                      columns=EXPRESSIONS.index)
    print("\nTotal runtime: {} seconds".format(str(datetime.now() - START_TIME)))
