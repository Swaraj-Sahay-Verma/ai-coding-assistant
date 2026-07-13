"""
Quality filtering utilities for extracted text.

This module evaluates whether normalized text is suitable for inclusion
in the AI training dataset. It applies lightweight heuristic rules to
remove low-quality, noisy, or uninformative documents before dataset
creation.

Current quality checks:
- Character count
- Word count
- Alphabetic character ratio

The implementation follows the Single Responsibility Principle by keeping
each quality rule independent and composable. This design allows new
filters, such as language detection, repetition analysis, readability
scoring, or entropy estimation, to be added without modifying the existing
architecture.

Pipeline Position:
    Raw HTML
        ↓
    Content Extraction
        ↓
    Text Normalization
        ↓
    Quality Filtering   ← This module
        ↓
    AI Training Dataset

Main Entry Point:
    is_high_quality(text)
"""


MIN_CHARACTERS = 300
MAX_CHARACTERS = 100_000

MIN_WORDS = 50

MIN_ALPHABET_RATIO = 0.50


def character_count(text: str) -> int:
    return len(text)


def word_count(text: str) -> int:
    return len(text.split())


def alphabet_ratio(text: str) -> float:
    if not text:
        return 0.0
    
    letters = sum(char.isalpha() for char in text)
    
    return letters / len(text)



def compute_metrics(text: str) -> dict:
    return {
        "characters": character_count(text),
        "words": word_count(text),
        "alphabet_ratio": alphabet_ratio(text),
    }
    
    

def passes_length(metrics: dict) -> bool:
    length = metrics["characters"]
    
    return MIN_CHARACTERS <= length <= MAX_CHARACTERS


def passes_word_count(metrics: dir) -> bool:
    return metrics["words"] >= MIN_WORDS


def passes_alphabet_ratio(metrics: dir) -> bool:
    return metrics["alphabet_ratio"] >= MIN_ALPHABET_RATIO



def is_high_quality(text: dir) -> bool:
    return evaluate_quality(text)["passed"]
    
def evaluate_quality(text: str) -> dict:
    metrics = compute_metrics(text)
    
    passed = (
        passes_length(metrics)
        and passes_word_count(metrics)
        and passes_alphabet_ratio(metrics)
    )
    
    return {
        "passed": passed,
        "metrics": metrics,
    }