import psycopg2

connection = psycopg2.connect(database='tomdb', user='tom', password='glnvod', host='127.0.0.1', port='5432')

cur = connection.cursor()


