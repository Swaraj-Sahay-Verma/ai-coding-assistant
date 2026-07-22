from pipeline.quality_filter import QualityFilter
from dataset.writer import DatasetWriter

def test_first_document_is_accepted():
    """
    The first unique document should be accepted.
    """

    quality_filter = QualityFilter()

    document = {
        "text": "Python is awesome " * 100,
        "quality": {
            "passed": True,
            "reasons": [],
        },
    }

    result = quality_filter.evaluate(document)

    assert result["accepted"] is True