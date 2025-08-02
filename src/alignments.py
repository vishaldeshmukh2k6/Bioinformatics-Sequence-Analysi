import numpy as np

def hamming_distance(seq1, seq2):
    """Hamming distance for same-length sequences."""
    assert len(seq1) == len(seq2), "Sequences must be same length"
    return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))

def simple_alignment_score(seq1, seq2, match=1, mismatch=-1, gap=-2):
    """Very simple global alignment, no traceback."""
    n, m = len(seq1), len(seq2)
    dp = np.zeros((n+1, m+1), dtype=int)
    for i in range(n+1):
        dp[i][0] = i * gap
    for j in range(m+1):
        dp[0][j] = j * gap
    for i in range(1, n+1):
        for j in range(1, m+1):
            score = match if seq1[i-1] == seq2[j-1] else mismatch
            dp[i][j] = max(
                dp[i-1][j-1] + score,
                dp[i-1][j] + gap,
                dp[i][j-1] + gap
            )
    return dp[n][m]
