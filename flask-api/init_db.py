import os
import psycopg2

def connect_db():
        conn = psycopg2.connect(host="localhost",
                        database="flask_api",
                        user="api_user",
                        password="API_Password"
                        # user=os.environ['DB_USERNAME'],
                        # password=os.environ['DB_PASSWORD'])
                )
        return conn


def create_tables():
        conn = connect_db()
        cur = conn.cursor()

        # Create User table
        # cur.execute('DROP TABLE IF EXISTS users')
        cur.execute('CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY,'
                                        'username varchar (150) NOT NULL UNIQUE,'
                                        'fullname varchar (50) NOT NULL,'
                                        'gender varchar (10) NOT NULL,'
                                        'age integer NOT NULL,'
                                        'status varchar,'
                                        'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                        )

        # Create todo table
        # cur.execute('DROP TABLE IF EXISTS todos')
        cur.execute('CREATE TABLE IF NOT EXISTS todos (id serial PRIMARY KEY,'
                                        'username varchar (150) NOT NULL,'
                                        'task varchar (50) NOT NULL,'
                                        'status varchar,'
                                        'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                        )


        conn.commit()

        cur.close()
        conn.close()

        return True

# create_tables()