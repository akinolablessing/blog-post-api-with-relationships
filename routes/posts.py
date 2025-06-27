from flask import Blueprint, request, jsonify
from database.blog_post_database import mongo
from bson import ObjectId
from models.post import create_post_document
from schemas.post_schema import PostSchema

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/posts', methods=['GET'])
def get_posts():
    posts = list(mongo.db.posts.find())
    for post in posts:
        post['_id'] = str(post['_id'])
        post['author_id'] = str(post['author_id'])
    return jsonify(posts)

@posts_bp.route('/posts/<post_id>', methods=['GET'])
def get_post(post_id):
    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    if not post:
        return jsonify({"error": "Post not found"}), 404
    post['_id'] = str(post['_id'])
    post['author_id'] = str(post['author_id'])
    return jsonify(post)

@posts_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    errors = PostSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    if not mongo.db.authors.find_one({"_id": ObjectId(data['author_id'])}):
        return jsonify({"error": "Author not found"}), 404

    post = create_post_document(data)
    result = mongo.db.posts.insert_one(post)
    return jsonify({"id": str(result.inserted_id)}), 201

@posts_bp.route('/posts/<post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    update_data = {key: value for key, value in data.items() if key in ["title", "content"]}
    mongo.db.posts.update_one({"_id": ObjectId(post_id)}, {"$set": update_data})
    return jsonify({"message": "Post updated"})

@posts_bp.route('/posts/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    mongo.db.posts.delete_one({"_id": ObjectId(post_id)})
    return jsonify({"message": "Post deleted"})
