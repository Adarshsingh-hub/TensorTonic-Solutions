def text_chunking(tokens, chunk_size, overlap):
    try:
        tokens = list(tokens)
        chunk_size = int(chunk_size)
        overlap = int(overlap)

        if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
            return None

        n = len(tokens)
        if n == 0:
            return []

        step = chunk_size - overlap
        chunks = []

        for start in range(0, n, step):
            end = start + chunk_size
            chunks.append(tokens[start:end])
            if end >= n:
                break

        return chunks

    except Exception:
        return None