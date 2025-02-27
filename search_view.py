from flask import Blueprint, request, jsonify
from db_config import mysql

# Create a Blueprint for view routes
search_view_bp = Blueprint('search_view', __name__)

@search_view_bp.route('/employees/<int:emp_id>', methods=['GET'])
def get_data_by_id(emp_id):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM employee WHERE emp_id = %s''', (emp_id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)
