from flask import Blueprint, jsonify, request
from db_config import mysql

update_bp = Blueprint('update', __name__)

@update_bp.route('/employee/update/<int:id>', methods=['PUT'])
def update_data(id):
    try:
        data = request.json
        first_name = data['first_name']
        last_name = data['last_name']
        dep_id = int(data['dep_id']) 

        cur = mysql.connection.cursor()
        cur.execute(
            '''UPDATE employee 
               SET first_name = %s, last_name = %s, dep_id = %s 
               WHERE emp_id = %s''',
            (first_name, last_name, dep_id, id)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Data updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
