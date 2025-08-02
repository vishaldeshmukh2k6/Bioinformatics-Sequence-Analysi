from io_utils import load_fasta
from preprocess import clean_sequences, encode_sequence
from analysis import gc_content, motif_count
from alignments import hamming_distance, simple_alignment_score
from mutations import mutate_sequence
import sys

def main():
    fasta_file = 'data/raw/sample.fasta'
    sequences = load_fasta(fasta_file)
    print(f"Loaded {len(sequences)} sequences.")

    sequences = clean_sequences(sequences)
    print(f"{len(sequences)} sequences after cleaning.")

    motif = 'ATG'
    motif_counts = motif_count(sequences, motif)
    print(f"Motif '{motif}' counts: {motif_counts}")
    
    gc_contents = [gc_content(seq) for seq in sequences]
    print("Average GC content: {:.3f}".format(sum(gc_contents)/len(gc_contents) if gc_contents else 0))

    # Pairwise example:
    if len(sequences) >= 2:
        print("Hamming distance (first 2 seq):", hamming_distance(sequences[0], sequences[1][:len(sequences[0])]))
        print("Alignment score (first 2 seq):", simple_alignment_score(sequences[0], sequences[1]))

    # Mutation example
    if sequences:
        print("Original: ", sequences[0])
        print("Mutated:  ", mutate_sequence(sequences[0], mutation_rate=0.05))

if __name__ == "__main__":
    main()
