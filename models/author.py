from bson import ObjectId

def create_author_document(data):
    return {
        "name": data.get("name"),
        "email": data.get("email")
    }