import os
# SQLALCHEMY_DATABASE_URI = 'postgresql://BHarris:@localhost:5432/supplements'
SQLALCHEMY_DATABASE_URI = os.environ.get('SQL_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False