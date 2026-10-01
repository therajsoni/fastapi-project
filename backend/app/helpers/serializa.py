def serialize_doc(doc):
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc
def serialize_docs(docs):
    return [serialize_doc(doc) for doc in docs]    
