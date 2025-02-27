from flask import Blueprint, jsonify
from db_config import mysql

# Create a Blueprint for view routes
delete_bp = Blueprint('delete', __name__)

@delete_bp.route('/employees/delete/<int:emp_id>', methods=['DELETE'])
def delete_data(emp_id):
    cur = mysql.connection.cursor()
    cur.execute('''DELETE FROM employee WHERE emp_id = %s''', (emp_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Data deleted successfully'})
