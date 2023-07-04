import mysql.connector

database_config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : '',
    'database' : ' finance-tracking'
    
}

connection = mysql.connector.connect(**database_config)