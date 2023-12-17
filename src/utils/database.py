import MySQLdb

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'password',
    'db': 'MediCareHub',
}

# Create a connection to the database
conn = MySQLdb.connect(**db_config)