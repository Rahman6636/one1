from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    request = db.Column(db.String, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    size = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'ip': self.ip,
            'timestamp': self.timestamp.isoformat(),
            'request': self.request,
            'status': self.status,
            'size': self.size
        }
