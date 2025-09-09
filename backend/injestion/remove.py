def remove_metadata(documents):
    for doc in documents:
        doc.metadata = {}  # Clear metadata completely
    return documents
