# parser.py
import os
import re
from datetime import datetime
from models import db, LogEntry
from config import Config
from app import create_app

log_pattern = re.compile(r'(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+)')

def parse_log_line(line):
    match = log_pattern.match(line)
    if match:
        data = match.groupdict()
        data['timestamp'] = datetime.strptime(data['timestamp'], '%d/%b/%Y:%H:%M:%S %z')
        data['status'] = int(data['status'])
        data['size'] = int(data['size'])
        return data
    return None

def parse_logs():
    app = create_app()
    with app.app_context():
        for root, dirs, files in os.walk(Config.FILES_DIR):
            for file in files:
                if file.endswith(Config.EXT):
                    with open(os.path.join(root, file)) as f:
                        for line in f:
                            data = parse_log_line(line)
                            if data:
                                entry = LogEntry(**data)
                                db.session.add(entry)
        db.session.commit()

if __name__ == '__main__':
    parse_logs()
