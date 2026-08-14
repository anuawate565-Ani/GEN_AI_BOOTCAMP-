import csv
import logging
from collections.abc import Iterator

logger = logging.getLogger(__name__)


class DatasetBatchGenerator:
    """
    Stream large CSV files in batches.
    Memory efficient: only loads one batch at a time.

    Usage:
        gen = DatasetBatchGenerator("data.csv", batch_size=32)
        for batch in gen:
            print(f"Batch: {len(batch)} rows")
    """

    def __init__(self, filepath: str, batch_size: int = 32):
        """
        Args:
            filepath: Path to CSV file.
            batch_size: Rows per batch.
        """
        if batch_size <= 0:
            raise ValueError("batch_size must be greater than zero.")

        self.filepath = filepath
        self.batch_size = batch_size

        logger.info(
            f"Initialized BatchGenerator: {filepath}, "
            f"batch_size={batch_size}"
        )

    def __iter__(self) -> Iterator[list[dict[str, str]]]:
        """
        Iterate over CSV rows in batches.

        Yields:
            A list of CSV rows as dictionaries.
        """
        with open(self.filepath, "r", newline="") as file:
            reader = csv.DictReader(file)
            batch: list[dict[str, str]] = []

            for row in reader:
                batch.append(row)

                if len(batch) == self.batch_size:
                    logger.info(
                        f"Yielding batch of {len(batch)} rows"
                    )
                    yield batch
                    batch = []

            if batch:
                logger.info(
                    f"Yielding final batch of {len(batch)} rows"
                )
                yield batch


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    gen = DatasetBatchGenerator("data.csv", batch_size=10)

    for i, batch in enumerate(gen, 1):
        print(f"Batch {i}: {len(batch)} rows")

        for row in batch:
            print(f"  - {row}")