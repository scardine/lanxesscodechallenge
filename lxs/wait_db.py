import psycopg2
import time

while True:
    try:
        conn = psycopg2.connect('host=db user=postgres dbname=postgres')
    except psycopg2.OperationalError:
        print("Database not availabe. Waiting...")
        time.sleep(1)
    else:
        break