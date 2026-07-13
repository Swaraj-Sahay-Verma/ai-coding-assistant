from extractor.quality import evaluate_quality

bad = "Hello"

good = """
FastAPI is a modern Python framework.
""" * 100

print(evaluate_quality(good))

print(evaluate_quality(bad))