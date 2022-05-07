import psycopg2

connection = psycopg2.connect(database='tomdb', user='tom', password='glnvod', host='47.100.138.122', port='5432')

cur = connection.cursor()


