from collections.abc import Iterator


def token_stream(text: str, chunk_size: int = 512) -> Iterator[str]:
    """Split text into token chunks and yield one chunk at a time.

    Args:
        text: Input text.
        chunk_size: Number of tokens in each chunk.

    Yields:
        A string containing one chunk of tokens.

    Raises:
        ValueError: If chunk_size is less than or equal to zero.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero.")

    tokens = text.split()

    for i in range(0, len(tokens), chunk_size):
        chunk = " ".join(tokens[i:i + chunk_size])
        yield chunk


if __name__ == "__main__":
    text = "The quick brown fox jumps over the lazy dog. " * 50

    for i, chunk in enumerate(token_stream(text, chunk_size=20), 1):
        print(f"Chunk {i}: {len(chunk.split())} tokens")