import MySQLdb

# Database configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'passwd': '',
    'db': 'json-test',
}

# Create a connection to the database
conn = MySQLdb.connect(**db_config)