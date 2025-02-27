from flask import Blueprint, request, jsonify
from db_config import mysql

# Create a Blueprint for insertion routes
insert_bp = Blueprint('insert', __name__)

@insert_bp.route('/data', methods=['POST'])
def add_data():
    try:
        data = request.json
        print("Received Data:", data)

        emp_id = data['emp_id']
        birth_date = data['birth_date']
        first_name = data['first_name']
        last_name = data['last_name']
        gender = data['gender']
        hire_date = data['hire_date']
        dep_id = int(data['dep_id'])

        cur = mysql.connection.cursor()
        cur.execute(
            '''INSERT INTO employee (emp_id, birth_date, first_name, last_name, gender, hire_date, dep_id) 
               VALUES (%s, %s, %s, %s, %s, %s, %s)''',
            (emp_id, birth_date, first_name, last_name, gender, hire_date, dep_id)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Data added successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
