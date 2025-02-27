from flask import Blueprint, jsonify
from db_config import mysql

fetch_relation_bp = Blueprint('fetch_relation', __name__)

@fetch_relation_bp.route('/employees/emp_dep', methods=['GET'])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT e.emp_id,e.first_name,e.last_name,e.hire_date,d.dep_name FROM employee e JOIN department d ON e.dep_id = d.dep_id''')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)