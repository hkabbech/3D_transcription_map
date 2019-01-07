# 3D Transcription map

## Installation

### Clone the repository
```
git clone https://github.com/kabhel/3D_transcription_map.git
cd 3D_transcription_map
```

### Requirements

1. A linux distribution.

2. The programming langage **Python3** and the following standard libraries :
```
pip3 install -r requirements.txt
# This command will install the following modules:
# docopt==0.6.2
# numpy==1.15.2
# pandas==0.23.4
# schema==0.6.8
# tqdm==4.28.1
# plotly==3.4.2
```

## Run the program

The program takes in input a file containing the **3D coordinates** of a chromosome/genome for each genes and a file containing the gene **expression values** in different conditions. The generated interactive plot is in `html` format.

### Toy example
Chromosome 1 of the genome of *Plasmodium falciparum*
```
./3d_transcription_map data/toy_example_chr1/coordinates.txt data/toy_example_chr1/expressions.txt -o results/plot_chr1.html
```

### Get help

```
./3d_transcription_map -h

    Usage:
        ./3d_transcription_map COORDINATES EXPRESSIONS [--nb_genes INT] [--cpu INT] [--output PATH]

    Arguments:
        COORDINATES                     Path to the file containing informations
                                        about 3D coordinates of the genes.
        EXPRESSIONS                     Path to the file containing the gene expression
                                        values in different conditions.
    Options:
        -h, --help                      Show this.
        -n INT, --nb_genes INT          Indicates the number of genes nearby
                                        to take into account. [default: 10]
        -c INT, --cpu INT               Number of cpus to use for parallelisation. By default
                                        using all available (0).
                                        [default: 0]
        -o PATH, --output Path          Path to the generated plot (html format).
                                        [default: results/plot.html]
```

## Author
- **Hélène Kabbech** ~ Bioinformatics master student at Paris Diderot University
- **Costas Bouyioukos** ~ Supervisor
