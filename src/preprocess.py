import numpy as np

def encode_sequence(seq):
    """Encode DNA as integers: A=0, C=1, G=2, T=3 (-1 for others)."""
    mapping = {'A':0, 'C':1, 'G':2, 'T':3}
    return np.array([mapping.get(base, -1) for base in seq])

def clean_sequences(seq_list):
    """Remove sequences containing invalid characters."""
    allowed = set('ACGT')
    cleaned = [s for s in seq_list if set(s).issubset(allowed)]
    return cleaned
