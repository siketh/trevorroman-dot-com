#!flask/bin/python

# This script is a modification of a script authored by Miguel Grinberg as part of his Flask Mega Tutorial:
# http://blog.miguelgrinberg.com/index

from app import configuration
from migrate.versioning import api

current_config = configuration

v = api.db_version(current_config.SQLALCHEMY_DATABASE_URI, current_config.SQLALCHEMY_MIGRATE_REPO)
api.downgrade(current_config.SQLALCHEMY_DATABASE_URI, current_config.SQLALCHEMY_MIGRATE_REPO, v - 1)
v = api.db_version(current_config.SQLALCHEMY_DATABASE_URI, current_config.SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))
