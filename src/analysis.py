import numpy as np

def motif_count(sequences, motif):
    """Count occurrences of a motif in each sequence."""
    motif_len = len(motif)
    counts = []
    for seq in sequences:
        count = 0
        for i in range(len(seq) - motif_len + 1):
            if seq[i:i+motif_len] == motif:
                count += 1
        counts.append(count)
    return counts

def gc_content(sequence):
    """GC proportion of a sequence."""
    gc = sequence.count('G') + sequence.count('C')
    try:
        return gc / len(sequence)
    except ZeroDivisionError:
        return 0.0
