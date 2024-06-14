from flask import Blueprint, request, jsonify
from models import LogEntry, db

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api/logs', methods=['GET'])
def get_logs():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    ip = request.args.get('ip')
    query = LogEntry.query
    if start_date:
        query = query.filter(LogEntry.timestamp >= start_date)
    if end_date:
        query = query.filter(LogEntry.timestamp <= end_date)
    if ip:
        query = query.filter(LogEntry.ip == ip)
    logs = query.all()
    return jsonify([log.to_dict() for log in logs])

# Пример другого эндпоинта API, для создания нового лога
@api_blueprint.route('/api/logs', methods=['POST'])
def create_log():
    data = request.get_json()
    new_log = LogEntry(
        ip=data['ip'],
        timestamp=data['timestamp'],
        request=data['request'],
        status=data['status'],
        size=data['size']
    )
    db.session.add(new_log)
    db.session.commit()
    return jsonify({'message': 'Log created successfully'}), 201
