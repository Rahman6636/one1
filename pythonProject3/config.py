import os

class Config:
    FILES_DIR = os.getenv('FILES_DIR', '/apache/logs')
    EXT = os.getenv('EXT', 'log')
    FORMAT = os.getenv('FORMAT', '%h %l %t "%r" %>s %b')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/dbname')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
