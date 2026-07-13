import json
from pathlib import Path


class DatasetWriter:
    """
    Writes validated document records to a JSON Lines (JSONL) dataset.

    This class is responsible for persisting processed documents produced
    by the extraction and quality evaluation pipeline. Each document is
    serialized as a single JSON object and appended as one line to the
    output dataset.

    The writer focuses solely on data persistence and does not perform
    crawling, content extraction, or quality evaluation.

    Pipeline Position:
        Crawler
            ↓
        Content Extraction
            ↓
        Quality Evaluation
            ↓
        DatasetWriter   ← This class
            ↓
        JSONL Corpus
    """
    
    
    def __init__(
        self,
        output_dir = "datasets",
        filename = "corpus.jsonl",
    ):
        """
        Initialize the dataset writer.

        Creates the output directory if it does not already exist and
        prepares the destination path for writing JSONL records.
        """
        
        self.output_dir = Path(output_dir)
        self.filepath = self.output_dir / filename
        self.documents_written = 0
        
        self.output_dir.mkdir(
            parents = True,
            exist_ok = True,
        )
        
    
    def write(self, document: dict):
        """
        Append a document record to the JSONL dataset.

        Each document is serialized as a single JSON object and written
        as one line in the output file.
        """
        
        
        with self.filepath.open(
            "a",
            encoding = "utf-8",
        ) as file:
            
            json.dump(
                document,
                file,
                ensure_ascii = False
            )
            
            file.write("\n")
            self.documents_written += 1
            
    def get_document_count(self) -> int:
        """
        Return the number of documents written by this writer.
        """
        
        return self.documents_written