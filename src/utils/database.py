import MySQLdb

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '12345678',
    'db': 'MediCareHub',
}

# Create a connection to the database
conn = MySQLdb.connect(**db_config)