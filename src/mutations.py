import random

def mutate_sequence(seq, mutation_rate=0.01):
    """Randomly mutate characters in seq at mutation_rate."""
    bases = ['A', 'C', 'G', 'T']
    new_seq = []
    for c in seq:
        if random.random() < mutation_rate:
            candidates = [b for b in bases if b != c]
            new_seq.append(random.choice(candidates))
        else:
            new_seq.append(c)
    return ''.join(new_seq)
