import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    try:
        # Convert to list
        if seqs is None:
            return None

        seqs = list(seqs)
        N = len(seqs)

        # Empty input → (0,0) array
        if N == 0:
            return np.zeros((0, 0), dtype=int)

        # Determine max_len
        if max_len is None:
            max_len = max(len(seq) for seq in seqs)
        else:
            max_len = int(max_len)

        if max_len < 0:
            return None

        # Initialize output array
        padded = np.full((N, max_len), pad_value, dtype=int)

        for i, seq in enumerate(seqs):
            seq = np.asarray(seq, dtype=int)
            length = min(len(seq), max_len)
            if length > 0:
                padded[i, :length] = seq[:length]

        return padded

    except Exception:
        return None