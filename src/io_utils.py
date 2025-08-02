import numpy as np

def load_fasta(filepath):
    """Load sequences from FASTA file as a list of strings."""
    sequences = []
    with open(filepath, 'r') as f:
        seq = ''
        for line in f:
            if line.startswith('>'):
                if seq:
                    sequences.append(seq)
                    seq = ''
            else:
                seq += line.strip()
        if seq:
            sequences.append(seq)
    return sequences

def save_numpy_array(arr, filepath):
    """Save numpy array to file."""
    np.save(filepath, arr)
