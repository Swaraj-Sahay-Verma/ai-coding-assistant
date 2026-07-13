from dataset.writer import DatasetWriter
from pipeline.dataset_pipeline import DatasetPipeline

accepted = DatasetWriter(
    filename="accepted.jsonl"
)

rejected = DatasetWriter(
    filename="rejected.jsonl"
)

pipeline = DatasetPipeline(
    accepted,
    rejected,
)

html = """
<html>
<body>

<article>

<h1>FastAPI Tutorial</h1>

<p>
""" + ("FastAPI is awesome. " * 200) + """

</p>
</article>
</body>
</html>
"""

document = pipeline.process(
    "https://example.com",
    html,
)

print(document["quality"])

print(
    accepted.get_document_count()
)

print(
    rejected.get_document_count()
)
