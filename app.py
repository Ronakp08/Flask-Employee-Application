from flask import Flask
from flask_cors import CORS
from db_config import init_app
from insert import insert_bp  # Importing Blueprint
from view import view_bp
from search_view import search_view_bp
from delete_user import delete_bp
from update import update_bp
from fetch_relation import fetch_relation_bp


app = Flask(__name__)
CORS(app)

# Initialize database
init_app(app)

# Register Blueprints
app.register_blueprint(insert_bp)

# View Blueprints
app.register_blueprint(view_bp)

# Search View Blueprints
app.register_blueprint(search_view_bp)

# Delete user Blueprints
app.register_blueprint(delete_bp)

# Update user Blueprints
app.register_blueprint(update_bp)

# table relation Blueprints
app.register_blueprint(fetch_relation_bp)

if __name__ == "__main__":
    app.run(debug=True)
