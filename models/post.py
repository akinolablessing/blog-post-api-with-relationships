from bson import ObjectId

def create_post_document(data):
    return {
        "title": data.get("title"),
        "content": data.get("content"),
        "author_id": ObjectId(data.get("author_id"))
    }