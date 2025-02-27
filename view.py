from flask import Blueprint, jsonify
from db_config import mysql

# Create a Blueprint for view routes
view_bp = Blueprint('view', __name__)

@view_bp.route('/employees', methods=['GET'])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM employee''')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)
