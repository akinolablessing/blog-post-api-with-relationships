from flask import Blueprint, request, jsonify
from database.blog_post_database import mongo

from models import author
from models.author import create_author_document
from schemas.author_schema import AuthorSchema

authors_bp = Blueprint('authors', __name__)

@authors_bp.route('/get_authors', methods=['GET'])
def get_authors():
    authors = list(mongo.db.authors.find())
    for autor in authors:
        autor['_id'] = str(autor['_id'])
    return jsonify(authors)

@authors_bp.route('/add_authors', methods=['POST'])
def add_author():
    data = request.get_json()
    errors = AuthorSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    author = create_author_document(data)
    result = mongo.db.authors.insert_one(author)
    return jsonify({"id": str(result.inserted_id)}), 201