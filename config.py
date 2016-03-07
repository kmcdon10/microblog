import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = "name"
MAIL_PASSWORD = "password123"

# admin list
ADMINS = ['katemcdonald39@gmail.com']

