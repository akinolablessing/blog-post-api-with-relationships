from routes.authors import authors_bp
from routes.posts import posts_bp


def register_routes(app):
    app.register_blueprint(authors_bp)
    app.register_blueprint(posts_bp)
