from extractor.quality import evaluate_quality, is_high_quality

sample = "FastAPI is a modern Python framework. " * 50

print(evaluate_quality(sample))
print(is_high_quality(sample))