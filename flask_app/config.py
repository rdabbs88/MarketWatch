import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    ALPHA_VANTAGE_API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY', 'OBB3DO3Y1GQXDMP7')
