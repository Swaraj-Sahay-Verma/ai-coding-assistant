"""
Dataset policy filtering.

This module decides whether a processed document should be accepted
into the training dataset.

Unlike extractor.quality, which evaluates the quality of extracted
text, this module evaluates dataset-level policies.

Examples of future policy checks:
- Duplicate detection
- Language validation
- PII detection
- License compliance
- Readability scoring
- Toxicity filtering
- AI-assisted quality scoring

Pipeline Position:
    Extracted Document
            ↓
    Dataset Policy Filter   ← This module
            ↓
    Accepted / Rejected Dataset
"""
from crawler.hasher import content_hash

class QualityFilter:
    """
    Applies dataset-level acceptance policies.

    This class acts as the final gatekeeper before a document is written
    into the training dataset.
    """
    
    def __init__(self):
        """
        Initialize the policy engine.

        The filter keeps track of hashes of previously accepted
        documents so exact duplicates can be rejected efficiently.
        """
        self.seen_hashes = set()


    def evaluate(self, document: dict) -> dict:
        """
        Evaluate whether a document satisfies dataset policies.

        Args:
            document: Processed document produced by DatasetPipeline.

        Returns:
            dict containing:
                accepted: bool
                reasons: list[str]
        """
        
        quality = document["quality"]
        accepted = quality["passed"]
        reasons = list(quality["reasons"])
        
        content_fingerprint = content_hash(document["text"])
        
        if accepted and content_fingerprint in self.seen_hashes:
            accepted = False
            reasons.append("Duplicate document.")
        
        if accepted:
            self.seen_hashes.add(content_fingerprint)
        
        return {
            "accepted": accepted,
            "reasons": reasons,
        }