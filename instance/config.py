import os
SQLALCHEMY_DATABASE_URI = 'postgresql://BHarris:@localhost:5432/supplements'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False