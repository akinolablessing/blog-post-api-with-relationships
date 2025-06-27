
from flask import Flask
from config import Config
from database.blog_post_database import mongo
from routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)

mongo.init_app(app)
register_routes(app)

@app.route('/')
def index():
    return "bad afeez"

if __name__ == '__main__':
    app.run(debug=True)