from dataset.writer import DatasetWriter

accepted_writer = DatasetWriter(
    filename="accepted.jsonl"
)

rejected_writer = DatasetWriter(
    filename="rejected.jsonl"
)

good_document = {
    "url": "https://good.com",
    "text": "High quality text",
    "quality": {
        "passed": True
    }
}

bad_document = {
    "url": "https://bad.com",
    "text": "Hi",
    "quality": {
        "passed": False
    }
}

for document in (good_document, bad_document):
    if document["quality"]["passed"]:
        accepted_writer.write(document)
    else:
        rejected_writer.write(document)

print(
    "Accepted:",
    accepted_writer.get_document_count()
)

print(
    "Rejected:",
    rejected_writer.get_document_count()
)