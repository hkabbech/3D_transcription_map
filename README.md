# 3D Transcription map

## Installation

### Clone the repository
```
git clone https://github.com/kabhel/3D_transcription_map.git
cd 3D_transcription_map
```

### Requirements

```
pip install -r requirements.txt
```

## Run the program

### Example
Genome of Plasmodium falciparum
```
./3d_transcription_map data/plasmodium_falciparum_coord.txt data/plasmodium_falciparum_exp.min
```

### Get help

```
./3d_transcription_map -h

    Usage:
        ./3d_transcription_map COORD EXP [--closest_genes INT] [--cpu INT]

    Arguments:
        COORD                               Path to the file containing informations
                                            about 3D coordinates of the genes.
        EXP                                 Path to the file containing the gene expression
                                            values in different conditions.
    Options:
        -h, --help                          Show this.
        -n INT, --closest_genes INT         Indicates the number of genes nearby
                                            to take into account.
                                            [default: 10]
        -c NUM, --cpu NUM                   Number of cpus to use for parallelisation. By default
                                            using all available (0).
                                            [default: 0]
```

## Author
- **Hélène Kabbech** ~ Bioinformatics master student at Paris Diderot University
- **Costas Bouyioukos** ~ Supervisor
