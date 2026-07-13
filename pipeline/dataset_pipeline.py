from extractor.pipeline import process_html
from extractor.quality import evaluate_quality
from dataset.writer import DatasetWriter


class DatasetPipeline:
    """
    Orchestrates the end-to-end dataset generation workflow.

    This pipeline coordinates the extraction, quality evaluation, and
    persistence of webpage content. It transforms raw HTML into a
    structured document record, evaluates its quality, and routes the
    document to the appropriate dataset writer.

    The pipeline acts as the orchestration layer of the data ingestion
    system and delegates specialized tasks to dedicated components
    instead of implementing their logic directly.

    Pipeline Workflow:
        Raw HTML
            ↓
        Content Extraction
            ↓
        Text Normalization
            ↓
        Quality Evaluation
            ↓
        Document Creation
            ↓
        Routing
            ↓
        Accepted / Rejected Dataset
    """


    def __init__(
        self,
        accepted_writer: DatasetWriter,
        rejected_writer: DatasetWriter,
    ):
        """
        Initialize the dataset pipeline with dataset writers.

        Args:
            accepted_writer: Writer used for high-quality documents.
            rejected_writer: Writer used for rejected documents.
        """
        
        self.accepted_writer = accepted_writer
        self.rejected_writer = rejected_writer

    def process(
        self,
        url: str,
        html: str,
    ):
        """
        Process a webpage through the complete dataset pipeline.

        The method extracts clean text from raw HTML, evaluates document
        quality, constructs a document record, routes it to the appropriate
        dataset writer, and returns the generated document.

        Args:
            url: Source URL of the webpage.
            html: Raw HTML content.

        Returns:
            dict: The processed document record containing the extracted
            text and quality evaluation.
        """
        
        
        text = process_html(html)

        quality = evaluate_quality(text)

        document = {
            "url": url,
            "text": text,
            "quality": quality,
        }

        if quality["passed"]:
            self.accepted_writer.write(document)
        else:
            self.rejected_writer.write(document)

        return document